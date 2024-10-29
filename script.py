# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
data = pd.read_csv('retail-trade-survey-june-2024-quarter.csv')

# %%
data.head()

# %%
print("Original 'Period' values:\n", data[['Period']].head(10))


# %%
print("Data type of 'Period':", data['Period'].dtype)

# %%
data['Period'] = data['Period'].astype(str).str.strip()

# %%
data['Period'] = pd.to_datetime(data['Period'], format='%Y.%m', errors='coerce')

# %%
print("Rows with NaT in 'Period' after conversion:\n", data[data['Period'].isna()])

# %%
data['Data_value'] = pd.to_numeric(data['Data_value'], errors='coerce')

max_value_row = data.loc[data['Data_value'].idxmax()]

highest_value = max_value_row['Data_value']
highest_value_period = max_value_row['Period']
highest_value_subject = max_value_row['Subject']

print(f"Higher Data Value: {highest_value}")
print(f"Period: {highest_value_period}")
print(f"Subject: {highest_value_subject}")

# %%
data['Year'] = data['Period'].dt.year  

annual_sales = data.groupby('Year')['Data_value'].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(annual_sales['Year'], annual_sales['Data_value'], color='blue')
plt.title('Total Penjualan per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Total Penjualan (Dollars)')
plt.xticks(rotation=45)  
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.tight_layout()
plt.show()


# %%
plt.figure(figsize=(10, 5))
plt.plot(annual_sales['Year'], annual_sales['Data_value'], marker='o', color='blue', label='Total Sales')
plt.title('Tren Penjualan Tahunan')
plt.xlabel('Tahun')
plt.ylabel('Total Penjualan (Dollars)')
plt.xticks(rotation=45) 
plt.grid(True)  
plt.legend()
plt.tight_layout()
plt.show()


# %%
plt.figure(figsize=(12, 6))  
plt.hist(data['Data_value'].dropna(), bins=30, color='orange', edgecolor='black')
plt.title('Distribusi Nilai Penjualan')
plt.xlabel('Nilai Penjualan (Dollars)')
plt.ylabel('Frekuensi')
plt.grid(axis='y')  
plt.show()


# %%
plt.figure(figsize=(20, 10))
plt.scatter(data['Period'], data['Data_value'], color='red')
plt.title('Scatter Plot: Periode vs. Nilai Penjualan')
plt.xlabel('Periode')
plt.ylabel('Nilai Penjualan (Dollars)')
plt.show()

# %%
subject_sales = data.groupby('Subject')['Data_value'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(subject_sales['Data_value'], labels=subject_sales['Subject'], autopct='%1.1f%%')
plt.title('Proporsi Penjualan Berdasarkan Subjek')
plt.show()


