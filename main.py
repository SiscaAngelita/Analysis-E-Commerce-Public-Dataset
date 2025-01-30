import streamlit as st 
import func  # Import file func.py

# 🎯 Judul Aplikasi
st.title("Dashboard E-Commerce Analysis")

# ⏳ Load Data
all_data, geolocation_df = func.load_data()

# 📊 1. Kategori Produk yang Paling Sering Terjual
st.header("Kategori Produk yang Paling Sering Terjual")
func.plot_top_categories(all_data)

# 🗺️ 2. Persebaran Lokasi Pelanggan dan Penjual
st.header("Persebaran Lokasi Pelanggan dan Penjual")
func.plot_customer_seller_map(all_data, geolocation_df)

# ⏳ 3. Kapan Pelanggan Biasanya Membeli?
st.header("Kapan Pelanggan Biasanya Melakukan Pembelian")
func.plot_purchase_distribution(all_data)

# 🚚 4. Apakah Biaya Pengiriman Meningkat Seiring Berat Produk?
st.header("Apakah Biaya Pengiriman Meningkat Seiring Berat Produk?")
func.plot_shipping_vs_weight(all_data)

# ⭐ 5. Tingkat Kepuasan Berdasarkan Metode Pembayaran
st.header("Tingkat Kepuasan Berdasarkan Metode Pembayaran")
func.plot_review_vs_payment(all_data)

#6. Menampilkan visualisasi: Distribusi Pelanggan Berdasarkan Waktu Pengiriman
st.subheader("Distribusi Pelanggan Berdasarkan Waktu Pengiriman")
func.plot_customer_count_by_shipping_time(all_data)

# 🗑️ Bersihkan Memori
func.clear_memory()