import pygame
from settings import WIDTH, HEIGHT

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Bauhaus 93", 60)
        self.instFont = pygame.font.SysFont("Bauhaus 93", 30)
        self.color = pygame.Color("white")
        self.instColor = pygame.Color("black")
        
        
    def show_score(self, intScore):
        birdScore = str(intScore)
        score = self.font.render(birdScore, True, self.color)
        self.screen.blit(score, (WIDTH // 2, 50))
    def instructions(self):
        inst_text0 = "Press SPACE to Jump,"
        inst_text1 = "Press \"R\" to Restart."
        ins0 = self.instFont.render(inst_text0, True, self.instColor)
        ins1 = self.instFont.render(inst_text1, True, self.instColor)
        self.screen.blit(ins0, (WIDTH // 4, 500))
        self.screen.blit(ins1, (WIDTH // 4, 450))
