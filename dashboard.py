# Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
data = pd.read_csv("semua_dataframe.csv")

# Title
st.title("E-Commerce Dashboard")

# Display the entire DataFrame
st.subheader("Raw Data")
st.write(data)

# Sidebar with filtering options
st.sidebar.header("Filter Options")

# Add components to sidebar
selected_city = st.sidebar.selectbox('Select City', data['customer_city'].unique())
selected_product = st.sidebar.selectbox('Select Product', data['product_id'].unique())

# Filter Data based on Sidebar Selection
filtered_data = data[(data['customer_city'] == selected_city) & (data['product_id'] == selected_product)]

# Display Filtered Data
st.subheader(f"Showing data for {selected_city} and product {selected_product}")
st.write(filtered_data)

# Visualizations
# Visualisasi 1: Jumlah pelanggan di setiap kota atau negara bagian
customer_count_by_city = data['customer_city'].value_counts()
st.subheader('Number of Customers in Each City')
fig_customer_count = px.bar(customer_count_by_city, x=customer_count_by_city.index, y=customer_count_by_city.values, labels={'x': 'City', 'y': 'Number of Customers'})
st.plotly_chart(fig_customer_count)

# Visualisasi 2: Produk dengan penjualan tertinggi
product_sales = data.groupby('product_id')['price'].sum().sort_values(ascending=False).head(10)
st.subheader('Top 10 Products with Highest Sales')
fig_product_sales = px.bar(product_sales, x=product_sales.index, y=product_sales.values, labels={'x': 'Product ID', 'y': 'Total Sales'})
st.plotly_chart(fig_product_sales)

# Visualisasi 3: Rata-rata keterlambatan pengiriman
data['order_delivered_customer_date'] = pd.to_datetime(data['order_delivered_customer_date'])
data['order_estimated_delivery_date'] = pd.to_datetime(data['order_estimated_delivery_date'])
data['delivery_delay'] = (data['order_delivered_customer_date'] - data['order_estimated_delivery_date']).dt.days
average_delivery_delay = data.groupby('customer_city')['delivery_delay'].mean()
st.subheader('Average Delivery Delay by City')
fig_delivery_delay = px.bar(average_delivery_delay, x=average_delivery_delay.index, y=average_delivery_delay.values, labels={'x': 'City', 'y': 'Average Delivery Delay'})
st.plotly_chart(fig_delivery_delay)

# Visualisasi 4: Distribusi skor ulasan pelanggan
st.subheader('Distribution of Customer Review Scores')
fig_review_score = px.histogram(data, x='review_score', nbins=5, labels={'x': 'Review Score', 'y': 'Count'})
st.plotly_chart(fig_review_score)

# Visualisasi 5: Jumlah penjual di setiap kota atau negara bagian
seller_count_by_city = data['seller_city'].value_counts()
st.subheader('Number of Sellers in Each City')
fig_seller_count = px.bar(seller_count_by_city, x=seller_count_by_city.index, y=seller_count_by_city.values, labels={'x': 'City', 'y': 'Number of Sellers'})
st.plotly_chart(fig_seller_count)

# Visualisasi 6: Heatmap korelasi antara lokasi pelanggan dan produk yang dibeli
correlation_columns = ['customer_zip_code_prefix', 'product_weight_g', 'product_description_lenght']
correlation_matrix = data[correlation_columns].corr()

st.subheader('Correlation Heatmap: Customer Location vs. Product Attributes')
fig_correlation_heatmap = px.imshow(correlation_matrix)
st.plotly_chart(fig_correlation_heatmap)

# Visualisasi 7: Distribusi metode pembayaran
payment_method_distribution = data['payment_type'].value_counts()
st.subheader('Distribution of Payment Methods')
fig_payment_method_distribution = px.pie(payment_method_distribution, values=payment_method_distribution.values, names=payment_method_distribution.index, labels={'names': 'Payment Method'})
st.plotly_chart(fig_payment_method_distribution)
