from data_structures import *
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Canan
# importer le fichier csv et créer une liste de dictionnaires
# args: biblio: ListeChainée
def creationBiblio(biblio):
    with open('./projet/livre.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            livre = {
                "titre": row[0],
                "auteur": row[1],
                "langue": row[2],
                "style": row[3],
                "genre": row[4]
            }
            biblio.ajouter_fin(livre)

# Canan
# fonction de recherche de livre
# args: biblio: ListeChainée, search_terms: liste de tuples (clé, terme de recherche)
def searchBook(biblio, search_terms):
    results = []
    for i in range(biblio.taille()):
        livre = biblio.get_maillon_indice(i).valeur
        match = True
        for key, term in search_terms:
            if term.lower() not in livre[key].lower():
                match = False
                break
        if match:
            results.append(livre)
    return results

# Canan
# Gère la fonctionnalité de recherche pour l'application.
def on_search():
    global search_history
    search_term = search_entry.get()
    search_key = search_key_var.get()
    if search_term == "":
        search_history = MaPile()
        results = [biblio.get_maillon_indice(i).valeur for i in range(biblio.taille())]
    else:
        search_history.empiler((search_key, search_term))
        search_terms = []
        temp_history = MaPile()
        while not search_history.est_vide():
            search = search_history.depiler()
            search_terms.append(search)
            temp_history.empiler(search)
        while not temp_history.est_vide():
            search_history.empiler(temp_history.depiler())
        results = searchBook(biblio, search_terms)
    for row in tree.get_children():
        tree.delete(row)
    if results:
        for livre in results:
            tree.insert("", tk.END, values=(livre["titre"], livre["auteur"], livre["langue"], livre["style"], livre["genre"]))
    else:
        tree.insert("", tk.END, values=("Aucun livre trouvé avec ce recherche.", "", "", "", ""))

# Canan
# Gère la fonctionnalité de retour pour l'application. Il récupère le dernier terme de recherche de l'historique de recherche,
def on_back():
    global search_history, forward_history
    if not search_history.est_vide():
        current_search = (search_key_var.get(), search_entry.get())
        forward_history.empiler(current_search)
        search_history.depiler()
        if not search_history.est_vide():
            last_search = search_history.depiler()
            search_key_var.set(last_search[0])
            search_entry.delete(0, tk.END)
            search_entry.insert(0, last_search[1])
            on_search()

# Canan
# gere la navigation avant dans l'historique de recherche.
def on_forward():
    global search_history, forward_history
    if not forward_history.est_vide():
        current_search = (search_key_var.get(), search_entry.get())
        search_history.empiler(current_search)
        next_search = forward_history.depiler()
        search_key_var.set(next_search[0])
        search_entry.delete(0, tk.END)
        search_entry.insert(0, next_search[1])
        on_search()

# Canan
# Gère le clic sur l'en-tête de colonne pour trier les résultats de la recherche.
# args: event: événement de clic de souris
def on_column_click(event):
    column = tree.identify_column(event.x)
    column_name = columns[int(column[1:]) - 1].lower()
    biblio.tri_optimise(column_name)
    on_search()

# Canan
# Gère le double-clic sur un livre dans les résultats de la recherche. Il ajoute le livre sélectionné à la liste des livres visités.
# args: event: événement de double-clic de souris
def on_book_double_click(event):
    selected_item = tree.selection()[0]
    book = tree.item(selected_item, "values")
    visited_books_tree.insert("", tk.END, values=book)
    current_search_history = MaPile()
    temp_history = MaPile()
    while not search_history.est_vide():
        search = search_history.depiler()
        current_search_history.empiler(search)
        temp_history.empiler(search)
    while not temp_history.est_vide():
        search_history.empiler(temp_history.depiler())
    visited_search_history.empiler(current_search_history)

# Canan
# Gère le double-clic sur un livre dans la liste des livres visités. Il affiche les détails du livre sélectionné et l'historique de recherche associé.
# args: event: événement de double-clic de souris
def on_visited_book_double_click(event):
    selected_item = visited_books_tree.selection()[0]
    book = visited_books_tree.item(selected_item, "values")
    search_history = visited_search_history.depiler()

    def delete_book():
        visited_books_tree.delete(selected_item)
        popup.destroy()

    def on_popup_close():
        visited_search_history.empiler(search_history)
        popup.destroy()

    popup = tk.Toplevel(root)
    popup.title("Visited Book Details")
    popup.protocol("WM_DELETE_WINDOW", on_popup_close)

    book_details = f"Title: {book[0]}\nAuthor: {book[1]}\nLanguage: {book[2]}\nStyle: {book[3]}\nGenre: {book[4]}"
    search_history_details = ""
    current = search_history.liste.tete
    while current is not None:
        key, term = current.valeur
        search_history_details += f"{key}: {term}\n"
        current = current.suivant

    details_label = tk.Label(popup, text=f"Book Details:\n{book_details}\n\nSearch History:\n{search_history_details}")
    details_label.pack(pady=10)

    delete_button = tk.Button(popup, text="Delete", command=delete_book)
    delete_button.pack(pady=10)

# initialise les variables
biblio = ListeChainée()
creationBiblio(biblio)
biblio.tri_optimise("titre")
search_history = MaPile()
forward_history = MaPile()
visited_search_history = MaPile()

# fenetre principale
root = tk.Tk()
root.title("Library Search")

# recherche frame
search_frame = ttk.Frame(root)
search_frame.pack(pady=5)

# les boutons radio
search_key_var = tk.StringVar(value="titre")
keys = [("Title", "titre"), ("Author", "auteur"), ("Language", "langue"), ("Style", "style"), ("Genre", "genre")]
for text, value in keys:
    radio_button = ttk.Radiobutton(search_frame, text=text, variable=search_key_var, value=value)
    radio_button.pack(side=tk.LEFT, padx=5)

# recherche label et entry
search_label = ttk.Label(search_frame, text="Enter the search term:")
search_label.pack(side=tk.LEFT, padx=5)
search_entry = ttk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=5)

# recherche bouton
search_button = ttk.Button(search_frame, text="Search", command=on_search)
search_button.pack(side=tk.LEFT, padx=5)

# retour et avant boutons
back_button = ttk.Button(search_frame, text="Back", command=on_back)
back_button.pack(side=tk.LEFT, padx=5)
forward_button = ttk.Button(search_frame, text="Forward", command=on_forward)
forward_button.pack(side=tk.LEFT, padx=5)

# frame tables
tables_frame = ttk.Frame(root)
tables_frame.pack(pady=5, fill=tk.BOTH, expand=True)

# treeview livres
columns = ("Titre", "Auteur", "Langue", "Style", "Genre")
tree = ttk.Treeview(tables_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col, command=lambda _col=col: on_column_click)
    tree.column(col, width=150)
tree.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
tree.bind("<Button-1>", on_column_click)
tree.bind("<Double-1>", on_book_double_click)

# treeview livres visités
visited_books_columns = ("Titre", "Auteur", "Langue", "Style", "Genre")
visited_books_tree = ttk.Treeview(tables_frame, columns=visited_books_columns, show="headings")
for col in visited_books_columns:
    visited_books_tree.heading(col, text=col)
    visited_books_tree.column(col, width=150)
visited_books_tree.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
visited_books_tree.bind("<Double-1>", on_visited_book_double_click)

# lancer l'application
on_search()
root.mainloop()