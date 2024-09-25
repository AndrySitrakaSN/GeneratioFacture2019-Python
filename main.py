import datetime

# Listes des gares par zone
gares_zone_1 = ["Fianarantsoa", "Ambalakely", "Sahambavy", "Ampitambe", "Ranomena", "Andrambovato"]
gares_zone_2 = ["Madiorano", "Tolongoina", "Amboanjobe", "Manapatrana"]

# Prix par catégorie entre différentes zones
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
# Prix pour  dans la même zone
prix_zone_meme = {
    "1re classe": 15000,
    "2e classe": 10000,
    "Résidentiel": 25000
}

# Fonction pour afficher les gares
def afficher_gares():
    print("\nZone 01 :")
    for gare in gares_zone_1:
        print(f"- {gare}")
    
    print("\nZone 02 :")
    for gare in gares_zone_2:
        print(f"- {gare}")

# Fonction pour générer la buillet
def generer_facture(depart, destination, nb_places, classe, prix_total):
    date_actuelle = datetime.datetime.now().strftime("%d/%m/%Y")
    heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
    
    facture = f"""
    ==============================
              FACTURE
    ==============================
    Gare de départ    : {depart}
    Gare d'arrivée    : {destination}
    Nombre de places  : {nb_places}
    Classe            : {classe}
    Prix total        : {prix_total} Ar
    Date              : {date_actuelle}
    Heure             : {heure_actuelle}
    ==============================
    """
    print(facture)

# Fonction principale de l'application
def main():
    print("Bienvenue à l'application de génération de billet de la Gare FCE !")
    
    afficher_gares()
    
    # Saisie des informations par l'utilisateur
    depart = input("\nEntrez la gare de départ : ")
    destination = input("Entrez la gare d'arrivée : ")
    
    while depart not in (gares_zone_1 + gares_zone_2) or destination not in (gares_zone_1 + gares_zone_2):
        print("Gare invalide. Veuillez entrer une gare valide.")
        depart = input("\nEntrez la gare de départ : ")
        destination = input("Entrez la gare d'arrivée : ")
    
    nb_places = int(input("Entrez le nombre de places que vous souhaitez réserver : "))
    
    print("\nChoisissez votre classe :")
    for classe in prix_classes.keys():
        print(f"- {classe}")
    
    classe_selectionnee = input("Entrez la classe : ")
    
    while classe_selectionnee not in prix_classes:
        print("Classe invalide. Veuillez entrer une classe valide.")
        classe_selectionnee = input("Entrez la classe : ")

    # Calcul du prix selon la zone
    if (depart == "Andrambovato" or destination == "Madiorano" or
        depart == "Madiorano" or destination == "Andrambovato"):
        # Appliquer le prix  pour Andrambovato et Madiorano
        prix_total = prix_special_andrambovato_madiorano[classe_selectionnee] * nb_places
    elif (depart in gares_zone_1 and destination in gares_zone_1) or (depart in gares_zone_2 and destination in gares_zone_2):
        #  Le prix est réduit si le départ et la destination sont dans la même zone
        prix_total = prix_zone_meme[classe_selectionnee] * nb_places
    else:
        # Appliquer le prix standard si les gares sont dans des zones différentes
        prix_total = prix_classes[classe_selectionnee] * nb_places

    # Génération de la facture
    generer_facture(depart, destination, nb_places, classe_selectionnee, prix_total)

# Lancer l'application
if __name__ == "__main__":
    main()
