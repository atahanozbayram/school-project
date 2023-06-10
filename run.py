import tkinter as tk
from tkinter import filedialog
from spellchecker import SpellChecker

# Function to open a file dialog and get the document path
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        process_document(file_path)

# Function to process the document and perform spell-checking
def process_document(file_path):
    spell_checker = SpellChecker(language='tr')
    corrected_words = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        
        for word in words:
            if not spell_checker.check(word):
                suggestions = spell_checker.suggest(word)
                corrected_words[word] = suggestions
    
    show_suggestions(corrected_words)

# Function to display suggestions and handle word replacements
def show_suggestions(corrected_words):
    suggestions_window = tk.Tk()
    suggestions_window.title("Spell Checker Suggestions")
    
    for word, suggestions in corrected_words.items():
        label = tk.Label(suggestions_window, text=f"Word: {word}")
        label.pack()
        
        if suggestions:
            for suggestion in suggestions:
                button = tk.Button(suggestions_window, text=suggestion,
                                   command=lambda w=word, s=suggestion: replace_word(w, s))
                button.pack()
        else:
            label = tk.Label(suggestions_window, text="No suggestions available.")
            label.pack()
    
    suggestions_window.mainloop()

# Function to replace a word with the selected suggestion or custom input
def replace_word(word, replacement):
    content = text_editor.get("1.0", tk.END)
    updated_content = content.replace(word, replacement)
    text_editor.delete("1.0", tk.END)
    text_editor.insert(tk.END, updated_content)

# GUI setup
root = tk.Tk()
root.title("Turkish Spell Checker")

text_editor = tk.Text(root)
text_editor.pack()

open_button = tk.Button(root, text="Open Document", command=open_file)
open_button.pack()

root.mainloop()
