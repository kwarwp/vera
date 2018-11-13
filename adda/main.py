# vera.adda.main.py
from browser import window
Phaser = window.Phaser
class Main:
    def __init__(self):
        self.config = {
              type: Phaser.AUTO,
              width: 800,
              height: 600,
              physics: {
                        default: 'arcade',
                        arcade: {
                                 gravity: { y: 200 }
                                 }
                        },
              scene: {
                      preload: preload,
                      create: create
                      }
              };

        self.game = Phaser.Game.new(self.config)
    def preload (self):
        this = self.game
        this.load.setBaseURL('http://labs.phaser.io')

        this.load.image('sky', 'assets/skies/space3.png')
        this.load.image('logo', 'assets/sprites/phaser3-logo.png')
        this.load.image('red', 'assets/particles/red.png')

    def create (self):
        this = self.game
        this.add.image(400, 300, 'sky');

        particles = this.add.particles('red');

        emitter = particles.createEmitter({
                                               speed: 100,
                                               scale: { start: 1, end: 0 },
                                               blendMode: 'ADD'
                                               });

        logo = this.physics.add.image(400, 100, 'logo');

        logo.setVelocity(100, 200);
        logo.setBounce(1, 1);
        logo.setCollideWorldBounds(true);

        emitter.startFollow(logo);
