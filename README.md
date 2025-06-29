# 財務諸表可視化アプリ

Streamlit、Pandas、Plotlyを使用した財務諸表の可視化アプリケーションです。

## 機能

- 📊 損益計算書の可視化
- 📈 財務指標の計算（ROA、ROE、負債比率など）
- 🏦 貸借対照表の表示
- 📄 PDFからの損益計算書データ抽出
- 📊 インタラクティブなグラフ表示

## セットアップ手順

### 1. 必要な環境
- Python 3.7以上
- pip

### 2. プロジェクトのクローン/ダウンロード
```bash
# プロジェクトディレクトリを作成
mkdir financial_visualizer
cd financial_visualizer

# ファイルをコピー
# - app.py
# - requirements.txt
# - README.md
```

### 3. 仮想環境の作成と有効化
```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 4. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 5. アプリケーションの実行
```bash
python -m streamlit run app.py
```

### 6. ブラウザでアクセス
アプリケーションは以下のURLでアクセスできます：
- http://localhost:8501
- http://127.0.0.1:8501

## 使用方法

### 基本的な使用方法
1. アプリを起動
2. サンプルデータが表示されます
3. 各種グラフと財務指標を確認

### PDFからのデータ抽出
1. 「PDF損益計算書アップロード」セクションでPDFファイルをアップロード
2. 自動的に損益計算書のデータが抽出されます
3. 「このデータを使用」ボタンでデータを保存
4. 抽出されたデータがグラフに反映されます

## 対応しているPDF形式
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

## トラブルシューティング

### Streamlitコマンドが認識されない場合
```bash
python -m streamlit run app.py
```

### ライブラリのインストールエラー
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。 