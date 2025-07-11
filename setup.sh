#!/bin/bash
# Claude3 Video Analyzer セットアップスクリプト

echo "Claude3 Video Analyzer のセットアップを開始します..."

# 現在のディレクトリに移動
cd /home/chinchilla/utils/claude3-video-analyzer

# 既存の仮想環境があれば削除
if [ -d ".venv" ]; then
    echo "既存の仮想環境を削除します..."
    rm -rf .venv
fi

# 新しい仮想環境を作成
echo "Python仮想環境を作成します..."
python -m venv .venv

# 仮想環境を有効化
echo "仮想環境を有効化します..."
source .venv/bin/activate

# 依存関係をインストール
echo "依存関係をインストールします..."
uv pip install -r requirements.txt
uv pip install "numpy<2"
uv pip install --upgrade anthropic

echo "セットアップが完了しました！"
echo ""
echo "使用方法:"
echo "1. 仮想環境を有効化: source .venv/bin/activate"
echo "2. 動画を解析: python main.py <動画パス>"
echo ""
echo "注意: .envファイルにAnthropicのAPIキーを設定してください。"