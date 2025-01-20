import tkinter as tk

# Funktion, um die Eingabe zu aktualisieren
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Funktion, um die Berechnung zu machen
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Fehler")

# Funktion, um die Eingabe zu löschen
def clear():
    entry.delete(0, tk.END)

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Windows 11 Rechner")
root.geometry("400x500")  # Fenstergröße anpassen
root.config(bg="#1E1E1E")

# Eingabefeld für Zahlen und Ergebnisse
entry = tk.Entry(root, width=15, font=("Segoe UI", 24), borderwidth=0, relief="solid", justify="right", bd=10, bg="#2D2D2D", fg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Erstellen der Tasten für den Rechner
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Funktion, um die Buttons zu erstellen
def create_button(text, row, col, command=None, bg="#3C3C3C", fg="#FFFFFF"):
    return tk.Button(root, text=text, width=5, height=2, font=("Segoe UI", 18), command=command, bg=bg, fg=fg, bd=0, relief="flat", activebackground="#565656")

# Hinzufügen der Tasten ins Fenster
for (text, row, col) in buttons:
    button = create_button(text, row, col, lambda t=text: button_click(t) if t != "=" else calculate())
    button.grid(row=row, column=col, padx=5, pady=5)

# Eine zusätzliche Taste zum Löschen der Eingabe
clear_button = create_button("C", 4, 0, command=clear, bg="#FF5C5C", fg="#FFFFFF")
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Starten der Tkinter GUI-Schleife
root.mainloop()
