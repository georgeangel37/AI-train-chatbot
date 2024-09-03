import tkinter as tk

root = tk.Tk()

root.title("Chat Bot")


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
    OutputWindow.configure(state="normal")

    send = "You -> " + InputWindow.get()
    OutputWindow.insert(tk.END, send + "\n")
 
    user = InputWindow.get().lower()
    OutputWindow.insert(tk.END, "Bot -> " + user + "\n")

    InputWindow.delete(0, tk.END)
    OutputWindow.configure(state="disabled")

lable1 = tk.Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

OutputWindow = tk.Text(root, bd=1, fg=TEXT_COLOR, bg=BG_COLOR, width = 50, height = 8)
OutputWindow.grid(row=1, column=0, columnspan=2)
OutputWindow.configure(state="disabled")

scrollbar = tk.Scrollbar(OutputWindow)
scrollbar.place(relheight=1, relx=0.974)

InputWindow = tk.Entry(root, bg=BG_GRAY, fg=TEXT_COLOR, width=55)
InputWindow.grid(row=2, column=0)

send = tk.Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)

root.mainloop()