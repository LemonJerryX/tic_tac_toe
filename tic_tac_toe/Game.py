# !/usr/bin/python
import time

import pygame

from AIPlayer import AIPlayer
from Board import Board
from GUI import piece1, piece2, Button, screen_game, choisir_mode, display_player
from HumanPlayer import HumanPlayer


class Game:
    def __init__(self):
        self.current_player = None
        self.player1 = None
        self.player2 = None
        self.board = Board()

    def switch_player(self):
        """changer current_player"""
        if self.current_player == self.player2:
            self.current_player = self.player1
        else:
            self.current_player = self.player2



    def restart(self):
        """Réinitialisation du jeu"""
        self.board.restart()

        self.run()

    def game_over(self, screen):
        if self.board.is_termine():
            font1 = pygame.font.SysFont("arial", 50)
            win_piece = self.board.get_winner()
            if win_piece == self.player1.piece:
                button_win = Button("Player 1 win !!!", 50, font1, (700, 100, 350, 200))
            elif win_piece == self.player2.piece:
                button_win = Button("Player 2 win !!!", 50, font1, (700, 100, 350, 200))
            else:
                button_win = Button("Match null !!!", 50, font1, (700, 100, 350, 200))

            button_win.draw(screen)
            pygame.display.update()

    def set_players(self, buttons_player1_choisi, buttons_player2_choisi):
        if buttons_player1_choisi[0]:
            self.player1 = HumanPlayer("X")
        if buttons_player1_choisi[1]:
            self.player1 = AIPlayer("X", 0)
        if buttons_player1_choisi[2]:
            self.player1 = AIPlayer("X", 1)
        if buttons_player1_choisi[3]:
            self.player1 = AIPlayer("X", 2)

        if buttons_player2_choisi[0]:
            self.player2 = HumanPlayer("O")
        if buttons_player2_choisi[1]:
            self.player2 = AIPlayer("O", 0)
        if buttons_player2_choisi[2]:
            self.player2 = AIPlayer("O", 1)
        if buttons_player2_choisi[3]:
            self.player2 = AIPlayer("O", 2)

    def game_play(self, screen, premier):

        if type(self.player1) == AIPlayer and type(self.player2) == AIPlayer:
            if premier:
                pos = self.current_player.move_random(self.board)
                self.current_player.move(self.board, pos, screen, piece1, piece2)
                self.switch_player()
                self.board.board_display()
                premier = False

        while not self.board.is_termine():
            print("-------------------------------")
            time_start = time.time()
            pos = self.current_player.think(self.board)
            self.current_player.move(self.board, pos, screen, piece1, piece2)
            self.switch_player()
            self.board.board_display()

            time_end = time.time()
            print('time cost', (time_end - time_start) * 1000, 'ms')

            pygame.display.update()
        self.game_over(screen)

    def run(self):

        screen, buttons_player1, buttons_player2, button_star, button_restar = screen_game()

        font_size = 25
        font1 = pygame.font.SysFont("arial", font_size)

        pygame.display.update()

        buttons_player1_choisi = [False, False, False, False]
        buttons_player2_choisi = [False, False, False, False]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_restar.is_mousse_in_button(event.pos):
                        button_restar.clique(event.pos, screen)
                        self.restart()

                    choisir_mode(buttons_player1, buttons_player1_choisi, event.pos, screen)
                    choisir_mode(buttons_player2, buttons_player2_choisi, event.pos, screen)

                    button_star.clique(event.pos, screen)

                if event.type == pygame.MOUSEBUTTONUP:
                    button_star.relacher(event.pos, screen)
                    if button_star.is_mousse_in_button(event.pos):
                        self.set_players(buttons_player1_choisi, buttons_player2_choisi)
                        display_player("Player 1", self.player1, font1, screen, 100)
                        display_player("Player 2", self.player2, font1, screen, 220)

                        pygame.display.update()

                        self.current_player = self.player1
                        self.game_play(screen, True)

                    button_restar.relacher(event.pos, screen)

            pygame.display.update()
