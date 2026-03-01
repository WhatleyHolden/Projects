import tkinter as tk
from PIL import Image, ImageTk


class FoodViewer:

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Food Viewer")
        self.main_window.minsize(400, 300)
        self.main_window.resizable(False, False)

        self.top_frame = tk.Frame(self.main_window, width=400, height=320)
        self.bottom_frame = tk.Frame(self.main_window)

        self.top_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)

        self.var = tk.IntVar()
        self.var.set(1)

        self.imgChicken = ImageTk.PhotoImage(
            Image.open("chicken.jpg").resize((400, 300))
        )
        self.imgPie = ImageTk.PhotoImage(
            Image.open("pie.jpg").resize((400, 300))
        )
        self.imgPizza = ImageTk.PhotoImage(
            Image.open("pizza.jpg").resize((350, 300))
        )
        self.imgSteak = ImageTk.PhotoImage(
            Image.open("steak.jpg").resize((300, 300))
        )

        self.image_label = tk.Label(self.top_frame)
        self.image_label.pack()

        for text, value in [("Chicken", 1), ("Pie", 2), ("Pizza", 3), ("Steak", 4)]:
            tk.Radiobutton(
                self.bottom_frame,
                text=text,
                variable=self.var,
                value=value,
                command=self.on_radio_select
            ).pack(side="left", padx=10)

        self.on_radio_select()

        tk.mainloop()

    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.image_label.config(image=self.imgChicken)
        elif choice == 2:
            self.image_label.config(image=self.imgPie)
        elif choice == 3:
            self.image_label.config(image=self.imgPizza)
        elif choice == 4:
            self.image_label.config(image=self.imgSteak)


if __name__ == "__main__":
    FoodViewer()