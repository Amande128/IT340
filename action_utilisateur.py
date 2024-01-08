from mainV2 import image_temporaire, image_temporaire_meeple, grille_x_offset, grille_y_offset

def curseur_dans_derniere_tuile_posee(x, y):
    """True si le curseur se situe là où on a posé la dernière tuile"""
    return (x // 100 + grille_x_offset == jeu.derniere_position[0] and
            y // 100 + grille_y_offset == jeu.derniere_position[1])


def event_clic_gauche(event):
    """Le joueur fait un clic gauche dans le canvas"""
    global image_temporaire, image_temporaire_meeple
    if not jeu.fini:
        x, y = event.x // 100 + grille_x_offset, event.y // 100 + grille_y_offset

        if jeu.phase_courante == 0:  # phase de tuile
            if jeu.input_add_tile(x, y) == True:  # le joueur fait une proposition valide
                ajout_image_liste(jeu.pioche[0], jeu.sac_tuiles[jeu.pioche[0]].rotation)  # ajout de l'image à la liste

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


def event_clic_droit(event):
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
