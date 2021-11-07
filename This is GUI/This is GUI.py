# ①画面を作成
import tkinter as tk
from tkinter import Button, Label

root = tk.Tk()
root.title("Tkinter")
root.geometry("600x400")


# ②クリック時の処理を作成
def clickmessage():
    lblmessage["text"] = textBox.get()


# ③画面の項目をそれぞれ作成
textBox = tk.Entry(root, width="25")
textBox.place(x=220, y=80)

Btnmessagedisp: Button = tk.Button(root, text="押してみろよ！！", width="20", command=clickmessage)
Btnmessagedisp.place(x=220, y=160)

lblmessage: Label = tk.Label(root, text="")
lblmessage.place(x=220, y=240)

root.mainloop()
