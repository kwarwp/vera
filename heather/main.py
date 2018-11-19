# vera.heather.main.py
# vera.adda.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = window.Phaser
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
        this.load.setBaseURL('http://labs.phaser.io')
        this.load.image('sky', 'assets/sky.png')
        this.load.image('ground', 'assets/platform.png')
        this.load.image('star', 'assets/star.png')
        this.load.image('bomb', 'assets/bomb.png')
        this.load.spritesheet('dude',  'assets/dude.png', { 'frameWidth': 32, 'frameHeight': 48 })

    def update (self, _self):
        pass

    def create (self, this):
        this.add.image(400, 300, 'sky')
        this.add.image(400, 300, 'star')


if __name__ == "__main__":
    Main()