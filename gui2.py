import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class FoodEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Entry Form")

        #Create a label and entry for date and time
        self.date_label = ttk.Label(root, text="Date:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry = ttk.Entry(root, width=25)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%H:%M"))

        self.date_label = ttk.Label(root, text="Time:")
        self.date_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry = ttk.Entry(root, width=25)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%H:%M"))
        

        # Create a label and entry for food
        self.food_label = ttk.Label(root, text="Food:")
        self.food_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.food_entry = ttk.Entry(root, width=25)
        self.food_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create a label and entries for ingredients
        self.ingredients_label = ttk.Label(root, text="Ingredients:")
        self.ingredients_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.ingredients_entries = []
        self.add_ingredient_entry()
        self.add_button = ttk.Button(root, text="Add Ingredient", command=self.add_ingredient_entry)
        self.add_button.grid(row=3, column=2, padx=5, pady=5)
        self.remove_button = ttk.Button(root, text="Remove Ingredient", command=self.remove_ingredient_entry)
        self.remove_button.grid(row=3, column=3, padx=5, pady=5)

        # Create a submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, column=1, padx=5, pady=5)

    def add_ingredient_entry(self):
        ingredient_entry = ttk.Entry(self.root, width=25)
        ingredient_entry.grid(row=len(self.ingredients_entries) + 3, column=1, padx=5, pady=5)
        self.ingredients_entries.append(ingredient_entry)

    def remove_ingredient_entry(self):
        if len(self.ingredients_entries) > 0:
            entry_to_remove = self.ingredients_entries.pop()
            entry_to_remove.destroy()

    def submit_form(self):
        date_time = self.date_time_entry.get()
        food = self.food_entry.get()
        ingredients = [entry.get() for entry in self.ingredients_entries]
        messagebox.showinfo("Form Data", f"Date and Time: {date_time}\nFood: {food}\nIngredients: {', '.join(ingredients)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodEntryForm(root)
    root.mainloop()