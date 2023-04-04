# !/usr/bin/python
import pygame
from pygame import font


class Button(object):
    def __init__(self, words, font_size, font1, rect):
        """Définir les propriétés du bouton """
        self.words = words
        self.font_size = font_size
        self.rect = rect  # rect est le position de button

        # bx,by sont les positions de x,y axes de button
        # bw, by sont le weigth  et heigth de button
        bx, by, bw, bh = self.rect

        self.text = font1.render(self.words, True, (0, 0, 0))
        tw, th = self.text.get_size()
        tx = bx + bw / 2 - tw / 2
        ty = by + bh / 2 - th / 2
        self.text_pos = tx, ty

    def draw(self, screen):

        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        screen.blit(self.text, self.text_pos)

    def is_mousse_in_button(self, pos):
        """verifier si le position de mousse est sur le button"""
        bx, by, bw, bh = self.rect
        if bx <= pos[0] <= bx + bw and by <= pos[1] <= by + bh:
            return True
        else:
            return False

    def clique(self, pos, screen):
        """si le button est clique changer le couleur de button"""
        bx, by, bw, bh = self.rect
        if self.is_mousse_in_button(pos):
            pygame.draw.rect(screen, (255, 0, 0), self.rect)
            screen.blit(self.text, self.text_pos)
            pygame.display.update()

    def relacher(self, pos, screen):
        """si le button est relache, changer le couleur de button"""
        bx, by, bw, bh = self.rect
        if self.is_mousse_in_button(pos):
            pygame.draw.rect(screen, (200, 200, 200), self.rect)
            screen.blit(self.text, self.text_pos)
            pygame.display.update()


"""-------------------------Une partie du matériel contenu dans les pages----------------------------------------"""
# piece1 = "X"
piece1 = pygame.image.load("/Users/yangcong/文件/学习/M2/IA/Projet_2/tic_tac_toe/img/piece2.png")
piece1 = pygame.transform.scale(piece1, (100, 100))

# piece2 = "O"
piece2 = pygame.image.load("/Users/yangcong/文件/学习/M2/IA/Projet_2/tic_tac_toe/img/piece1.png")
piece2 = pygame.transform.scale(piece2, (100, 100))

"""-------------------------certain fonctions---------------------------------------"""


def get_value_pos(pos):
    """on a position(x,y) => retourner value(012345678)"""
    if 375 < pos[0] < 475:
        if 35 < pos[1] < 135:
            return 0
        elif 135 < pos[1] < 235:
            return 3
        elif 235 < pos[1] < 335:
            return 6
    elif 475 < pos[0] < 575:
        if 35 < pos[1] < 135:
            return 1
        elif 135 < pos[1] < 235:
            return 4
        elif 235 < pos[1] < 335:
            return 7
    elif 575 < pos[0] < 675:
        if 35 < pos[1] < 135:
            return 2
        elif 135 < pos[1] < 235:
            return 5
        elif 235 < pos[1] < 335:
            return 8


def get_pos_value(value):
    """on a value(012345678) => retourner position(x,y)"""
    pos = {}
    if value == 0:
        pos[0] = 375
        pos[1] = 35
    if value == 1:
        pos[0] = 475
        pos[1] = 35
    if value == 2:
        pos[0] = 575
        pos[1] = 35

    if value == 3:
        pos[0] = 375
        pos[1] = 135
    if value == 4:
        pos[0] = 475
        pos[1] = 135
    if value == 5:
        pos[0] = 575
        pos[1] = 135

    if value == 6:
        pos[0] = 375
        pos[1] = 235
    if value == 7:
        pos[0] = 475
        pos[1] = 235
    if value == 8:
        pos[0] = 575
        pos[1] = 235

    return pos


def display_player(words, player, font1, screen, pos_y):
    """affichier les information de player"""
    text1 = font1.render(words + " : ", True, (0, 0, 0))
    screen.blit(text1, (750, pos_y))
    text2 = font1.render(player.piece + ":", True, (0, 0, 0))
    screen.blit(text2, (800, pos_y + 50))

    if player.human:
        text3 = font1.render("Human ", True, (0, 0, 0))
        screen.blit(text3, (850, pos_y + 50))
    else:
        text3 = font1.render("AI  ", True, (0, 0, 0))
        screen.blit(text3, (850, pos_y + 50))
        if player.mode == 0:
            text4 = font1.render("Random  ", True, (0, 0, 0))
            screen.blit(text4, (900, pos_y + 50))
        elif player.mode == 1:
            text4 = font1.render("Minmax  ", True, (0, 0, 0))
            screen.blit(text4, (900, pos_y + 50))
        else:
            text4 = font1.render("AlphaBeta  ", True, (0, 0, 0))
            screen.blit(text4, (900, pos_y + 50))


def set_player_choisi(words, font1, font2, pos, screen):
    text1 = font1.render(words + " : ", True, (0, 0, 0))
    screen.blit(text1, pos)
    button_human = Button("Human", 20, font2, (pos[0] + 50, pos[1] + 50, 125, 30))
    button_human.draw(screen)

    button_ai_random = Button("AI_Random", 20, font2, (pos[0] + 200, pos[1] + 50, 125, 30))
    button_ai_random.draw(screen)

    button_ai_minmax = Button("AI_MinMax", 20, font2, (pos[0] + 50, pos[1] + 100, 125, 30))
    button_ai_minmax.draw(screen)

    button_ai_alphabeta = Button("AI_AlphaBete", 20, font2, (pos[0] + 200, pos[1] + 100, 125, 30))
    button_ai_alphabeta.draw(screen)

    return [button_human, button_ai_random, button_ai_minmax, button_ai_alphabeta]


def choisir_mode(buttons_player, buttons_player_choisi, pos, screen):
    for i in range(0, len(buttons_player)):
        if buttons_player[i].is_mousse_in_button(pos) and not buttons_player_choisi[i]:

            for j in range(0, len(buttons_player_choisi)):
                if buttons_player_choisi[j]:
                    buttons_player_choisi[j] = False

                    bx, by, bw, bh = buttons_player[j].rect
                    buttons_player[j].relacher((bx, by), screen)

            buttons_player_choisi[i] = True
            buttons_player[i].clique(pos, screen)
            break


def screen_game():
    pygame.init()
    pygame.display.set_caption('Tic_tac_toe')
    screen = pygame.display.set_mode((1100, 400), 0, 32)

    check_board = pygame.Rect(375, 35, 300, 300)

    screen.fill((155, 155, 155))
    pygame.draw.rect(screen, (225, 225, 225), check_board, 300)

    pygame.draw.line(screen, (0, 0, 0), (375, 135), (675, 135), width=1)
    pygame.draw.line(screen, (0, 0, 0), (375, 235), (675, 235), width=1)
    pygame.draw.line(screen, (0, 0, 0), (475, 35), (475, 335), width=1)
    pygame.draw.line(screen, (0, 0, 0), (575, 35), (575, 335), width=1)

    font1 = pygame.font.SysFont("arial", 25)
    font2 = pygame.font.SysFont("arial", 20)

    button_restar = Button("Restart", 20, font1, (800, 350, 125, 25))
    button_restar.draw(screen)

    buttons_player1 = set_player_choisi("player 1", font1, font2, (10, 20), screen)
    buttons_player2 = set_player_choisi("player 2", font1, font2, (10, 180), screen)

    button_star = Button("Start", 20, font1, (135, 350, 125, 25))
    button_star.draw(screen)

    pygame.display.update()

    return screen, buttons_player1, buttons_player2, button_star, button_restar
