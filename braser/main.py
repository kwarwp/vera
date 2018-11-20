# vera.braser.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = PHASER = window.Phaser
class Braser:
    game = None
    subscribers = []
    def __init__(self, width=800, height=600, subscribers=[], parent="pydiv", mode=Phaser.AUTO):
        doc["pydiv"].html = ""
        [self.subscribe(subscriber) for subscriber in subscribers]
        self.config = dict(
              type= Phaser.AUTO,
              width= 800,
              height= 600,
              parent= "pydiv",
              physics= {
                        'default': 'arcade',
                        'arcade': {
                                 'gravity': { 'y': 300 },
                                 'debug': False
                                 }
                        },
              scene= {
                      'preload': lambda *_: self._preload(_this()),
                      'create': lambda *_: self._create(_this()),
                      'update': lambda *_: self._update(_this())
                      }
              )

        Braser.game = Phaser.Game.new(self.config) if not Braser.game else Braser.game

    def subscribe(self, subscriber):
        """
        Subscribe elements for game loop.

        :param subscriber:
        """
        Braser.subscribers.append(subscriber)
        
    def _preload (self, this):
        self.game = this
        self.preload()
        for subscriber in Braser.subscribers:
            subscriber.preload() if hasattr(subscriber, 'preload') else None

    def _create (self, this):
        self.game = this
        self.create()
        for subscriber in Braser.subscribers:
            subscriber.create() if hasattr(subscriber, 'create') else None

    def _update(self, this):
        """
        Update element.

        """
        self.update()
        for subscriber in Braser.subscribers:
            subscriber.update() if hasattr(subscriber, 'update') else None
        
    def preload (self, *_):
        pass

    def create (self, *_):
        pass

    def update(self, *_):
        pass


class Main(Braser):
    """
    Brython object-oriented  wrapper for js Phaser.

    :param x: Canvas width.
    :param y: Canvas height.
    :param mode: Canvas mode.
    :param name: Game name.
    :param keyargs: Extra arguments
    """

    def __init__(self, x=800, y=600, mode=None, name="pydiv", **kwargs):
        super().__init__()

    def preload(self, *_):
        """
        Preload element.

        """
        this = self.game
        this.load.setBaseURL('http://labs.phaser.io')

        this.load.image('sky', 'assets/skies/space3.png')
        this.load.image('logo', 'assets/sprites/phaser3-logo.png')
        self.game.load.image('red', 'assets/particles/red.png')

    def create(self, *_):
        """
        Create element.

        """
        this = self.game
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
