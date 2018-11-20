# vera.braser.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = window.Phaser
PHYSICS = dict(default='arcade', arcade=dict(gravity=dict(y=200))
class Main:
    def __init__(self, width=800, height=600, parent="pydiv", mode=Phaser.AUTO):
        scene= {
                    'preload': lambda *_: self._preload(_this()),
                    'create': lambda *_: self._create(_this()),
                    'update': lambda *_: self._update(_this())
                    }
        doc["pydiv"].html = ""
        self.config = dict(
              type=mode,
              width=width,
              height=height,
              parent=parent,
              physics=PHYSICS,
              scene=scene
              )

        self.game = Phaser.Game.new(self.config)
        window._game = self.game
    def _preload (self, _self):
        this = _self
        if this not in self.__base__:
            self.__base__.append(this)
        this.load.setBaseURL('http://labs.phaser.io')

        this.load.image('sky', 'assets/skies/space3.png')
        this.load.image('logo', 'assets/sprites/phaser3-logo.png')
        self.load.image('red', 'assets/particles/red.png')

    def create (self, _self):
        this = _self
        # this = self.game
        this.add.image(400, 300, 'sky');
        particles = this.add.particles('red');

        emitter = particles.createEmitter({
                                               'speed': 100,
                                               'scale': { 'start': 1, 'end': 0 },
                                               'blendMode': 'ADD'
                                               });

        logo = this.physics.add.image(400, 100, 'logo');

        logo.setVelocity(100, 200);
        logo.setBounce(1, 1);
        logo.setCollideWorldBounds(True);

        emitter.startFollow(logo);

if __name__ == "__main__":
    Main()

PHASER = window.Phaser
BraserGame = PHASER.Game.new

class Braser:
    """
    Brython object-oriented  wrapper for js Phaser.

    :param x: Canvas width.
    :param y: Canvas height.
    :param mode: Canvas mode.
    :param name: Game name.
    :param keyargs: Extra arguments
    """
    PHASER = window.Phaser

    def __init__(self, x=800, y=600, mode=None, name="pydiv", **kwargs):
        mode = mode or PHASER.CANVAS
        self.game = BraserGame(x, y, mode, name,
                                {"preload": self.preload, "create": self.create, "update": self.update})
        self.subscribers = []

    def subscribe(self, subscriber):
        """
        Subscribe elements for game loop.

        :param subscriber:
        """
        self.subscribers.append(subscriber)

    def preload(self, *_):
        """
        Preload element.

        """
        for subscriber in self.subscribers:
            subscriber.preload()

    def create(self, *_):
        """
        Create element.

        """
        for subscriber in self.subscribers:
            subscriber.create()

    def update(self, *_):
        """
        Update element.

        """
        for subscriber in self.subscribers:
            subscriber.update()
