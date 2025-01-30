import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import streamlit as st
import gc  # Untuk garbage collection

# ⏳ 1. Fungsi untuk memuat data (gunakan caching agar cepat)
@st.cache_data
def load_data():
    all_data = pd.read_csv("all_data.csv", dtype={
        "customer_zip_code_prefix": "category",
        "customer_city": "category",
        "customer_state": "category",
        "order_status": "category",
        "product_category_name": "category",
        "seller_zip_code_prefix": "category",
        "seller_city": "category",
        "seller_state": "category",
        "payment_type": "category",
        "review_score": "int8",
        "payment_installments": "int8"
    }, parse_dates=["order_purchase_timestamp", "order_delivered_customer_date"])
    
    geolocation_df = pd.read_csv("geolocation_df.csv", dtype={
        "geolocation_zip_code_prefix": "category",
        "geolocation_city": "category",
        "geolocation_state": "category"
    })
    
    # Tambahkan kolom waktu pembelian
    all_data["purchase_hour"] = all_data["order_purchase_timestamp"].dt.hour
    
    return all_data, geolocation_df


# 📊 2. Visualisasi: Top 10 kategori produk yang paling sering terjual
def plot_top_categories(all_data):
    # Menghitung jumlah produk terjual per kategori
    top_categories = all_data["product_category_name"].value_counts().head(10)

    # Membuat barplot dengan kategori produk di sumbu y dan jumlah produk terjual di sumbu x
    fig, ax = plt.subplots(figsize=(12, 8))  # Ukuran plot yang lebih besar
    sns.barplot(y=top_categories.index, x=top_categories.values, ax=ax, palette="viridis", order=top_categories.index)
    
    # Menambahkan judul dan label
    ax.set_title("Top 10 Kategori Produk yang Paling Sering Terjual")
    ax.set_xlabel("Jumlah Produk Terjual")
    ax.set_ylabel("Kategori Produk")
    
    # Menyajikan plot
    st.pyplot(fig)
    
# 🗺️ 3. Visualisasi: Peta lokasi pelanggan & penjual
def plot_customer_seller_map(all_data, geolocation_df):

    # Sampling data pelanggan dan penjual
    customer_sample = all_data.sample(n=10000, random_state=42)
    seller_sample = all_data.sample(n=10000, random_state=42)

    # Gabungkan lokasi pelanggan
    customer_geo = customer_sample[["customer_zip_code_prefix"]].merge(
        geolocation_df, left_on="customer_zip_code_prefix", right_on="geolocation_zip_code_prefix"
    ).drop_duplicates()

    # Gabungkan lokasi penjual
    seller_geo = seller_sample[["seller_zip_code_prefix"]].merge(
        geolocation_df, left_on="seller_zip_code_prefix", right_on="geolocation_zip_code_prefix"
    ).drop_duplicates()

    # Rename columns for Streamlit compatibility
    customer_geo = customer_geo.rename(columns={"geolocation_lat": "lat", "geolocation_lng": "lon"})
    seller_geo = seller_geo.rename(columns={"geolocation_lat": "lat", "geolocation_lng": "lon"})

    # Menampilkan peta lokasi pelanggan
    st.subheader("Peta Lokasi Pelanggan")
    st.map(customer_geo[["lat", "lon"]])

    # Menampilkan peta lokasi penjual
    st.subheader("Peta Lokasi Penjual")
    st.map(seller_geo[["lat", "lon"]])

# ⏳ 4. Visualisasi: Kapan pelanggan biasanya membeli?
def plot_purchase_distribution(all_data):
    # Membuat kolom untuk hari dan bulan dari kolom 'order_purchase_timestamp'
    all_data['purchase_day'] = all_data['order_purchase_timestamp'].dt.day_name()
    all_data['purchase_month'] = all_data['order_purchase_timestamp'].dt.month_name()
    all_data['purchase_hour'] = all_data['order_purchase_timestamp'].dt.hour
    
    # Pilihan distribusi yang ingin ditampilkan
    option = st.selectbox("Pilih distribusi yang ingin dilihat", ["Jam", "Hari", "Bulan"])

    if option == "Jam":
        # Visualisasi distribusi berdasarkan jam
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(all_data["purchase_hour"], bins=24, kde=True, ax=ax)
        ax.set_title("Distribusi Waktu Pembelian Berdasarkan Jam")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Jumlah Transaksi")
        st.pyplot(fig)

    elif option == "Hari":
        # Visualisasi distribusi berdasarkan hari
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='purchase_day', data=all_data, ax=ax, palette="viridis")
        ax.set_title("Distribusi Pembelian Berdasarkan Hari")
        ax.set_xlabel("Hari")
        ax.set_ylabel("Jumlah Transaksi")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)

    elif option == "Bulan":
        # Visualisasi distribusi berdasarkan bulan
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='purchase_month', data=all_data, ax=ax, palette="viridis")
        ax.set_title("Distribusi Pembelian Berdasarkan Bulan")
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Jumlah Transaksi")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        st.pyplot(fig)

# 🚚 5. Visualisasi: Apakah biaya pengiriman meningkat seiring berat produk?
def plot_shipping_vs_weight(all_data):
    # Ubah berat produk dari gram ke kilogram
    all_data['product_weight_kg'] = all_data['product_weight_g'] / 1000

    # Tentukan kategori berat produk dalam kilogram (misalnya dalam rentang 0-0.5kg, 0.5-1kg, dll.)
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, float('inf')]  # Menambahkan kategori > 5kg
    labels = ['0-0.5 kg', '0.5-1 kg', '1-1.5 kg', '1.5-2 kg', '2-2.5 kg', '2.5-3 kg', '3-3.5 kg', '3.5-4 kg', '4-4.5 kg', '4.5-5 kg', '>5 kg']

    # Membuat kolom kategori berat
    all_data['weight_category'] = pd.cut(all_data['product_weight_kg'], bins=bins, labels=labels)

    # Menghitung rata-rata biaya pengiriman per kategori berat
    avg_shipping_cost = all_data.groupby('weight_category')['freight_value'].mean()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=avg_shipping_cost.index, y=avg_shipping_cost.values, ax=ax, palette="viridis")
    
    # Menambahkan judul dan label
    ax.set_title("Rata-Rata Biaya Pengiriman Berdasarkan Kategori Berat Produk (kg)")
    ax.set_xlabel("Kategori Berat Produk (kg)")
    ax.set_ylabel("Rata-Rata Biaya Pengiriman (IDR)")
    
    # Menampilkan plot
    st.pyplot(fig)

# ⭐ 6. Visualisasi: Tingkat kepuasan berdasarkan metode pembayaran
def plot_review_vs_payment(all_data):
    # Menghitung rata-rata skor ulasan berdasarkan metode pembayaran
    avg_review_score = all_data.groupby('payment_type')['review_score'].mean().reset_index()

    # Membuat grafik garis zigzag
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot garis zigzag
    sns.lineplot(x='payment_type', y='review_score', data=avg_review_score, marker='o', ax=ax, linestyle='-', color='b')

    # Menambahkan judul dan label
    ax.set_title("Tingkat Kepuasan Berdasarkan Metode Pembayaran")
    ax.set_xlabel("Metode Pembayaran")
    ax.set_ylabel("Rata-Rata Skor Ulasan")
    
    # Menampilkan plot
    st.pyplot(fig)

#7. Distribusi Pelanggan Berdasarkan Waktu Pengiriman
def plot_customer_count_by_shipping_time(all_data):
    # Pastikan kolom waktu adalah datetime
    all_data["order_purchase_timestamp"] = pd.to_datetime(all_data["order_purchase_timestamp"], errors="coerce")
    all_data["order_delivered_customer_date"] = pd.to_datetime(all_data["order_delivered_customer_date"], errors="coerce")

    # Hapus nilai NaN (jika ada pesanan yang belum dikirim)
    all_data = all_data.dropna(subset=["order_delivered_customer_date"])

    # Hitung waktu pengiriman dalam hari
    all_data["shipping_time_days"] = (all_data["order_delivered_customer_date"] - all_data["order_purchase_timestamp"]).dt.days

    # Pastikan hanya nilai valid (> 0 hari)
    all_data = all_data[all_data["shipping_time_days"] >= 0]

    # Kategorisasi waktu pengiriman
    all_data["shipping_time_category"] = all_data["shipping_time_days"].apply(lambda x: ">30 hari" if x > 30 else f"{x} hari")

    # Hitung jumlah pelanggan berdasarkan kategori waktu pengiriman
    customer_count_by_shipping = all_data["shipping_time_category"].value_counts().reset_index()
    customer_count_by_shipping.columns = ["shipping_time_category", "customer_count"]

    # Urutkan kategori berdasarkan nilai numerik
    customer_count_by_shipping["sort_key"] = customer_count_by_shipping["shipping_time_category"].apply(
        lambda x: 999 if x == ">30 hari" else int(x.split()[0])
    )
    customer_count_by_shipping = customer_count_by_shipping.sort_values("sort_key")

    # Buat grafik garis zigzag
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        x=customer_count_by_shipping["shipping_time_category"],
        y=customer_count_by_shipping["customer_count"],
        marker="o",
        linestyle="-",
        color="b",
        ax=ax
    )

    # Tambahkan judul dan label
    ax.set_title("Jumlah Pelanggan Berdasarkan Waktu Pengiriman")
    ax.set_xlabel("Waktu Pengiriman (Hari)")
    ax.set_ylabel("Jumlah Pelanggan")
    ax.grid(True, linestyle="--", alpha=0.6)

    # Memutar label sumbu X agar tidak bertabrakan
    ax.set_xticklabels(customer_count_by_shipping["shipping_time_category"], rotation=45, ha="right")

    # Tambahkan angka pada titik data
    for i, txt in enumerate(customer_count_by_shipping["customer_count"]):
        ax.annotate(f"{txt}", (i, customer_count_by_shipping["customer_count"].iloc[i]), 
                    textcoords="offset points", xytext=(0, 8), ha="center", fontsize=10, color="black")

    # Tambahkan padding untuk menghindari label bertabrakan
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Tampilkan grafik di Streamlit
    st.pyplot(fig)

# 🗑️ 8. Fungsi untuk membersihkan memori
def clear_memory():
    gc.collect()