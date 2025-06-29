# 財務諸表可視化アプリ

Streamlit、Pandas、Plotlyを使用した財務諸表の可視化アプリケーションです。

## 機能

- 📊 損益計算書の可視化
- 📈 財務指標の計算（ROA、ROE、負債比率など）
- 🏦 貸借対照表の表示
- 📄 PDFからの損益計算書データ抽出
- 📊 インタラクティブなグラフ表示

## 🚀 セットアップ手順（Cursorから始める）

### 1. Cursorを起動
1. Cursorアプリケーションを開く
2. 「Open Folder」または「フォルダを開く」をクリック
3. 新しいフォルダを作成して選択（例：`financial_visualizer`）

### 2. プロジェクトファイルの準備
Cursorで以下のファイルを作成してください：

#### `app.py` - メインアプリケーション
```python
# このファイルの内容は、GitHubリポジトリからコピーしてください
```

#### `requirements.txt` - 必要なライブラリ
```
streamlit==1.28.1
pandas==2.1.3
plotly==5.17.0
numpy==1.24.3
openpyxl==3.1.2
xlrd==2.0.1
requests==2.31.0
yfinance==0.2.18
python-dotenv==1.0.0
pdfplumber==0.9.0
```

#### `.gitignore` - 除外ファイル設定
```
# Virtual Environment
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Streamlit
.streamlit/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
*.tmp
*.temp
```

### 3. Python環境の確認
1. Cursorの下部にあるターミナルを開く（Ctrl + `）
2. Pythonがインストールされているか確認：
   ```bash
   python --version
   ```
3. バージョンが表示されない場合は、Pythonをインストール：
   - https://www.python.org/downloads/ からダウンロード
   - インストール時に「Add Python to PATH」にチェック

### 4. 仮想環境の作成
ターミナルで以下のコマンドを実行：

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**成功すると、プロンプトの先頭に `(venv)` が表示されます**

### 5. 必要なライブラリのインストール
仮想環境が有効な状態で以下を実行：

```bash
# pipを最新版に更新
pip install --upgrade pip

# 必要なライブラリをインストール
pip install -r requirements.txt
```

**インストールが完了するまで数分かかる場合があります**

### 6. アプリケーションの実行
```bash
# Streamlitアプリを起動
python -m streamlit run app.py
```

**成功すると、以下のようなメッセージが表示されます：**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.xxx:8501
```

### 7. ブラウザでアプリにアクセス
1. 自動的にブラウザが開かない場合は、手動で以下にアクセス：
   - http://localhost:8501
   - http://127.0.0.1:8501

2. 財務諸表可視化アプリが表示されます！

## 📄 PDF機能の使用方法

### PDFからのデータ抽出
1. アプリの上部にある「📄 PDF損益計算書アップロード」セクションを確認
2. 「損益計算書のPDFファイルを選択してください」をクリック
3. 損益計算書が含まれるPDFファイルを選択
4. 自動的にデータが抽出されます
5. 「このデータを使用」ボタンをクリックしてデータを保存
6. 抽出されたデータがグラフに反映されます

### 対応しているPDF形式
- 損益計算書が含まれるPDFファイル
- 以下の項目を自動検出：
  - 売上高
  - 売上原価
  - 販管費
  - 営業利益
  - 営業外収益
  - 営業外費用
  - 税引前当期純利益
  - 法人税等
  - 当期純利益

## 🔧 トラブルシューティング

### Pythonが見つからない場合
```bash
# Pythonのパスを確認
where python
# または
which python
```

### 仮想環境が有効にならない場合
```bash
# PowerShellの場合
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

### Streamlitコマンドが認識されない場合
```bash
# 仮想環境が有効になっているか確認（プロンプトに(venv)があるか）
# 有効になっていない場合：
venv\Scripts\activate

# それでも問題がある場合：
python -m streamlit run app.py
```

### ライブラリのインストールエラー
```bash
# pipを更新
pip install --upgrade pip

# 個別にインストール
pip install streamlit pandas plotly numpy pdfplumber
```

### ポート8501が使用中の場合
```bash
# 別のポートで実行
python -m streamlit run app.py --server.port 8502
```

## 📁 プロジェクト構造
```
financial_visualizer/
├── app.py              # メインアプリケーション
├── requirements.txt    # 必要なライブラリ
├── .gitignore         # Git除外設定
├── README.md          # このファイル
└── venv/              # 仮想環境（自動生成）
```

## 🎯 次のステップ

アプリが正常に動作したら：
1. 実際の財務データでテスト
2. PDF機能の活用
3. グラフのカスタマイズ
4. 新しい機能の追加

## 📞 サポート

問題が発生した場合：
1. エラーメッセージを確認
2. 仮想環境が有効になっているか確認
3. 必要なライブラリがインストールされているか確認
4. 上記のトラブルシューティングを試す

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。
