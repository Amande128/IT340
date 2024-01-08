from tkinter import *
from PIL import Image, ImageTk  # Librairie à insaller : pip install pillow
from carcassonne_structure import *


def position_dans_tuile(x, y):
    """Renvoie la position x et y à l'intérieur de la tuile, en se basant sur une subdivision 3*3"""
    x, y = x % 100, y % 100  # position du curseur au sein de la tuile
    x, y = x // 34, y // 34  # on divise la tuile en une sous-grille 3*3
    return x, y


def afficher_image_temporaire(canva, i, j):
    """Affichage de l'image temporaire au niveau du curseur"""
    global image_temporaire
    if 0 <= i < grille_x_longueur and 0 <= j < grille_y_longueur:  # On se place dans la grille affichée
        if jeu.plat[i + grille_x_offset][
            j + grille_y_offset] == -1:  # Si on a aucune tuile à cet emplacement on montre la tuile actuelle
            img = Image.open("images/tuile" + str(jeu.pioche[0]) + ".png")  # On charge l'image puis on l'affiche
            img = img.rotate(jeu.sac_tuiles[jeu.pioche[0]].rotation * 90)
            image_temporaire = ImageTk.PhotoImage(img)
            afficher_image(canva, i * 100, j * 100, image_temporaire)
        else:
            image_temporaire = 0


def curseur_dans_derniere_tuile_posee(x, y):
    """True si le curseur se situe là où on a posé la dernière tuile"""
    return (x // 100 + grille_x_offset == jeu.derniere_position[0] and
            y // 100 + grille_y_offset == jeu.derniere_position[1])


def afficher_meeple_temporaire(canva, position, x, y):
    """Affichage du meeple temporaire"""
    global image_temporaire_meeple
    if curseur_dans_derniere_tuile_posee(x, y):  # si le curseur est sur la tuile qui vient d'être posée
        x, y = position_dans_tuile(x, y)

        if x == 1 or y == 1:  # le meeple est à un des emplacements qu'on souhaite donc on l'affiche
            img_meeple = Image.open("images/meeple" + str(jeu.joueur_courant) + ".png")
            image_temporaire_meeple = ImageTk.PhotoImage(img_meeple)
            afficher_image_meeple(canva, [position[0], position[1], point_cardinal_curseur[(x, y)]],
                                  image_temporaire_meeple)
        else:
            image_temporaire_meeple = 0
    else:
        image_temporaire_meeple = 0


def afficher_image(canva, x, y, img):
    """On affiche l'image dans le canvas"""
    canva.create_image(x, y, anchor=NW, image=img)


def afficher_grille(canva, tableau):
    """On affiche une grille de n*m tuiles sur l'écran"""
    canva.delete("all")  # quand on dessine les tuiles, on efface ce qu'on avait en dessous
    for i in range(grille_x_longueur):
        for j in range(grille_y_longueur):
            if tableau[i + grille_x_offset][j + grille_y_offset] >= 0:  # si on a une tuile à afficher
                afficher_image(canva, i * 100, j * 100, images[tableau[i + grille_x_offset][j + grille_y_offset]])
            elif tableau[i + grille_x_offset][j + grille_y_offset] < -1:  # si on a un mur
                afficher_image(canva, i * 100, j * 100, images[72])
            else:  # on a de l'herbe
                afficher_image(canva, i * 100, j * 100, images[73])
                canva.create_text(i * 100 + 50, j * 100 + 50,
                                  text="(" + str(i + grille_x_offset) + "," + str(j + grille_y_offset) + ")",
                                  fill="white")  # DEBUG

    if jeu.phase_courante == 1:  # on encadre la dernière tuile posée si on est en phase de meeple
        afficher_encadrement_tuile(canva)


def afficher_encadrement_tuile(canva):
    """Affiche un cadre autour de la dernière tuile posée"""
    x_pos_affichage = jeu.derniere_position[0] - grille_x_offset
    y_pos_affichage = jeu.derniere_position[1] - grille_y_offset
    if x_pos_affichage in range(grille_x_longueur) and y_pos_affichage in range(grille_y_longueur):
        # on encadre la tuile qui vient d'être posée si elle est dans l'afficage actuel
        canva.create_rectangle(x_pos_affichage * 100, y_pos_affichage * 100, (x_pos_affichage + 1) * 100,
                               (y_pos_affichage + 1) * 100, outline="bisque", width=2)

def afficher_meeple(canva):
    """Affiche tous les meeples des joueurs qui sont sur le plateau"""
    for i in range(jeu.nb_joueurs):
        print("Score du joueur", i + 1, ":", jeu.joueurs[i].score)
        for j in range(len(jeu.joueurs[i].meeples)):
            meeple = jeu.joueurs[i].meeples[j]
            coords = meeple.coordonnees
            if meeple.type != 0 and coords[0] - grille_x_offset in range(grille_x_longueur) \
                    and coords[1] - grille_y_offset in range(
                grille_y_longueur):  # on affiche le meeple s'il est dans la portion qu'on affiche et qu'il fait parti des meeples à afficher
                x_offset, y_offset = affichage_dans_la_tuile[coords[2]][0], affichage_dans_la_tuile[coords[2]][1]  # au sein de la tuile, on décale selon le point cardinal
                x_pos, y_pos = coords[0] - grille_x_offset, coords[1] - grille_y_offset  # calcul de la position de la tuile
                canva.create_image(x_pos * 100 + x_offset, y_pos * 100 + y_offset, anchor=NW, image=images_meeple[i])
            print(jeu.joueurs[i].meeples[j])


def add_image_liste(id_image_ajoutee, rotation):
    """On ajoute la tuile à la liste d'images fixes"""
    img = Image.open("images/tuile" + str(id_image_ajoutee) + ".png")  # chargement de l'image
    img = img.rotate(rotation * 90)  # rotation de l'image
    img_sauvegardee = ImageTk.PhotoImage(img)
    images[id_image_ajoutee] = img_sauvegardee


def clic_gauche(event):
    """Le joueur fait un clic gauche dans le canvas"""
    global image_temporaire, image_temporaire_meeple
    if not jeu.fini:
        x, y = event.x // 100 + grille_x_offset, event.y // 100 + grille_y_offset

        if jeu.phase_courante == 0:  # phase de tuile
            if jeu.input_add_tile(x, y) == True:  # le joueur fait une proposition valide
                add_image_liste(jeu.pioche[0], jeu.sac_tuiles[jeu.pioche[0]].rotation)  # ajout de l'image à la liste

                jeu.fin_phase_tuile(x, y)  # on termine la phase

                afficher_grille(canvas, jeu.plat)  # mise à jour de l'affichage
                afficher_meeple(canvas)
                image_temporaire = 0

        elif jeu.phase_courante == 1:  # phase meeple
            i, j = position_dans_tuile(event.x, event.y)  # i et j valent entre 0 et 2 au sein de la tuile subdivisée
            if i == 1 or j == 1:  # Au sein de la tuile pointée, on se situe à un des endroits où le meeple peut être placé
                point_cardinal = point_cardinal_curseur[(i, j)]
                if jeu.check_pour_poser_meeple(x, y, point_cardinal) == True:  # le joueur fait une proposition valide

                    jeu.fin_phase_meeple(point_cardinal)  # on termine la phase

                    afficher_meeple(canvas)  # mise à jour de l'affichage
                    image_temporaire_meeple = 0


def clic_droit(event):
    """Clic droit dans le canvas"""
    global image_temporaire_meeple
    if not jeu.fini:
        if jeu.phase_courante == 0:  # phase de tuile
            jeu.sac_tuiles[jeu.pioche[0]].tourner()
            afficher_image_temporaire(canvas, event.x // 100, event.y // 100)

        elif jeu.phase_courante == 1:
            passage_au_joueur_suivant()
            image_temporaire_meeple = 0


def deplacement_curseur(event):
    """Déplacement du curseur dans le canvas"""
    if not jeu.fini:
        if jeu.phase_courante == 0:  # phase de tuile
            afficher_image_temporaire(canvas, event.x // 100, event.y // 100)  # on affiche la tuile temporaire
        elif jeu.phase_courante == 1:  # phase de meeple
            afficher_meeple_temporaire(canvas, jeu.derniere_position, event.x,
                                       event.y)  # on affiche le meeple temporaire

    # print(jeu.plat_territoire[event.x//100][event.y//100])
    """print(jeu.plat_territoire[4][4].est)
    print(jeu.plat_territoire[4][4]["est"])
    jeu.plat_territoire[4][4]["est"] = [[0, 0]]"""


def passage_au_joueur_suivant():
    jeu.joueur_suivant()
    afficher_grille(canvas, jeu.plat)
    afficher_meeple(canvas)


def deplacement_grille_vers_la_gauche(event):
    mise_a_jour_grille_quand_deplacement(-1, 0, canvas)


def deplacement_grille_vers_la_droite(event):
    mise_a_jour_grille_quand_deplacement(1, 0, canvas)


def deplacement_grille_vers_le_haut(event):
    mise_a_jour_grille_quand_deplacement(0, -1, canvas)


def deplacement_grille_vers_le_bas(event):
    mise_a_jour_grille_quand_deplacement(0, 1, canvas)


def mise_a_jour_grille_quand_deplacement(modif_x, modif_y, canva):
    global grille_x_offset, grille_y_offset
    # on met à jour la partie affichée si on ne passe pas au dela d'un mur
    if grille_x_offset + modif_x in range(len(jeu.plat) - grille_x_longueur + 1) and \
            grille_y_offset + modif_y in range(len(jeu.plat) - grille_y_longueur + 1):
        grille_x_offset += modif_x
        grille_y_offset += modif_y
        afficher_grille(canva, jeu.plat)
        afficher_meeple(canva)


def fin_jeu(event):
    jeu.fin_du_jeu()


def skip_tuile(event):
    passage_au_joueur_suivant(jeu)


def setup_offset_grille():
    """Place la caméra au centre du plateau"""
    global grille_x_offset, grille_y_offset
    grille_x_offset = (len(jeu.plat) - grille_x_longueur + 1) // 2
    grille_y_offset = (len(jeu.plat) - grille_y_longueur + 1) // 2


if __name__ == "__main__":
    Window = Tk()
    main_frame = Frame(Window)
    main_frame.pack()

    # arial30 = tkFont.Font(family='Arial', size=30) Au final, pas utilisée

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

    # mise en place des interactions avec l'utilisateur
    canvas.bind("<Button-1>", clic_gauche)
    canvas.bind("<Button-2>", clic_droit)  # selon les appareils, le clic droit peut varier entre 2 et 3
    canvas.bind("<Button-3>", clic_droit)
    canvas.bind("<Motion>", deplacement_curseur)
    main_frame.focus_set()  # pour récupérer les inputs du clavier
    main_frame.bind("<Left>", deplacement_grille_vers_la_gauche)
    main_frame.bind("<Right>", deplacement_grille_vers_la_droite)
    main_frame.bind("<Up>", deplacement_grille_vers_le_haut)
    main_frame.bind("<Down>", deplacement_grille_vers_le_bas)

    # bind pour debug
    main_frame.bind("f", fin_jeu)
    main_frame.bind("s", skip_tuile)

    # pour l'affichage graphique, on utilise des dictionnaires pour récupérer et convertir des données
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
    for i in range(2):  # on charge les images de meeple
        images_meeple[i] = ImageTk.PhotoImage(Image.open("images/meeple" + str(i) + ".png"))

    image_temporaire_meeple = ImageTk.PhotoImage(Image.open("images/meeple0.png"))

    jeu = Jeu(2, 3)  # initialisation du jeu pour deux joueurs
    # Test début de jeu
    """jeu.derniere_position = [4, 4]
    jeu.pose_meeple(jeu.joueurs[jeu.joueur_courant].meeples[0], "est")
    jeu.joueur_suivant()
    jeu.pose_meeple(jeu.joueurs[jeu.joueur_courant].meeples[0], "est")
    jeu.joueur_suivant()"""

    setup_offset_grille()  # les coordonnées d'offset sont de telle sorte qu'on se place au milieu de la grille
    afficher_grille(canvas, jeu.plat)  # affichage de la grille au début du jeu

    canvas.pack()
    Window.mainloop()
