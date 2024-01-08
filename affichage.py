from mainV2 import image_temporaire, image_temporaire_meeple

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


def afficher_image_meeple(canva, coords, img):
    """On affiche un meeple en fonction de ses coordonnées x,y et point_cardinal"""
    x_offset, y_offset = affichage_dans_la_tuile[coords[2]][0], affichage_dans_la_tuile[coords[2]][
        1]  # au sein de la tuile, on décale selon le point cardinal
    x_pos, y_pos = coords[0] - grille_x_offset, coords[1] - grille_y_offset  # calcul de la position de la tuile
    canva.create_image(x_pos * 100 + x_offset, y_pos * 100 + y_offset, anchor=NW, image=img)


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
                afficher_image_meeple(canva, coords, images_meeple[i])
            print(jeu.joueurs[i].meeples[j])
