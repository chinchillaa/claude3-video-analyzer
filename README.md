# Claude3 Video Analyzer

Claude3 Video Analyzerは、Anthropic社のClaude-3モデルのマルチモーダル機能を利用して、MP4形式の動画をプロンプトに基づいて解析するPythonプロジェクトです。

## 主な機能

- MP4動画からフレームを抽出し、base64エンコードされた画像データに変換
- プロンプトとエンコードされた画像データをClaude-3モデルに送信し、動画の内容を解析
- 解析結果をテキストとして出力
- **CLI対応** - コマンドラインから簡単に実行可能
- **カスタムプロンプト対応** - 様々な分析ニーズに対応

## 必要条件

- Python 3.9以上（3.9.19で動作確認済み）
- AnthropicのAPIキー

## インストール

### クイックセットアップ（推奨）

```bash
# リポジトリのクローン
git clone https://github.com/Olemi-llm-apprentice/claude3-video-analyzer.git
cd claude3-video-analyzer

# セットアップスクリプトの実行
./setup.sh
```

### 手動セットアップ

1. リポジトリをクローンします:
```bash
git clone https://github.com/Olemi-llm-apprentice/claude3-video-analyzer.git
cd claude3-video-analyzer
```

2. Python仮想環境を作成・有効化します:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
```

3. 依存関係をインストールします:
```bash
# uvを使用する場合（推奨）
uv pip install -r requirements.txt
uv pip install "numpy<2"  # OpenCV互換性のため
uv pip install --upgrade anthropic

# pipを使用する場合
pip install -r requirements.txt
pip install "numpy<2"
pip install --upgrade anthropic
```

4. AnthropicのAPIキーを設定します:
`.env`ファイルを作成し、APIキーを設定：
```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

## 使用方法

### CLI使用方法（推奨）

基本的な使い方:
```bash
python main.py <動画ファイルパス>
```

カスタムプロンプトを使用:
```bash
python main.py <動画ファイルパス> -p "この動画の内容を詳しく説明してください"
```

全てのオプション:
```bash
python main.py <動画ファイルパス> \
  -p "カスタムプロンプト" \
  -m claude-3-5-haiku-20241022 \
  --max-images 30
```

### 利用可能なオプション

- `-p, --prompt`: 動画解析用のプロンプト（デフォルト：動画の流れを日本語で解説）
- `-m, --model`: 使用するClaudeモデル
  - `claude-3-5-sonnet-20241022`（デフォルト）
  - `claude-3-5-haiku-20241022`
  - `claude-3-opus-20240229`
- `--max-images`: 解析に使用する最大フレーム数（デフォルト：20）

### プロンプトテンプレートの使用

`prompts`ディレクトリに様々なプロンプトテンプレートが用意されています：

```bash
# 詳細分析プロンプトを使用
python main.py <動画パス> -p "$(cat prompts/detailed_analysis_prompt.txt)"

# シンプルな分析
python main.py <動画パス> -p "$(cat prompts/simple_analysis_prompt.txt)"
```

### 従来の使用方法（直接編集）

`main.py`を直接編集する場合:

```python
if __name__ == "__main__":
    video_file_path = "path/to/video.mp4"
    prompt = "動画の内容を説明してください"
    model = "claude-3-5-sonnet-20241022"
    
    get_text_from_video(video_file_path, prompt, model)
```

## 実行例

Excel操作動画の解析:
```bash
python main.py "/path/to/excel_tutorial.mp4" \
  -p "Excelの操作手順を詳しく説明してください" \
  --max-images 30
```

## セットアップ済み環境

このプロジェクトは`/home/chinchilla/utils/claude3-video-analyzer`に配置されています。

仮想環境の有効化:
```bash
cd /home/chinchilla/utils/claude3-video-analyzer
source .venv/bin/activate
```

## トラブルシューティング

### ModuleNotFoundError
仮想環境が有効化されていない場合に発生します：
```bash
source .venv/bin/activate
```

### NumPy互換性エラー
OpenCVとNumPy 2.xの互換性問題の場合：
```bash
uv pip install "numpy<2"
```

### APIキーエラー
`.env`ファイルにAPIキーが正しく設定されているか確認してください。

## 注意事項

- Python 3.9.19で動作確認済みです（元のプロジェクトは3.10.13を要求）
- 仮想環境の有効化を忘れずに行ってください
- APIキーは適切に管理し、Gitにコミットしないよう注意してください
- 長い動画や詳細なプロンプトの場合、処理時間が長くなることがあります

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。