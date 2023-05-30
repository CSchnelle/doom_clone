import pygame as pg
import sys
import numpy as np
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *

class Game:
    #constructor that initializes pygame modules
    def __init__(self):
        pg.init()
        #disable mouse cursor
        pg.mouse.set_visible(False)
        #creates screen
        self.screen = pg.display.set_mode(RES)
        #frame rate
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        
    def new_game(self):
        #creates instance of map class
        self.map = Map(self)
        #creates instance of player class
        self.player = Player(self)
        #create instance of object renderer class
        self.object_renderer = ObjectRenderer(self)
        #create instance of raycasting class
        self.raycasting = RayCasting(self)
        #create instance of sprite object class
        self.static_sprite = SpriteObject(self)

    #updates screen
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    #draws screen
    def draw(self):
        #self.screen.fill('black') used only when background textures arent set
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    #exiting game event
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #main game loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
          

#creates instance of game and calls main loop "run method"
if __name__=='__main__':
    
    game = Game()
    game.run()