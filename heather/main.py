# vera.heather.main.py
# vera.adda.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = window.Phaser
DUDE = "IiClU5D.png"
BOMB = "8nVPuac.png"
PLAT = "fI4fviI.png"
SKY = "qkC2BMI.png"
STAR = "yS0o6qt.png
class Main:
    def __init__(self):
        doc["pydiv"].html = ""
        def preload():
            
            self.preload(_this())
        def create(a):
            self.create(_this())
        self.config = dict(
              type= Phaser.AUTO,
              width= 800,
              height= 600,
              parent= "pydiv",
              physics= {
                        'default': 'arcade',
                        'arcade': {
                                 'gravity': { 'y': 200 }
                                 }
                        },
              scene= {
                      'preload': lambda *_: self.preload(_this()),
                      'create': lambda *_: self.create(_this()),
                      'update': lambda *_: self.update(_this())
                      }
              )

        self.game = Phaser.Game.new(self.config)
        window._game = self.game
    def preload (self, this):
        this.load.setBaseURL('https://i.imgur.com/')
        this.load.image('sky', SKY)
        this.load.image('ground', PLAT)
        this.load.image('star', STAR)
        this.load.image('bomb', BOMB)
        this.load.spritesheet('dude',  DUDE, { 'frameWidth': 32, 'frameHeight': 48 })

    def update (self, _self):
        pass

    def create (self, this):
        this.add.image(400, 300, 'sky')
        this.add.image(400, 300, 'star')


if __name__ == "__main__":
    Main()