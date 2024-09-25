import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from fpdf import FPDF  # Ajout de l'importation nécessaire

# Listes des gares par zone
gares_zone_1 = ["Fianarantsoa", "Ambalakely", "Sahambavy", "Ampitambe", "Ranomena", "Andrambovato"]
gares_zone_2 = ["Madiorano", "Tolongoina", "Amboanjobe", "Manapatrana"]

# Prix par catégorie pour trajets entre différentes zones
prix_classes = {
    "1re classe": 20000,
    "2e classe": 13000,
    "Résidentiel": 30000
}

# Prix spéciaux pour "Andrambovato" et "Madiorano"
prix_special_andrambovato_madiorano = {
    "1re classe": 15000,
    "2e classe": 10000,
    "Résidentiel": 25000
}

# Prix pour trajets dans la même zone
prix_zone_meme = {
    "1re classe": 15000,
    "2e classe": 10000,
    "Résidentiel": 25000
}

# Fonction pour générer la facture PDF avec un nom unique
def generer_facture_pdf(depart, destination, nb_places, classe, prix_total):
    date_actuelle = datetime.datetime.now().strftime("%d/%m/%Y")
    heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Générer un nom unique pour le fichier PDF
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"facture_{timestamp}.pdf"
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="FACTURE", ln=True, align="C")
    pdf.cell(200, 10, txt="==============================", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Gare de départ    : {depart}", ln=True)
    pdf.cell(200, 10, txt=f"Gare d'arrivée    : {destination}", ln=True)
    pdf.cell(200, 10, txt=f"Nombre de places  : {nb_places}", ln=True)
    pdf.cell(200, 10, txt=f"Classe            : {classe}", ln=True)
    pdf.cell(200, 10, txt=f"Prix total        : {prix_total} Ar", ln=True)
    pdf.cell(200, 10, txt=f"Date              : {date_actuelle}", ln=True)
    pdf.cell(200, 10, txt=f"Heure             : {heure_actuelle}", ln=True)
    pdf.cell(200, 10, txt="==============================", ln=True, align="C")

    # Enregistrer le fichier PDF
    pdf.output(nom_fichier)
    
    # Message de confirmation
    messagebox.showinfo("Facture", f"Facture enregistrée sous le nom {nom_fichier}")

# Fonction pour calculer le prix et générer la facture
def calculer_facture():
    depart = depart_combobox.get()
    destination = destination_combobox.get()
    nb_places = int(nb_places_entry.get())
    classe = classe_combobox.get()

    if (depart == "Andrambovato" or destination == "Madiorano" or
        depart == "Madiorano" or destination == "Andrambovato"):
        prix_total = prix_special_andrambovato_madiorano[classe] * nb_places
    elif (depart in gares_zone_1 and destination in gares_zone_1) or (depart in gares_zone_2 and destination in gares_zone_2):
        prix_total = prix_zone_meme[classe] * nb_places
    else:
        prix_total = prix_classes[classe] * nb_places

    # Générer la facture en PDF
    generer_facture_pdf(depart, destination, nb_places, classe, prix_total)

    # Rafraîchir la fenêtre
    depart_combobox.set("")
    destination_combobox.set("")
    nb_places_entry.delete(0, tk.END)
    classe_combobox.set("")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Génération de Billet FCE")

# Design de la fenêtre (fixée)
fenetre.geometry("400x400")
fenetre.resizable(False, False)

# Widgets pour les gares de départ et d'arrivée
depart_label = ttk.Label(fenetre, text="Gare de départ :")
depart_label.pack(pady=5)
depart_combobox = ttk.Combobox(fenetre, values=gares_zone_1 + gares_zone_2)
depart_combobox.pack(pady=5)

destination_label = ttk.Label(fenetre, text="Gare d'arrivée :")
destination_label.pack(pady=5)
destination_combobox = ttk.Combobox(fenetre, values=gares_zone_1 + gares_zone_2)
destination_combobox.pack(pady=5)

# Widget pour le nombre de places
nb_places_label = ttk.Label(fenetre, text="Nombre de places :")
nb_places_label.pack(pady=5)
nb_places_entry = ttk.Entry(fenetre)
nb_places_entry.pack(pady=5)

# Widget pour sélectionner la classe
classe_label = ttk.Label(fenetre, text="Classe :")
classe_label.pack(pady=5)
classe_combobox = ttk.Combobox(fenetre, values=list(prix_classes.keys()))
classe_combobox.pack(pady=5)

# Bouton pour générer la facture
generer_facture_btn = ttk.Button(fenetre, text="Générer Facture PDF", command=calculer_facture)
generer_facture_btn.pack(pady=20)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
