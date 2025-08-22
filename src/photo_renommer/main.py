import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import sys

from renommer.renommer import renommer_dir

def main() -> None :

    def resource_path(relative_path:str) -> Path:
        """Retourne le chemin absolu correct du fichier, que ce soit en dev ou en EXE PyInstaller."""
        if getattr(sys, 'frozen', False):
            # Chemin temporaire PyInstaller
            base_path = Path(sys._MEIPASS) # type: ignore
        else:
            # Chemin normal en dev
            base_path = Path(__file__).parent.parent
        return base_path / relative_path

    # Fonction de récupération du dossier
    def choisir_dossier() -> None :
        dossier = filedialog.askdirectory()
        if dossier:
            dossier_var.set(dossier)
    
    # Fonction d'appel au renommeur
    def renommer_images() -> None :
        dossier = Path(dossier_var.get())
        date = date_var.get()
        nom = nom_var.get()
        val_start = val_start_var.get()
        order_by = choix_order[order_by_var.get()]

        if not dossier.exists():
            messagebox.showerror("Erreur", "Dossier invalide.")
            return
        if not date or not nom:
            messagebox.showerror("Erreur", "Remplissez tous les champs.")
            return
        if not val_start.isdigit() :
            messagebox.showerror("Erreur", "Valeur de départ doit contenir un nombre.")
            return
        
        renommer_dir(dossier, date, nom, int(val_start), order_by)

        messagebox.showinfo("Info", "Le renommage des fichiers s'est déroulé dans problème.")


    # Fenêtre principale
    window = tk.Tk()
    window.title("Renommeur de Photos")
    window.geometry("400x300")

    # Icône au format PNG
    icone_path = resource_path("assets/ico.png")
    icone = tk.PhotoImage(file=icone_path)
    window.iconphoto(True, icone)

    # Variables
    date_var = tk.StringVar()
    nom_var = tk.StringVar()
    dossier_var = tk.StringVar()
    val_start_var = tk.StringVar(value="1")
    order_by_var = tk.StringVar(value="Date de dernière modification")

    # Choix
    choix_order = {"Date de dernière modification" : "Modifie",
                   "Date de création" : "Cree",
                   "Nom du fichier" : "Nom"}

    # Widgets
    tk.Label(window, text="Date fixe (ex: 2025 08 15) :").pack(pady=5)
    tk.Entry(window, textvariable=date_var, width=30).pack(padx=10)

    tk.Label(window, text="Nom fixe (ex: Jeux Olympiques) :").pack(pady=5)
    tk.Entry(window, textvariable=nom_var, width=30).pack(padx=10)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    frame1 = tk.Frame(frame)
    frame1.pack(side=tk.LEFT, padx=10)
    tk.Label(frame1, text="Valeur de départ (ex: 15) :").pack(pady=5)
    tk.Entry(frame1, textvariable=val_start_var, width=5).pack(pady=5)
    frame2 = tk.Frame(frame)
    frame2.pack(side=tk.LEFT, padx=10)
    tk.Label(frame2, text="Type de tri :").pack(pady=5)
    ttk.Combobox(frame2, textvariable=order_by_var, values=list(choix_order), state="readonly", width=max(len(opt) for opt in choix_order)).pack(pady=5)

    tk.Button(window, text="Choisir dossier", command=choisir_dossier).pack(pady=5)
    tk.Label(window, textvariable=dossier_var, fg="blue").pack()

    tk.Button(window, text="Renommer", command=renommer_images).pack(pady=10)

    window.mainloop()

if __name__ == "__main__" :
    main()