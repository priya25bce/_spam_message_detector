# gui.py
#importing libraries

import tkinter as tk
import joblib



# Loading  model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")



# Function to check spam
def check_spam():
    msg = entry.get()
    
    if msg.strip() == "":
        out_label.config(text="Please enter the message", fg="orange")
        return

    vec = vectorizer.transform([msg])
    result = model.predict(vec)[0]

    if result == 1:
        out_label.config(text="Spam , do not believe as it is very risky.", fg="red")
    else:
        out_label.config(text="Not Spam  ,please move forward.", fg="green")



# Creating the  window
root = tk.Tk()
root.title("Spam Detector Message")
root.geometry("450x300")

# Title of the window
title = tk.Label(root, text="Spam Message Detector", font=("Arial", 16, "bold"))
title.pack(pady=10)


# Input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)



# making buttons 
buton = tk.Button(root, text="Check", command=check_spam)
buton.pack(pady=10)


# Output label
out_label = tk.Label(root, text="", font=("Arial", 14))
out_label.pack(pady=10)


# Running  GUI
root.mainloop()

# end of the GUI window 
