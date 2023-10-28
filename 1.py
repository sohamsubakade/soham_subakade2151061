class Customer:
    def __init__(self, name):
        self.name = name
        self.purchases = []

    def make_purchase(self, item, price):
        self.purchases.append((item, price))


class InventoryManagementSystem:
    def __init__(self):
        self.customers = {}
        self.sales = []

    def record_sale(self, customer_name, item, price):
        if customer_name not in self.customers:
            self.customers[customer_name] = Customer(customer_name)
        self.customers[customer_name].make_purchase(item, price)
        self.sales.append((customer_name, item, price))

    def calculate_total_sales(self, period_start, period_end):
        total_sales = 0
        for sale in self.sales:
            if period_start <= sale[0] <= period_end:
                total_sales += sale[2]
        return total_sales

    def generate_report(self):
        print("Sales Report:")
        for customer_name, customer in self.customers.items():
            total_spent = sum([purchase[1] for purchase in customer.purchases])
            print(f"Customer: {customer_name}, Total Spent: ${total_spent}")

    def top_customers(self, n):
        sorted_customers = sorted(self.customers.values(), key=lambda x: sum([p[1] for p in x.purchases]), reverse=True)
        top_n_customers = sorted_customers[:n]
        print(f"Top {n} Customers:")
        for customer in top_n_customers:
            total_spent = sum([purchase[1] for purchase in customer.purchases])
            print(f"Customer: {customer.name}, Total Spent: ${total_spent}")


if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.record_sale("Aakash", "pc", 1000)
    ims.record_sale("soham", "mouse", 200)
    ims.record_sale("Aakash", "iphone 14", 1499)
    ims.record_sale("manas", "pc", 500)
    ims.record_sale("soham", "airpod", 750)

    print("Total Sales in Period: $", ims.calculate_total_sales("Aakash", "soham"))
    ims.generate_report()
    ims.top_customers(2)
