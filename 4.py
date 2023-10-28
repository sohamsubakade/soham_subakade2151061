import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Month': ['jun','jul', 'aug', 'sept', 'oct', ],
    'Sales': [100, 120, 130, 110, 150]
}


df = pd.DataFrame(data)


mean_sales = df['Sales'].mean()
total_sales = df['Sales'].sum()


plt.figure(figsize=(9, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')


plt.text(0.5, 165, f'Mean Sales: {mean_sales:.2f}', fontsize=13, color='red')

plt.text(0.5, 150, f'Total Sales: {total_sales}', fontsize=13, color='green')


plt.show()
