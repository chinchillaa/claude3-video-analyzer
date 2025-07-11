import anthropic
import base64
import cv2
from dotenv import load_dotenv
import os
import argparse

# APIキーの取得
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    # 環境変数にAPIキーがない場合は、.envファイルから読み取る
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    # 環境変数にも.envファイルにもAPIキーがない場合は、エラーメッセージを表示して終了する
    print("Error: ANTHROPIC_API_KEY not found in environment variables or .env file.")
    exit(1)

# Anthropicクライアントの初期化
client = anthropic.Anthropic(api_key=api_key)

def get_frames_from_video(file_path, max_images=20):
    video = cv2.VideoCapture(file_path)
    base64_frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64_frame = base64.b64encode(buffer).decode("utf-8")
        base64_frames.append(base64_frame)
    video.release()

    # 選択する画像の数を制限する
    selected_frames = base64_frames[0::len(base64_frames)//max_images][:max_images]

    return selected_frames, buffer

def get_text_from_video(file_path, prompt, model, max_images=20):
    # ビデオからフレームを取得し、それらをbase64にエンコードする
    print(f"{file_path}:\nフレーム取得開始")
    base64_frames, buffer = get_frames_from_video(file_path, max_images)
    print("フレーム取得完了")
    # Claude APIにリクエストを送信
    with client.messages.stream(
        model=model,  # モデル指定
        max_tokens=1024,  # 最大トークン数
        messages=[
            {
                "role": "user",
                "content": [
                    *map(lambda x: {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": x}}, base64_frames),
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
    ) as stream:
        for text in stream.text_stream: 
            print(text, end="", flush=True)

if __name__ == "__main__":
    # CLI引数のパーサーを設定
    parser = argparse.ArgumentParser(description="Claude-3を使用して動画を解析します")
    parser.add_argument("video_path", help="解析する動画ファイルのパス")
    parser.add_argument("-p", "--prompt", 
                       default="これは動画のフレーム画像です。動画の最初から最後の流れ、動作を微分して日本語で解説してください。",
                       help="動画解析用のプロンプト (デフォルト: 動画の流れを日本語で解説)")
    parser.add_argument("-m", "--model", 
                       default="claude-3-5-sonnet-20241022",
                       choices=["claude-3-5-sonnet-20241022", "claude-3-5-haiku-20241022", "claude-3-opus-20240229"],
                       help="使用するClaudeモデル (デフォルト: claude-3-5-sonnet-20241022)")
    parser.add_argument("--max-images", 
                       type=int, 
                       default=20,
                       help="解析に使用する最大フレーム数 (デフォルト: 20)")
    
    args = parser.parse_args()
    
    # ファイルの存在確認
    if not os.path.exists(args.video_path):
        print(f"エラー: 動画ファイルが見つかりません: {args.video_path}")
        exit(1)
    
    # 動画を解析
    get_text_from_video(args.video_path, args.prompt, args.model, args.max_images)
