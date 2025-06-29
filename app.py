import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pdfplumber
import re
from io import BytesIO
import base64

# ページ設定
st.set_page_config(
    page_title="財務諸表可視化アプリ",
    page_icon="📊",
    layout="wide"
)

# タイトル
st.title("📊 財務諸表可視化アプリ")
st.markdown("---")

# サイドバー
st.sidebar.header("設定")
st.sidebar.markdown("### データ選択")

# PDFから損益計算書データを抽出する関数
def extract_income_statement_from_pdf(pdf_file):
    """PDFから損益計算書のデータを抽出"""
    try:
        extracted_data = {}
        
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # 損益計算書の項目を検索
                    patterns = {
                        '売上高': r'売上高[：:]\s*([0-9,]+)',
                        '売上原価': r'売上原価[：:]\s*([0-9,]+)',
                        '販管費': r'販管費[：:]\s*([0-9,]+)',
                        '営業利益': r'営業利益[：:]\s*([0-9,]+)',
                        '営業外収益': r'営業外収益[：:]\s*([0-9,]+)',
                        '営業外費用': r'営業外費用[：:]\s*([0-9,]+)',
                        '税引前当期純利益': r'税引前当期純利益[：:]\s*([0-9,]+)',
                        '法人税等': r'法人税等[：:]\s*([0-9,]+)',
                        '当期純利益': r'当期純利益[：:]\s*([0-9,]+)'
                    }
                    
                    for key, pattern in patterns.items():
                        match = re.search(pattern, text)
                        if match:
                            # カンマを除去して数値に変換
                            value_str = match.group(1).replace(',', '')
                            try:
                                extracted_data[key] = int(value_str)
                            except ValueError:
                                st.warning(f"{key}の値の変換に失敗しました: {value_str}")
        
        return extracted_data
    except Exception as e:
        st.error(f"PDFの読み込みエラー: {e}")
        return {}

# サンプルデータの作成
@st.cache_data
def create_sample_data():
    """サンプルの財務データを作成"""
    try:
        years = list(range(2020, 2025))
        
        # 損益計算書データ
        income_data = {
            '年度': years,
            '売上高': [1000000, 1200000, 1400000, 1600000, 1800000],
            '売上原価': [600000, 720000, 840000, 960000, 1080000],
            '販管費': [200000, 240000, 280000, 320000, 360000],
            '営業利益': [200000, 240000, 280000, 320000, 360000],
            '営業外収益': [10000, 12000, 14000, 16000, 18000],
            '営業外費用': [5000, 6000, 7000, 8000, 9000],
            '税引前当期純利益': [205000, 246000, 287000, 328000, 369000],
            '法人税等': [41000, 49200, 57400, 65600, 73800],
            '当期純利益': [164000, 196800, 229600, 262400, 295200]
        }
        
        # 貸借対照表データ
        balance_data = {
            '年度': years,
            '現金・預金': [200000, 240000, 280000, 320000, 360000],
            '売上債権': [150000, 180000, 210000, 240000, 270000],
            '棚卸資産': [100000, 120000, 140000, 160000, 180000],
            '固定資産': [500000, 600000, 700000, 800000, 900000],
            '流動負債': [300000, 360000, 420000, 480000, 540000],
            '固定負債': [200000, 240000, 280000, 320000, 360000],
            '資本金': [300000, 300000, 300000, 300000, 300000],
            '利益剰余金': [150000, 180000, 210000, 240000, 270000]
        }
        
        return pd.DataFrame(income_data), pd.DataFrame(balance_data)
    except Exception as e:
        st.error(f"データ作成エラー: {e}")
        return pd.DataFrame(), pd.DataFrame()

# PDFアップロードセクション
st.header("📄 PDF損益計算書アップロード")
st.markdown("損益計算書のPDFをアップロードして、データを自動抽出できます。")

uploaded_file = st.file_uploader(
    "損益計算書のPDFファイルを選択してください",
    type=['pdf'],
    help="損益計算書が含まれるPDFファイルをアップロードしてください"
)

# アップロードされたPDFの処理
if uploaded_file is not None:
    st.success(f"ファイルがアップロードされました: {uploaded_file.name}")
    
    # PDFからデータを抽出
    extracted_data = extract_income_statement_from_pdf(uploaded_file)
    
    if extracted_data:
        st.subheader("📊 抽出されたデータ")
        
        # 抽出されたデータを表示
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**抽出された損益計算書データ:**")
            for key, value in extracted_data.items():
                st.write(f"{key}: ¥{value:,}")
        
        with col2:
            # 抽出されたデータをDataFrameに変換
            if extracted_data:
                # 年度を設定（現在の年を仮定）
                current_year = 2024
                extracted_df = pd.DataFrame({
                    '年度': [current_year],
                    **extracted_data
                })
                
                st.write("**データフレーム形式:**")
                st.dataframe(extracted_df)
                
                # データを保存するオプション
                if st.button("このデータを使用"):
                    st.session_state.extracted_data = extracted_df
                    st.success("データが保存されました！")
    else:
        st.warning("PDFから損益計算書のデータを抽出できませんでした。")
        st.info("PDFの形式や内容を確認してください。")

# データの読み込み
try:
    income_df, balance_df = create_sample_data()
    
    if income_df.empty or balance_df.empty:
        st.error("データの読み込みに失敗しました。")
        st.stop()
        
except Exception as e:
    st.error(f"データ読み込みエラー: {e}")
    st.stop()

# 抽出されたデータがある場合は使用
if hasattr(st.session_state, 'extracted_data'):
    st.info("📊 抽出されたPDFデータを使用しています")
    # 抽出されたデータとサンプルデータを結合
    combined_income_df = pd.concat([income_df, st.session_state.extracted_data], ignore_index=True)
else:
    combined_income_df = income_df

# メインコンテンツ
try:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("📈 損益計算書")
        
        # 損益計算書の表示
        st.dataframe(combined_income_df, use_container_width=True)
        
        # 売上高と利益の推移グラフ
        fig_income = make_subplots(
            rows=2, cols=1,
            subplot_titles=('売上高の推移', '利益の推移'),
            vertical_spacing=0.1
        )
        
        # 売上高
        fig_income.add_trace(
            go.Scatter(x=combined_income_df['年度'], y=combined_income_df['売上高'], 
                      mode='lines+markers', name='売上高', line=dict(color='blue')),
            row=1, col=1
        )
        
        # 利益
        fig_income.add_trace(
            go.Scatter(x=combined_income_df['年度'], y=combined_income_df['営業利益'], 
                      mode='lines+markers', name='営業利益', line=dict(color='green')),
            row=2, col=1
        )
        fig_income.add_trace(
            go.Scatter(x=combined_income_df['年度'], y=combined_income_df['当期純利益'], 
                      mode='lines+markers', name='当期純利益', line=dict(color='red')),
            row=2, col=1
        )
        
        fig_income.update_layout(height=600, showlegend=True)
        st.plotly_chart(fig_income, use_container_width=True)

    with col2:
        st.header("💰 財務指標")
        
        # 最新年度のデータを取得
        latest_year = combined_income_df['年度'].max()
        latest_income = combined_income_df[combined_income_df['年度'] == latest_year].iloc[0]
        latest_balance = balance_df[balance_df['年度'] == latest_year].iloc[0]
        
        # 財務指標の計算
        sales = latest_income['売上高']
        net_income = latest_income['当期純利益']
        total_assets = (latest_balance['現金・預金'] + latest_balance['売上債権'] + 
                       latest_balance['棚卸資産'] + latest_balance['固定資産'])
        total_liabilities = latest_balance['流動負債'] + latest_balance['固定負債']
        equity = latest_balance['資本金'] + latest_balance['利益剰余金']
        
        # 指標の表示
        st.metric("売上高", f"¥{sales:,}")
        st.metric("当期純利益", f"¥{net_income:,}")
        st.metric("総資産", f"¥{total_assets:,}")
        
        # ゼロ除算を避ける
        if total_assets > 0:
            st.metric("ROA", f"{(net_income/total_assets)*100:.1f}%")
        else:
            st.metric("ROA", "N/A")
            
        if equity > 0:
            st.metric("ROE", f"{(net_income/equity)*100:.1f}%")
        else:
            st.metric("ROE", "N/A")
            
        if equity > 0:
            st.metric("負債比率", f"{(total_liabilities/equity)*100:.1f}%")
        else:
            st.metric("負債比率", "N/A")

    # 貸借対照表セクション
    st.markdown("---")
    st.header("🏦 貸借対照表")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("資産の部")
        st.dataframe(balance_df[['年度', '現金・預金', '売上債権', '棚卸資産', '固定資産']], 
                    use_container_width=True)

    with col4:
        st.subheader("負債・純資産の部")
        st.dataframe(balance_df[['年度', '流動負債', '固定負債', '資本金', '利益剰余金']], 
                    use_container_width=True)

    # 資産構成の円グラフ
    st.subheader("資産構成（最新年度）")
    latest_balance_row = balance_df[balance_df['年度'] == latest_year].iloc[0]

    assets_data = {
        '項目': ['現金・預金', '売上債権', '棚卸資産', '固定資産'],
        '金額': [
            latest_balance_row['現金・預金'],
            latest_balance_row['売上債権'],
            latest_balance_row['棚卸資産'],
            latest_balance_row['固定資産']
        ]
    }

    fig_pie = px.pie(
        pd.DataFrame(assets_data), 
        values='金額', 
        names='項目',
        title=f"{latest_year}年度 資産構成"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

except Exception as e:
    st.error(f"アプリケーションエラー: {e}")
    st.info("ページを再読み込みしてください。")

# フッター
st.markdown("---")
st.markdown("*このアプリはサンプルデータを使用しています。実際の財務データでご利用ください。*") 