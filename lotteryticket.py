import tkinter as tk
import random

#--- Lottery Logic ---

def generate_winning_ticket():
    pool = list(range(1, 50)) # numbers 1-49
    winning = tuple(sorted (random.sample(pool, 6)))
    return winning

def buy_lottery_ticket():
    pool = list(range(1, 50))
    ticket = tuple(sorted(random.sample(pool, 6))) 
    return ticket

def check_ticket(ticket, winning):
    ticket_nums = set(ticket) 
    winning_nums = set(winning)
    matched = ticket_nums.intersection(winning_nums) 
    return matched

# --- Tkinter GUI ---

def on_generate():
    global winning_ticket
    winning_ticket = generate_winning_ticket()
    winning_label.config(text=f"Winning Ticket: {winning_ticket}")

def on_buy():
    global player_ticket
    player_ticket = buy_lottery_ticket()
    ticket_label.config(text=f"Your Ticket: {player_ticket}")

def on_check():
    if not winning_ticket:
      result_label.config(text="Generate winning ticket first!")
      return

    if not player_ticket:
      result_label.config(text="Buy your ticket first!")
      return
    matched = check_ticket(player_ticket, winning_ticket) 
    result_label.config(
      text=f"Matched {len(matched)} numbers: {tuple(sorted(matched))}"  
    )
# --- Main Window ---

root = tk.Tk()
root.title("Lottery Ticket Generator")
root.geometry("400x300")

winning_ticket = None 
player_ticket = None

#  Buttons
btn_generate = tk.Button(root, text="Generate Winning Ticket", command=on_generate) 
btn_generate.pack(pady=10)

btn_buy = tk.Button(root, text="Buy Lottery Ticket", command=on_buy) 
btn_buy.pack(pady=10)

btn_check = tk.Button(root, text="Check Result", command=on_check) 
btn_check.pack (pady=10)

# Labels
winning_label = tk.Label(root, text="Winning Ticket: None", font=("Arial", 12))
winning_label.pack (pady=10)

ticket_label = tk.Label(root, text="Your Ticket: None",  font=("Arial", 12)) 
ticket_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue") 
result_label.pack(pady=20)

root.mainloop()