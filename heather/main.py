# vera.heather.main.py
# vera.adda.main.py
from browser import window, doc, alert
from javascript import this as _this
Phaser = window.Phaser
DUDE = "IiClU5D.png"
BOMB = "8nVPuac.png"
PLAT = "fI4fviI.png"
SKY = "qkC2BMI.png"
STAR = "yS0o6qt.png"
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
                                 'gravity': { 'y': 300 },
                                 'debug': False
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
        player = self.player
        if (self.cursors.left.isDown):
            player.setVelocityX(-160);

            player.anims.play('left', True);
        elif (self.cursors.right.isDown):
            player.setVelocityX(160);

            player.anims.play('right', True);
        else:
            player.setVelocityX(0);

            player.anims.play('turn');

        if (self.cursors.up.isDown and player.body.touching.down):
            player.setVelocityY(-330);

    def create (self, this):
        this.add.image(400, 300, 'sky')
        this.add.image(400, 300, 'star')
        platforms = this.physics.add.staticGroup()

        platforms.create(400, 568, 'ground').setScale(2).refreshBody()

        platforms.create(600, 400, 'ground')
        platforms.create(50, 250, 'ground')
        platforms.create(750, 220, 'ground')
        self.player = player = this.physics.add.sprite(100, 450, 'dude');

        player.setBounce(0.2)
        player.setCollideWorldBounds(True)
        this.physics.add.collider(player, platforms);
        this.anims.create({
            'key': 'left',
            'frames': this.anims.generateFrameNumbers('dude', { 'start': 0, 'end': 3 }),
            'frameRate': 10,
            'repeat': -1
        });

        this.anims.create({
            'key': 'turn',
            'frames': [ { 'key': 'dude', 'frame': 4 } ],
            'frameRate': 20
        });

        this.anims.create({
            'key': 'right',
            'frames': this.anims.generateFrameNumbers('dude', { 'start': 5, 'end': 8 }),
            'frameRate': 10,
            'repeat': -1
        });
        self.cursors = this.input.keyboard.createCursorKeys();
        stars = this.physics.add.group({
            'key': 'star',
            'repeat': 11,
            'setXY': { 'x': 12, 'y': 0, 'stepX': 70 }
        });
        this.physics.add.collider(stars, platforms);
        self.score=0
        self.scoreText = this.add.text(16, 16, 'score: 0', { 'fontSize': '32px', 'fill': '#000' });
        def collectStar (player, star):
            star.disableBody(True, True);
            self.score += 10;
            self.scoreText.setText('Score: ' + self.score);


        #As well as doing this we will also check to see if the player overlaps with a star or not:

        this.physics.add.overlap(player, stars, collectStar, None, this);
        def iterate(child, _):

            child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));
        

        stars.children.iterate(iterate);



if __name__ == "__main__":
    Main()