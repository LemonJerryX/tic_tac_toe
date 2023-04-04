# !/usr/bin/python
import pygame

from GUI import get_pos_value


class Player(object):
    '''
    Les joueurs ne font que deux choses : penser et jouer.
        1. réfléchir --> trouver un coup
        2. jouer --> exécuter le coup, modifier le tableau
    '''

    def __init__(self, piece='X'):  # La pièce par défaut est take = 'X'
        self.piece = piece
        self.human = False

    def think(self, board):
        pass

    def move(self, board, pos_value,  screen, piece1, piece2):
        board.move(pos_value, self.piece)
        pos_xy = get_pos_value(pos_value)
        rect = pygame.Rect(pos_xy[0], pos_xy[1], 100, 100)
        if self.piece == "X":
            screen.blit(piece1, rect)
        else:
            screen.blit(piece2, rect)



