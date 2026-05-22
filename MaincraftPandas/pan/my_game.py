from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.load_land('land.txt)')
        base.camLens.setFov(90)

game = Game()
game.run()