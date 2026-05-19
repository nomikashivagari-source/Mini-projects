import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    """Class to handle BMI calculation.""" 
    @staticmethod
    def calculate_bmi(weight, height):
        try:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
               return f"BMI: {bmi:.2f} (Underweight)" 
            elif 18.5 <= bmi < 24.9:
               return f"BMI: {bmi:.2f} (Normal weight)" 
            elif 25 <= bmi < 29.9:
               return f"BMI: {bmi:.2f} (Overweight)"
            else:
               return f"BMI: {bmi:.2f} (Obese)"
        except ZeroDivisionError:
               return "Height cannot be zero!"
class BMIApp:
     """class for the BMI Calculator GUI."""
     def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("300x300")


        tk.Label(root, text="weight (kg):", font=("Arial", 12)).pack(pady=10)
        
        
        self.weight_entry=tk.Entry(root, font=("Arial", 12)) 
        self.weight_entry.pack()

        tk.Label(root, text="Height (m):", font=("Arial", 12)).pack(pady=10) 
        
        self.height_entry= tk.Entry(root, font=("Arial", 12))
        self.height_entry.pack()
        
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi, font=("Arial", 12))
        self.calculate_button.pack(pady=20)

        
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

     def calculate_bmi(self):
        """Calculate and display BMI."""
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            result = BMICalculator.calculate_bmi(weight, height)
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()