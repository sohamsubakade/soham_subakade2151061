import pandas as pd
import matplotlib.pyplot as plt


sales_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Sales': [100, 150, 200, 120],
    'Product': ['Iphone14', 'Macbook air', 'iphone14', 'Airpods'],
    'Hour': [10, 12, 14, 16],
}


df = pd.DataFrame(sales_data)


df['Date'] = pd.to_datetime(df['Date'])  
df.set_index('Date', inplace=True) 
monthly_sales = df['Sales'].resample('M').sum()


plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(df.index, df['Sales'], marker='o', linestyle='-')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)

plt.subplot(2, 2, 2)
product_sales = df.groupby('Product')['Sales'].sum()
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.subplot(2, 2, 3)
hourly_sales = df.groupby('Hour')['Sales'].sum()
hourly_sales.plot(kind='bar')
plt.title("Peak Sales Hours")
plt.xlabel("Hour")
plt.ylabel("Sales")

plt.subplot(2, 2, 4)
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()

