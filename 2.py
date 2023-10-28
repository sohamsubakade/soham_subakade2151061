import tkinter as tk

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Store")
        
        self.products = [
            Product("mac mini", 1899),
            Product("macbook", 2899),
            Product("Iphone 14", 1599),
            Product("Airpods", 799),
            Product("ipad", 1599),
            Product("Apple TV", 2899),
            Product("Airtag", 399),
            Product("macos", 1299),
            Product("Apple Watch", 999),
            Product("ipod", 299),
            Product("Iphone 15pro max", 1699),
            Product("Iphone 13pro ", 1499),
            Product("Home pod ", 899),
            
        ]
        
        self.cart = []

        self.create_ui()
    
    def create_ui(self):
        
        self.search_label = tk.Label(self.root, text="Search for a product:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        self.search_button = tk.Button(self.root, text="Search", command=self.search_product)
        self.search_button.pack()

        
        self.product_listbox = tk.Listbox(self.root, width=30, height=10)
        self.product_listbox.pack()
        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product.name} - ${product.price:.2f}")

        
        self.cart_label = tk.Label(self.root, text="Shopping Cart:")
        self.cart_label.pack()
        self.cart_listbox = tk.Listbox(self.root, width=30, height=5)
        self.cart_listbox.pack()

       
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()
        self.calculate_total_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_total_button.pack()
        self.place_order_button = tk.Button(self.root, text="Place Order", command=self.place_order)
        self.place_order_button.pack()

    def search_product(self):
        query = self.search_entry.get()
        self.product_listbox.delete(0, tk.END)
        for product in self.products:
            if query.lower() in product.name.lower():
                self.product_listbox.insert(tk.END, f"{product.name} - ${product.price:.2f}")

    def add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            product_index = selected_index[0]
            product = self.products[product_index]
            self.cart.append(product)
            self.cart_listbox.insert(tk.END, f"{product.name} - ${product.price:.2f}")

    def calculate_total(self):
        total = sum(product.price for product in self.cart)
        self.cart_listbox.insert(tk.END, f"Total: ${total:.2f}")

    def place_order(self):
        self.cart_listbox.insert(tk.END, "Order placed. Thank you!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
