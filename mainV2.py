from tkinter import *
from PIL import Image, ImageTk  # Librairie à insaller : pip install pillow
from carcassonne_structure import *
from affichage import *
from action_utilisateur import *

def position_dans_tuile(x, y):
    """Renvoie la position x et y à l'intérieur de la tuile, en se basant sur une subdivision 3*3"""
    x, y = x % 100, y % 100  # position du curseur au sein de la tuile
    x, y = x // 34, y // 34  # on divise la tuile en une sous-grille 3*3
    return x, y


def ajout_image_liste(id_image_ajoutee, rotation):
    """On ajoute la tuile à la liste d'images fixes"""
    img = Image.open("images/tuile" + str(id_image_ajoutee) + ".png")  # chargement de l'image
    img = img.rotate(rotation * 90)  # rotation de l'image
    img_sauvegardee = ImageTk.PhotoImage(img)
    images[id_image_ajoutee] = img_sauvegardee


def setup_camera_on_grille():
    """Place la caméra au centre du plateau"""
    global grille_x_offset, grille_y_offset
    grille_x_offset = (len(jeu.plat) - grille_x_longueur + 1) // 2
    grille_y_offset = (len(jeu.plat) - grille_y_longueur + 1) // 2


def interactions_utilisateurs():
    global canva, main_frame
    canvas.bind("<Button-1>", event_clic_gauche)
    # selon les appareils, le clic droit peut varier entre 2 et 3
    canvas.bind("<Button-2>", event_clic_droit)
    canvas.bind("<Button-3>", event_clic_droit)
    canvas.bind("<Motion>", deplacement_curseur)
    main_frame.focus_set()  # pour récupérer les inputs du clavier
    main_frame.bind("<Left>", deplacement_grille_vers_la_gauche)
    main_frame.bind("<Right>", deplacement_grille_vers_la_droite)
    main_frame.bind("<Up>", deplacement_grille_vers_le_haut)
    main_frame.bind("<Down>", deplacement_grille_vers_le_bas)

    main_frame.bind("f", fin_jeu)
    main_frame.bind("s", skip_tuile)


if __name__ == "__main__":
    Window = Tk()
    main_frame = Frame(Window)
    main_frame.pack()

    # au niveau de l'affichage, on a des variables du nombre de tuiles à afficher d'offset car on affiche seulement une partie de la grille
    grille_x_offset, grille_y_offset = 1, 1
    grille_x_longueur, grille_y_longueur = 13, 8

    # Espace de l'écran où il y aura les informations sur les joueurs et sur la partie en cours + les boutons de Menu Règles Son ...
    MenuJeu = Canvas(main_frame, width=400, height=800)
    MenuJeu.pack(side=LEFT)

    # mise en place de l'affichage de la grille et du canvas
    espace_de_jeu = Frame(main_frame)
    espace_de_jeu.pack()

    images_fleches = {0: PhotoImage(file="images/fleche_haut.png"),
                      1: PhotoImage(file="images/fleche_gauche.png"),
                      2: PhotoImage(file="images/fleche_droite.png"),
                      3: PhotoImage(file="images/fleche_bas.png")}

    bouton_haut = Button(espace_de_jeu, image=images_fleches[0], command=lambda: deplacement_grille_vers_le_haut(0))
    bouton_gauche = Button(espace_de_jeu, image=images_fleches[1], command=lambda: deplacement_grille_vers_la_gauche(0))
    bouton_droite = Button(espace_de_jeu, image=images_fleches[2], command=lambda: deplacement_grille_vers_la_droite(0))
    bouton_bas = Button(espace_de_jeu, image=images_fleches[3], command=lambda: deplacement_grille_vers_le_bas(0))

    bouton_haut.pack(side=TOP, fill=X)
    bouton_bas.pack(side=BOTTOM, fill=X)
    bouton_gauche.pack(side=LEFT, fill=Y)
    bouton_droite.pack(side=RIGHT, fill=Y)

    canvas = Canvas(espace_de_jeu, width=grille_x_longueur * 100, height=grille_y_longueur * 100)    

    # définition du dictionnaire qui associe une position au sein de la tuile au point cardinal
    point_cardinal_curseur = {(1, 0): "nord", (0, 1): "ouest", (1, 1): "abbaye", (2, 1): "est", (1, 2): "sud"}
    affichage_dans_la_tuile = {"nord": (34, 0), "ouest": (0, 34), "abbaye": (34, 34), "est": (67, 34), "sud": (34, 67)}

    # on charge toutes les objets des images dans un tableau
    images = {0: ImageTk.PhotoImage(Image.open("images/tuile0.png")),
              72: ImageTk.PhotoImage(Image.open("images/mur.png")),
              73: ImageTk.PhotoImage(Image.open("images/herbe.png"))}
    image_temporaire = ImageTk.PhotoImage(Image.open("images/tuile0.png"))

    # on fait de même pour les meeples
    images_meeple = {}
    for i in range(2):
        images_meeple[i] = ImageTk.PhotoImage(Image.open("images/meeple" + str(i) + ".png"))

    image_temporaire_meeple = ImageTk.PhotoImage(Image.open("images/meeple0.png"))

    jeu = Jeu(2, 3)  # initialisation du jeu pour deux joueurs

    setup_camera_on_grille()  # les coordonnées d'offset sont de telle sorte qu'on se place au milieu de la grille
    afficher_grille(canvas, jeu.plat)  # affichage de la grille au début du jeu

    canvas.pack()
    Window.mainloop()
