# Currency Converter using Tkinter and API
import tkinter as tk
from tkinter import ttk
import requests

# Available currencies
currencies = ["USD", "AUD", "NPR", "BDT", "INR", "PKR", "EUR", "CNY", "JPY", "CAD"]

# Setting up the main GUI window
root = tk.Tk()
root.title("Currency Converter")

# GUI widgets
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

tk.Label(root, text="Base Currency:").grid(row=1, column=0)
from_currency = ttk.Combobox(root, values=currencies)
from_currency.grid(row=1,column=1)
from_currency.set("USD")

tk.Label(root, text="Target Currency:").grid(row=2, column=0)
to_currency = ttk.Combobox(root, values=currencies)
to_currency.grid(row=2,column=1)
to_currency.set("NPR")

result_label = tk.Label(root, text="Enter details and click Convert.")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform conversion
def convert():
    try:
        amount = float(entry_amount.get())  # Convert input to float
        base_cur = from_currency.get()
        to_cur = to_currency.get()
        
        # API call to get exchange rate
        url = f"https://api.exchangerate-api.com/v4/latest/{base_cur}"
        response = requests.get(url)
        data = response.json()
        
        rate = data['rates'].get(to_cur)
        converted_amount = amount * rate

        # Showing the result
        message = f"{amount} {base_cur} = {converted_amount:.2f} {to_cur}"
        result_label.config(text= message)
    except ValueError:
        result_label.config(text="Invalid Input, Please enter a valid number.")

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Start GUI loop
root.mainloop()
