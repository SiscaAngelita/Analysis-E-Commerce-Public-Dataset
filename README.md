# E-Commerce Public Data Analysis  

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Data Sources](#data-sources)
4. [Data Description](#data-description)
5. [Installation & Usage](#Installation-&-Usage)

## Overview
Proyek ini merupakan analisis kumpulan data e-commerce publik untuk mengidentifikasi tren perilaku pelanggan, popularitas produk, dan kinerja penjualan. Tujuannya adalah untuk memberikan wawasan yang dapat membantu bisnis e-commerce meningkatkan strategi pemasaran dan keputusan operasional mereka.

## Project Structure
- **`dashboard/`**: Folder ini berisi skrip Python yang digunakan untuk melakukan analisis dan pemrosesan data.
  - **`func.py`**: Skrip yang berisi fungsi-fungsi untuk analisis atau pemrosesan data tertentu.
  - **`main.py`**: Skrip utama yang menjalankan analisis berdasarkan fungsi yang ada di `func.py`.
  - **`requirements.txt`**: File yang berisi daftar dependensi Python yang dibutuhkan untuk menjalankan proyek ini.

- **`data/`**: Folder yang berisi dataset yang digunakan dalam proyek.
  - **`all_data.csv`**: Dataset utama yang berisi informasi tentang pelanggan, pesanan, produk, dll.
  - **`geolocation_df.csv`**: Dataset tambahan yang berisi informasi geolokasi pelanggan.

- **`Proyek_Analisis_Data.ipynb`**: File Jupyter Notebook yang digunakan untuk eksplorasi dan analisis data secara interaktif.

- **`README.md`**: File ini, yang menjelaskan tujuan dan struktur proyek serta cara penggunaan.

## Data Sources
Dataset yang digunakan dalam proyek ini berasal dari Proyek Analisis Data pada kursus Belajar Analisis Data dengan Python yang diselenggarakan oleh Decoding

## Data Description

Proyek ini menggunakan dua dataset utama, yaitu:

### 1. all_data: Dataset utama yang berisi informasi transaksi e-commerce.

| Kolom                        | Deskripsi                                                                                   |
|------------------------------|---------------------------------------------------------------------------------------------|
| customer_id                  | ID unik untuk setiap pelanggan.                                                              |
| customer_unique_id           | ID unik pelanggan yang bisa digunakan untuk mengidentifikasi pelanggan secara lebih akurat. |
| customer_zip_code_prefix     | Kode pos pelanggan yang menunjukkan lokasi pengiriman.                                       |
| customer_city                | Kota tempat pelanggan berada.                                                                |
| customer_state               | Provinsi tempat pelanggan berada.                                                            |
| order_id                     | ID unik untuk setiap pesanan.                                                                |
| order_status                 | Status pesanan (misalnya: 'delivered', 'canceled').                                          |
| order_purchase_timestamp     | Waktu pembelian pesanan.                                                                     |
| order_approved_at            | Waktu persetujuan pesanan.                                                                  |
| order_delivered_carrier_date | Tanggal pengiriman oleh kurir.                                                              |
| order_delivered_customer_date| Tanggal diterimanya pesanan oleh pelanggan.                                                  |
| order_estimated_delivery_date| Tanggal estimasi pengiriman.                                                                |
| order_item_id                | ID unik untuk setiap item dalam pesanan.                                                    |
| product_id                   | ID unik produk.                                                                               |
| seller_id                    | ID penjual produk.                                                                           |
| shipping_limit_date          | Tanggal batas pengiriman.                                                                   |
| price                        | Harga per unit produk.                                                                       |
| freight_value                | Biaya pengiriman untuk pesanan.                                                             |
| product_category_name        | Kategori produk (misalnya: elektronik, pakaian).                                              |
| product_name_length          | Panjang nama produk.                                                                         |
| product_description_length  | Panjang deskripsi produk.                                                                    |
| product_photos_qty           | Jumlah foto produk yang tersedia.                                                           |
| product_weight_g             | Berat produk dalam gram.                                                                     |
| product_length_cm            | Panjang produk dalam sentimeter.                                                            |
| product_height_cm            | Tinggi produk dalam sentimeter.                                                             |
| product_width_cm             | Lebar produk dalam sentimeter.                                                              |
| review_id                    | ID ulasan produk.                                                                             |
| review_score                 | Skor ulasan produk.                                                                          |
| review_comment_title         | Judul ulasan produk.                                                                         |
| review_comment_message       | Isi ulasan produk.                                                                           |
| review_creation_date         | Tanggal pembuatan ulasan.                                                                    |
| review_answer_timestamp      | Tanggal jawaban atas ulasan.                                                                |

### 2. geolocation_df: Dataset yang berisi informasi lokasi geografis.

| Kolom                         | Deskripsi                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------|
| geolocation_zip_code_prefix   | Kode pos lokasi geografis.                                                                  |
| geolocation_lat                | Latitude (garis lintang) dari lokasi geografis.                                             |
| geolocation_lng                | Longitude (garis bujur) dari lokasi geografis.                                              |
| geolocation_city               | Kota dari lokasi geografis.                                                                  |
| geolocation_state              | Provinsi dari lokasi geografis.                                                              |

Data ini memberikan gambaran lengkap tentang pesanan, produk, pelanggan, serta lokasi geografis yang dapat digunakan untuk analisis perilaku pelanggan dan kinerja pengiriman dalam e-commerce.

## Installation & Usage
### 1. Clone repository ke komputer lokal anda menggunakan perintah berikut:
```bash
git clone https://github.com/SiscaAngelita/Analysis-E-Commerce-Public-Dataset.git

### 2. Masuk ke Direktori Proyek
Masuk ke direktori proyek yang telah Anda clone:
cd Analysis-E-Commerce-Public-Dataset

### 3. Instal Dependensi
Instal semua dependensi yang diperlukan dengan menjalankan perintah berikut:
pip install -r requirements.txt

### 4. Instal Streamlit
Jika Streamlit belum terinstal dalam proyek Anda, jalankan perintah berikut untuk menginstalnya:
pip install streamlit

### 5. Menjalankan aplikasi dengan Streamlit
Anda dapat menjalankan aplikasi analisis menggunakan Streamlit. Gunakan perintah berikut untuk menjalankan aplikasi:
streamlit run dashboard/main.py

### 6. Menjalankan Jupyter Notebook
Jika Anda ingin mengeksplorasi data menggunakan Jupyter Notebook, jalankan perintah berikut untuk membuka notebook:
jupyter notebook Proyek_Analisis_Data.ipynb

Atau anda dapat mengunjungi aplikasi streamlit saya dengan [klik di sini](https://analysis-e-commerce-public-dataset-pef9ip8c8ourhgtsccf9dj.streamlit.app/)
