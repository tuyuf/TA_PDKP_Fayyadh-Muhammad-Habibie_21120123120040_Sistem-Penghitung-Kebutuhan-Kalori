from tkinter import ttk

def apply_styles(app):
    style = ttk.Style()
    
    # Button style
    style.configure('TButton', font=('Arial', 10, 'bold'), background='#1e1e1e', foreground='Black', padding=5)
    style.map('TButton', background=[('active', '#1e1e1e')])

    # Frame style
    style.configure('MainFrame.TFrame', background='#1e1e1e')

    # Label style
    style.configure('TLabel', background='#1e1e1e')

    # Radiobutton style
    style.configure('TRadiobutton', background='#1e1e1e', foreground='White')
