import pygame as pg
#empty space defined by _ false value
#digits will be walls
_ = False

mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,3,3,3,3,_,_,_,3,3,3,_,_,1],
    [1,_,_,_,_,_,3,_,_,_,_,_,3,_,_,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,3,_,_,_,_,_,3,_,_,1,1,1,1,1,1,1,_,1],
    [1,_,_,3,3,3,3,_,_,_,_,_,_,_,_,1,1,1,1,1,1,1,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1,1,1,1,1,1,1,_,1],
    [1,_,_,4,_,_,_,4,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

#map class gets instance of game class as input to the constructor - mini map and world map are attributes
class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

        #world map obtaine through method, 
        # iterating over array and write coordinates 
        # of elements with only numeric values to dict
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    #test method to display map on screen
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
        for pos in self.world_map]