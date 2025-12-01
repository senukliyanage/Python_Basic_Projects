import tkinter as tk
from tkinter import messagebox, simpledialog

cart = []

def add_item():
    item = simpledialog.askstring("Add Item", "Enter item to add to cart: ")
    if item:
        cart.append(item)
        messagebox.showinfo("Added", f"{item} has been added to your cart.")
    else:
        messagebox.showwarning("Invalid", "Invalid item. Please try again.")

def view_cart():
    if cart:
        item = "\n".join(f"{i+1}. {item}" for i, item in enumerate(cart))
        messagebox.showinfo("Cart Items", f"Your cart:\n{item}")
    else:
        messagebox.showinfo("Cart Empty", "Your cart is Empty.")

def remove_item():
    if cart:
        items = "\n".join(f"{i+1}. {item}" for i, item in enumerate(cart))
        prompt_text = (
            f" 🛒 Items you can remove:\n(items_list)\n\n"
            "Enter exact item name to remove:"
        )
        item = simpledialog.askstring("Remove Item", prompt_text)

        if item in cart:
            cart.remove(item)
            messagebox.showinfo("Removed", f"{item} has been removed from your cart.")

        else:
            messagebox.showwarning("Warning", f"{item} not found in cart.")
            
    else:
        messagebox.showinfo("Cart Empty", "Your cart is empty. Nothing to remove.")

def checkout():
    if cart:
        items = "\n".join(f"{i+1}. {item}" for i, item in enumerate(cart))
        confirm = messagebox.showinfo("Checkout", f"Checkout Summary of items:\n{items}")
        if confirm:
            messagebox.showinfo("Thank You", "Thank you for your purchase!")
            root.destroy()

    else:
        messagebox.showinfo("Cart Empty", "Your cart is empty. Nothing to checkout.")

def exit_shop():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
            messagebox.showinfo("Thank You", "Thank you for visiting My Shop!")
            root.destroy()

# Main Window
root = tk.Tk()
root.title("Senuk's Shopping Menu System")
root.geometry("400x300")


# Heading
heading = tk.Label(root, text = "Shopping Menu", font=("Arial", 16, "bold"))
heading.pack(pady=10)


# Buttons
btn_add = tk.Button(root, text = "Add Item", width = 20, command = add_item)
btn_add.pack(pady=5)

btn_view = tk.Button(root, text = "View Cart", width = 20, command = view_cart)
btn_view.pack(pady = 5)

btn_remove = tk.Button(root, text = "Remove Item", width = 20, command = remove_item)
btn_remove.pack(pady = 5)

btn_checkout = tk.Button(root, text = "Checkout", width = 20, command = checkout)
btn_checkout.pack(pady = 5)

btn_exit = tk.Button(root, text = "Exit", width = 20, command = exit_shop)
btn_exit.pack(pady = 5)


root.mainloop()
