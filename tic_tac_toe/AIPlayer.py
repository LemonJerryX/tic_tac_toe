# !/usr/bin/python
import pygame

from GUI import get_pos_value
from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, piece, mode):
        super().__init__(piece)
        self.mode = mode  # le modele de AI (0 = Random, 1=  Minmax,,,,)

    def think(self, board):

        pos_value = 0
        print('AI is thinking ...')
        if self.mode == 0:
            pos_value = self.move_random(board)
        if self.mode == 1:
            pos_value = self.min_max_pos(board)
        if self.mode == 2:
            pos_value = self.alpha_beta_pos(board)

        print("AI place le piece a position : ", pos_value)

        return pos_value

    @staticmethod
    def move_random(board):
        """Choisir un pas aléatoire parmi les marches possibles"""
        move_list = board.get_moves_legal()
        i = random.randint(0, len(move_list) - 1)
        return move_list[i]

    def min_max(self, board, depth, maxmizingPlayer, piece):
        """:return le score de board par le methode de minmax"""
        if board.is_termine() or depth == 0:
            return evaluer_board(board, depth, maxmizingPlayer, self.piece)

        if maxmizingPlayer:
            maxEval = -100
            move_list = board.get_moves_legal()
            for i in move_list:
                board_new = board.move1(i, piece)
                piece1 = change_piece(piece)
                Eval = self.min_max(board_new, depth - 1, False, piece1)
                maxEval = max(maxEval, Eval)
            return maxEval

        else:
            minEval = 100
            move_list = board.get_moves_legal()
            for i in move_list:
                board_new = board.move1(i, piece)
                piece1 = change_piece(piece)
                Eval = self.min_max(board_new, depth - 1, True, piece1)
                minEval = min(minEval, Eval)
            return minEval

    def min_max_pos(self, board):
        """:return le value de position par le methode de minmax"""
        move_list = board.get_moves_legal()
        maxscore = -100
        maxscore_pos = -1
        for i in range(0, len(move_list)):

            board_new = board.move1(move_list[i], self.piece)

            piece1 = change_piece(self.piece)
            score = self.min_max(board_new, 20, False, piece1)

            if score > maxscore:
                maxscore = score
                maxscore_pos = i
        return move_list[maxscore_pos]

    def alpha_beta(self, board, depth, maxmizingPlayer, piece, alpha, beta):
        """:return le score de board par le methode de minmax"""
        if board.is_termine() or depth == 0:
            return evaluer_board(board, depth, maxmizingPlayer, self.piece)

        if maxmizingPlayer:
            maxEval = -100
            move_list = board.get_moves_legal()
            for i in move_list:
                board_new = board.move1(i, piece)
                Eval = self.alpha_beta(board_new, depth - 1, False, change_piece(piece), alpha, beta)
                maxEval = max(maxEval, Eval)
                alpha = max(alpha, Eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 100
            move_list = board.get_moves_legal()
            for i in move_list:
                board_new = board.move1(i, piece)
                Eval = self.alpha_beta(board_new, depth - 1, True, change_piece(piece), alpha, beta)
                minEval = min(minEval, Eval)
                beta = min(beta, Eval)
                if beta <= alpha:
                    break
            return minEval

    def alpha_beta_pos(self, board):
        """:return le value de position par le methode de alpha_beta"""
        move_list = board.get_moves_legal()
        maxscore = -100
        maxscore_pos = -1
        for i in range(0, len(move_list)):

            board_new = board.move1(move_list[i], self.piece)

            piece1 = change_piece(self.piece)
            score = self.alpha_beta(board_new, 20, False, piece1, -1, 1)

            if score == 1:
                return move_list[i]

            if score > maxscore:
                maxscore = score
                maxscore_pos = i
        return move_list[maxscore_pos]


def change_piece(piece):
    """if piece couvrant = "X" :return "O" """
    piece1 = "-"
    if piece == "X":
        piece1 = "O"
    else:
        piece1 = "X"
    return piece1


def evaluer_board(board, depth, maxmizingPlayer, piece):
    """":return le secore de board if le board est fini ou il est deja arrive le depth"""
    if board.is_termine():
        if board.get_winner() == "match nul":
            return 0
        elif board.get_winner() == piece:
            return 1
        else:
            return -1
    if depth == 0:
        if maxmizingPlayer:
            return -100
        else:
            return 100
