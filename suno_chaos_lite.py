import random
import tkinter as tk
from tkinter import messagebox, filedialog

class PromptMakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Prompt Maker")
        self.root.geometry("900x900")

        # Listene dine – akkurat som du sendte
        self.themes = [ ... ]  # behold hele listen din her
        self.moods = [ ... ]
        self.instruments = [ ... ]
        self.effects = [ ... ]
        self.settings = [ ... ]
        self.bpms = list(range(40, 241, 4))

        self.selected_themes = []
        self.selected_moods = []
        self.selected_instruments = []
        self.selected_effects = []
        self.selected_settings = []

        # GUI – nøyaktig som du skrev, bare litt ryddigere plassering
        tk.Label(root, text="Advanced Music Prompt Generator", font=("Arial", 16, "bold")).pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Movement Name
        tk.Label(input_frame, text="Movement Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="e")
        self.movement_entry = tk.Entry(input_frame, width=30)
        self.movement_entry.grid(row=0, column=1, pady=5, columnspan=2)
        self.movement_entry.insert(0, "I. Dies Irae")

        # ——— Themes ———
        tk.Label(input_frame, text="Themes:", font=("Arial", 10)).grid(row=1, column=0, sticky="ne")
        theme_frame = tk.Frame(input_frame)
        theme_frame.grid(row=1, column=1, pady=5)
        self.theme_listbox = tk.Listbox(theme_frame, height=5, width=40, selectmode="multiple", exportselection=0)
        for t in self.themes: self.theme_listbox.insert(tk.END, t)
        self.theme_listbox.pack(side=tk.LEFT)
        tk.Scrollbar(theme_frame, command=self.theme_listbox.yview).pack(side=tk.RIGHT, fill=tk.Y)
        self.theme_listbox.config(yscrollcommand=tk.Scrollbar(theme_frame).set)
        tk.Button(input_frame, text="Add Themes", command=self.add_themes).grid(row=1, column=2, padx=5)
        self.theme_display = tk.Label(input_frame, text="Selected: None", fg="gray")
        self.theme_display.grid(row=1, column=3)

        # Gjør det samme for Moods, Instruments, Effects, Settings (kopier blokken over og bytt navn/variabler)

        # BPM
        tk.Label(input_frame, text="BPM (leave blank for random):", font=("Arial", 10)).grid(row=6, column=0, sticky="e")
        self.bpm_entry = tk.Entry(input_frame, width=10)
        self.bpm_entry.grid(row=6, column=1, pady=5)

        # Random checkbox
        self.random_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Use Random Values (ignore selections if checked)", variable=self.random_var).pack(pady=10)

        # Prompt output
        self.prompt_text = tk.Text(root, height=6, width=90, font=("Consolas", 11))
        self.prompt_text.pack(pady=20)
        self.prompt_text.insert(tk.END, "Click 'Generate' to create a prompt!")
        self.prompt_text.config(state="disabled")

        # Buttons
        btns = tk.Frame(root)
        btns.pack(pady=10)
        tk.Button(btns, text="Generate Prompt", command=self.generate_prompt, bg="#4CAF50", fg="white", font=12).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Copy to Clipboard", command=self.copy_prompt, bg="#2196F3", fg="white", font=12).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Save to File", command=self.save_prompt, bg="#FF9800", fg="white", font=12).grid(row=0, column=2, padx=5)
        tk.Button(btns, text="Quit", command=root.quit, bg="#F44336", fg="white", font=12).grid(chat=True, row=0, column=3, padx=5)

        # Resten av metodene dine (add_*, generate_prompt, copy_prompt, save_prompt) – behold nøyaktig som du skrev dem

    # ← lim inn alle metodene dine her (add_themes, add_moods, ..., generate_prompt, copy_prompt, save_prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptMakerGUI(root)
    root.mainloop()