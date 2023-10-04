# Importation bibliothèques
import pygame, sys

# Init
pygame.init()

# Création fenêtre
largeur, hauteur = 600, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("TicTacToe - Python Edition")

# Couleurs & Traits
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
EPAISSEUR_LIGNE = 15
EPAISSEUR_TRAIT = 10

grille = [["" for c in range(3)] for l in range(3)]
tour_joueur = "X"

def afficher_grille():
    '''
    Fonction affichant la grille et gérant les symboles X et O
    '''
    taille_case = largeur // 3

    # Création des symboles
    for ligne in range(3):
        for col in range(3):
            if grille[ligne][col] == "X":
                pygame.draw.line(fenetre, ROUGE, (col * taille_case, ligne * taille_case), ((col + 1) * taille_case, (ligne + 1) * taille_case), EPAISSEUR_TRAIT)
                pygame.draw.line(fenetre, ROUGE, ((col + 1) * taille_case, ligne * taille_case), (col * taille_case, (ligne + 1) * taille_case), EPAISSEUR_TRAIT)
            elif grille[ligne][col] == "O":
                pygame.draw.circle(fenetre, BLEU, (col * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2), taille_case // 2 - 5, EPAISSEUR_TRAIT)

    # Création des lignes de la grille
    for ligne in range(1, 3):
        pygame.draw.line(fenetre, NOIR, (0, ligne * taille_case), (largeur, ligne * taille_case), EPAISSEUR_LIGNE)
    for col in range(1, 3):
        pygame.draw.line(fenetre, NOIR, (col * taille_case, 0), (col * taille_case, hauteur), EPAISSEUR_LIGNE)

def verifier_gagnant():
    '''
    Fonction renvoyant le symbole du gagnant si trois même symboles sont alignés
    '''
    # Check lignes / colonnes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "":
            return grille[i][0]
        if grille[0][i] == grille[1][i] == grille[2][i] != "":
            return grille[0][i]

    # Check diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != "":
        return grille[0][0]
    if grille[0][2] == grille[1][1] == grille[2][0] != "":
        return grille[0][2]

    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not verifier_gagnant():
            x, y = pygame.mouse.get_pos()
            colonne = x // (largeur // 3)
            ligne = y // (hauteur // 3)
            if grille[ligne][colonne] == "":
                grille[ligne][colonne] = tour_joueur
                if tour_joueur == "X":
                    tour_joueur = "O"
                else:
                    tour_joueur = "X"

    fenetre.fill((255, 255, 255))
    afficher_grille()

    if verifier_gagnant():
        font = pygame.font.Font(None, 36)
        texte = font.render("Le joueur {0} a gagné !".format(gagnant), True, ROUGE, NOIR)
        fenetre.blit(texte, ((largeur - texte.get_width()) // 2, (hauteur - texte.get_height()) // 2))

    pygame.display.flip()