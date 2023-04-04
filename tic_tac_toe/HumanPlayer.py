# !/usr/bin/python
import pygame

from GUI import get_value_pos
from Player import Player


class HumanPlayer(Player):
    def __init__(self, piece):
        super().__init__(piece)
        self.human = True

    def think(self, board):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 375 <= event.pos[0] <= 675 and 35 <= event.pos[1] <= 335:
                        pos = get_value_pos(event.pos)
                        if board.is_move_legal(pos):
                            print("human place le piece a position :", pos)
                            return pos
