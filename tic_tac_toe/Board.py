# !/usr/bin/python


class Board:

    def __init__(self):
        self._board = ["-" for _ in range(9)]

    def board_display(self):
        """affichier damier """
        for i in range(0, len(self._board)):
            print(self._board[i], end='|')
            if (i + 1) % 3 == 0:
                print(" ")

    def move(self, pos, piece):
        """Placer la pièce X dans la position pos"""
        if self._board[pos] != "-":
            print("Vous ne pouvez pas jouer votre pièce ici ")
        else:
            self._board[pos] = piece

    def move1(self, pos, piece):
        """Placer la pièce X dans la position pos et return le nouveau board"""
        B = Board()

        for i in range(0, len(self._board)):
            B._board[i] = self._board[i]

        if B._board[pos] != "-":
            print("Vous ne pouvez pas jouer votre pièce ici ")
        else:
            B._board[pos] = piece
        return B

    def is_move_legal(self, pos):
        """verifier si on peut placer le piece a position pos"""
        if self._board[pos] == "-":
            return True
        else:
            return False

    def get_moves_legal(self):
        """retourner les move legal"""
        moves = []
        for i in range(9):
            if self._board[i] == '-':
                moves.append(i)
        return moves

    def is_termine(self):
        """verifier si le game est deja termine"""
        board = self._board
        lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]

        if ['X'] * 3 in lines or ['O'] * 3 in lines or '-' not in board:
            return True
        else:
            return False

    def get_winner(self):
        board = self._board
        lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]

        if ['O'] * 3 in lines:
            return "O"
        elif ['X'] * 3 in lines:
            return "X"
        else:
            return "match nul"

    def restart(self):
        """Réinitialisation du jeu"""
        for i in range(0, len(self._board)):
            self._board[i] = "-"



