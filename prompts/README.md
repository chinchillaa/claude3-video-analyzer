# Claude3 Video Analyzer プロンプト集

このディレクトリには、動画解析で使用する様々なプロンプトを保存しています。

## プロンプト一覧

### detailed_analysis_prompt.txt / detailed_analysis_prompt.md
Excel操作画面の詳細な分析用プロンプト。タイムスタンプ付きの詳細な操作手順を出力するフォーマットが含まれています。

**分析項目：**
- Excelシートの構造（列名、行、セルの値）
- 操作の順序と具体的な手順
- 使用されているExcel機能の詳細
- 各操作の目的と効果
- ダイアログボックスやメニューの内容
- セルの書式設定の変更
- 数式やリンクの内容

**出力フォーマット：**
- タイムスタンプ付きセクション
- ステップごとの詳細な操作手順
- 結果・補足・確認の説明
- マークダウン形式での強調表示

使用例：
```bash
# テキスト形式のプロンプトを使用
python main.py <動画パス> -p "$(cat prompts/detailed_analysis_prompt.txt)"

# マークダウン形式を確認したい場合
cat prompts/detailed_analysis_prompt.md
```