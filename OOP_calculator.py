import tkinter as tk
import math

class CalculatorGUI:
    """
    Calculator ka GUI (Graphical User Interface) class.
    Yeh class design aur buttons ke events ko manage karti hai.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Simple OOP Calculator")
        self.root.geometry("350x500")      # Window ka size set kiya
        self.root.configure(bg="#17171C")  # Dark theme background color
        
        # Display par text show karne ke liye StringVar use kiya
        self.display_var = tk.StringVar(value="0")
        
        # Grid structure aur buttons banane ke functions call kiye
        self.create_widgets()
        self.setup_bindings()
        
    def create_widgets(self):
        # 1. Display Screen (Jahan numbers aur result nazar aayenge)
        display = tk.Label(
            self.root, 
            textvariable=self.display_var, 
            font=("Segoe UI", 28, "bold"),
            fg="#FFFFFF", 
            bg="#0D0D0E", 
            anchor="e",  # Text ko right side alignment dega
            padx=20, 
            pady=25
        )
        display.pack(fill=tk.BOTH, expand=False)
        
        # 2. Buttons Frame (Grid layout ke liye)
        frame = tk.Frame(self.root, bg="#17171C")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Grid columns (4 columns) aur rows (6 rows) ko responsive banaya
        for i in range(4):
            frame.columnconfigure(i, weight=1)
        for i in range(6):
            frame.rowconfigure(i, weight=1)
            
        # Calculator buttons layout: (text, row, column, columnspan)
        buttons_layout = [
            # Row 0 (C aur Backspace ab 2-2 columns cover karenge)
            ("C", 0, 0, 2), ("⌫", 0, 2, 2),
            # Row 1
            ("x²", 1, 0, 1), ("x³", 1, 1, 1), ("√x", 1, 2, 1), ("÷", 1, 3, 1),
            # Row 2
            ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("×", 2, 3, 1),
            # Row 3
            ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("-", 3, 3, 1),
            # Row 4
            ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("+", 4, 3, 1),
            # Row 5
            ("0", 5, 0, 2), (".", 5, 2, 1), ("=", 5, 3, 1)
        ]
        
        # Buttons create karne ka loop
        for text, r, c, span in buttons_layout:
            # Har button type ke hisab se colors set kiye
            if text in ("+", "-", "×", "÷", "="):
                bg, hvr = "#8B5CF6", "#A78BFA"  # Operator keys (Purple color)
            elif text in ("C", "⌫", "x²", "x³", "√x"):
                bg, hvr = "#4E505F", "#5E6173"  # Utility keys (Slate grey)
            else:
                bg, hvr = "#2E2F38", "#3E3F48"  # Number keys (Dark grey)
                
            # Button element banaya
            btn = tk.Button(
                frame, 
                text=text, 
                bg=bg, 
                fg="#FFFFFF", 
                relief="flat", 
                bd=0,
                font=("Segoe UI", 14, "bold" if text.isalpha() or len(text) > 1 else "normal"),
                command=lambda t=text: self.click_button(t)
            )
            # Button ko grid mein place kiya
            btn.grid(row=r, column=c, columnspan=span, sticky="nsew", padx=1, pady=1)
            
            # Hover effect lagaya (Mouse enter aur leave par color change hoga)
            btn.bind("<Enter>", lambda e, b=btn, h=hvr: b.config(bg=h))
            btn.bind("<Leave>", lambda e, b=btn, n=bg: b.config(bg=n))

    def click_button(self, text):
        """Jab koi button click hoga, yeh function chalega."""
        current = self.display_var.get()
        
        # Agar screen par pehle se koi error show ho rha ho, to reset kar do
        if current in ("Error", "Cannot divide by zero", "Invalid Input"):
            current = "0"
            
        # Math Ke Single-Number operations map (Optimization using lambdas)
        unary_ops = {
            "x²": lambda v: v ** 2,
            "x³": lambda v: v ** 3,
            "√x": lambda v: math.sqrt(v)
        }
            
        if text == "C":
            # Screen ko clear karke '0' set karega
            self.display_var.set("0")
            
        elif text == "⌫":
            # Backspace: Aakhri character ko delete karega
            self.display_var.set(current[:-1] if len(current) > 1 else "0")
                
        elif text == "=":
            # Expression ko evaluate (solve) karega
            try:
                # User-friendly symbols ko standard arithmetic operators se badla
                expression = current.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                self.display_var.set(self.format_res(result))
            except ZeroDivisionError:
                self.display_var.set("Cannot divide by zero")
            except Exception:
                self.display_var.set("Error")
                
        elif text in unary_ops:
            # Square, Cube, aur Square Root ka ek hi optimized block
            try:
                val = float(current)
                if text == "√x" and val < 0:
                    self.display_var.set("Invalid Input")
                else:
                    self.display_var.set(self.format_res(unary_ops[text](val)))
            except Exception:
                self.display_var.set("Error")
                
        else:
            # Numbers aur basic operations ko screen par append karna
            if current == "0" and text not in ("+", "-", "×", "÷", "."):
                self.display_var.set(text)
            else:
                self.display_var.set(current + text)

    def format_res(self, val):
        """Result ko clean format karne ka optimized function."""
        # Built-in format strings automatic precision control aur scientific notation handle karti hain
        try:
            return f"{float(val):.10g}"
        except (ValueError, TypeError):
            return str(val)

    def setup_bindings(self):
        """Keyboard keys ko calculator ke functions se bind karne ke liye."""
        self.root.bind("<Key>", self.handle_key)
        
    def handle_key(self, event):
        key = event.char
        keysym = event.keysym
        
        if key in "0123456789.+-":
            self.click_button(key)
        elif key == "*":
            self.click_button("×")
        elif key == "/":
            self.click_button("÷")
        elif keysym in ("Return", "KP_Enter") or key == "=":
            self.click_button("=")
        elif keysym == "BackSpace":
            self.click_button("⌫")
        elif keysym == "Escape":
            self.click_button("C")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    # Window ko screen ke center mein open karne ke liye
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
