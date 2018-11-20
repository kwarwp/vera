# vera.braser.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = window.Phaser
PHYSICS = dict(default='arcade', arcade=dict(gravity=dict(y=200)))
class Braser:
    game = None
    subscribers = []
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
