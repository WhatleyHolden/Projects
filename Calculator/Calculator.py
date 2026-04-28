import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Calculator")
        self.iconbitmap('calc.ico')
        self.resizable(False, False)

        # HEX Colors
        button_color = "#4C72B0"     # blue
        operator_color = "#DD8452"   # orange
        clear_color = "#55A868"      # green
        delete_color = "#C44E52"     # red
        entry_color = "#F7F7F7"      # light gray

        # Input field
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(
            self,
            textvariable=self.input_text,
            justify='right',
            font=("Arial", 12, "bold"),
            bg=entry_color,
            width=25
        )
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'C', 'DEL'
        ]

        row = 1
        col = 0

        for button in buttons:
            command = lambda x=button: self.button_click(x)

            # Color selection
            if button in ['+', '-', '*', '/', '=']:
                bg_color = operator_color
            elif button == 'C':
                bg_color = clear_color
            elif button == 'DEL':
                bg_color = delete_color
            else:
                bg_color = button_color

            tk.Button(
                self,
                text=button,
                width=6,
                height=2,
                bg=bg_color,
                fg="white",
                command=command
            ).grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Keyboard
        self.bind('<Key>', self.keyboard_input)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.input_text.get())
                self.input_text.set(result)
            except:
                self.input_text.set("ERROR")

        elif value == 'C':
            self.input_text.set("")

        elif value == 'DEL':
            current = self.input_text.get()
            self.input_text.set(current[:-1])

        else:
            current = self.input_text.get()
            self.input_text.set(current + value)

    def keyboard_input(self, event):
        if event.char in '0123456789+-*/.()':
            self.button_click(event.char)
        elif event.keysym == 'Return':
            self.button_click('=')
        elif event.keysym == 'BackSpace':
            self.button_click('DEL')
        elif event.char.lower() == 'c':
            self.button_click('C')

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()