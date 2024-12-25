
class Affichage_menu:

    def __init__(self):

        self.menu1 = "1) Enregistrer un saut en DB"
        self.menu2 = "2) Enregistrer des data en BD"
        self.menu3 = "3) Enregistrer un parachute"
        self.menu4 = "4) **********"

        pass

    #--------------------------
    # Méthodes
    #--------------------------

    def afficher_menu_principal(self):

        print("\n")
        print("MENU PRINCIPAL")

        print(70 * "-")
        print(5 * " " + f'{self.menu1}')
        print(5 * " " + f'{self.menu2}')
        print(5 * " " + f'{self.menu3}')
        print(5 * " " + f'{self.menu4}')

        print("\n" + "Appuyez sur q pour quitter")
        print(70 * "-")
        print("\n")
        choix = input("Que voulez vous faire: ")
        return choix