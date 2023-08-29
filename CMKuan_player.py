import CMKuan_game
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.__height = 600
        self.__mapLen = len(CMKuan_game.Game.get_map())
        self.__player_height = 60
        self.__player_width = 60
        self.__point = 0
        self.__speed = 5
        self.__width = 800
        self.image = pygame.Surface((self.__player_width, self.__player_height))
        self.image = pygame.transform.scale(Player.get_image('image\管中閔(左).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.__width//2
        self.rect.centery = self.__height//2
    
    def add_point(self, point):
        self.__point += point

    def get_point(self):
        return (self.__point)

    def get_rect_x(self):
        return (self.rect.centerx)
    
    def get_rect_y(self):
        return (self.rect.centery)

    def update(self):
        keys = pygame.key.get_pressed()
        # move
        if keys[K_RIGHT]:
            if not ((self.rect.right > self.__width) and (CMKuan_game.Game.get_position()%self.__mapLen == (self.__mapLen-1))):
                self.rect.centerx += self.__speed
                self.image = pygame.transform.scale(Player.get_image('image\管中閔(右).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        if keys[K_DOWN]:
            if not ((self.rect.bottom > self.__height) and (CMKuan_game.Game.get_position() >= (self.__mapLen*(self.__mapLen-1)))):
                self.rect.centery += self.__speed
        if keys[K_LEFT]:
            if not((self.rect.left < 0) and (CMKuan_game.Game.get_position()%3 == 0)):
                self.rect.centerx -= self.__speed
                self.image = pygame.transform.scale(Player.get_image('image\管中閔(左).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        if keys[K_UP]:
            if not ((self.rect.top < 0) and (CMKuan_game.Game.get_position() < self.__mapLen)):
                self.rect.centery -= self.__speed

        # boundary case
        if (self.rect.right > self.__width) and (CMKuan_game.Game.get_position()%self.__mapLen != (self.__mapLen-1)):
            self.rect.centerx -= (self.__width-self.__player_width)
            CMKuan_game.Game.update_class_map(CMKuan_game.Game.get_position()+1)
        if (self.rect.bottom > self.__height) and (CMKuan_game.Game.get_position() < (self.__mapLen*(self.__mapLen-1))):
            self.rect.centery -= (self.__height-self.__player_height)
            CMKuan_game.Game.update_class_map(CMKuan_game.Game.get_position()+self.__mapLen)
        if (self.rect.left < 0) and (CMKuan_game.Game.get_position()%self.__mapLen != 0):
            self.rect.centerx += (self.__width-self.__player_width)
            CMKuan_game.Game.update_class_map(CMKuan_game.Game.get_position()-1)
        if (self.rect.top < 0) and (CMKuan_game.Game.get_position() >= self.__mapLen):
            self.rect.centery += (self.__height-self.__player_height)
            CMKuan_game.Game.update_class_map(CMKuan_game.Game.get_position()-self.__mapLen)

    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        return (pygame.transform.scale(pygame.image.load(fileName), (image_width, image_height)))
