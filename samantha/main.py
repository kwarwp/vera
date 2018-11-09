# vera.samantha.main.py
from browser import window, document
PHASER = window.Phaser

class PlayGame (PHASER.Scene):
    def __init__(self):
        self.game = None
        self.gameOptions = None
        super("PlayGame");

    def preload(self):
        self.load.image("bigcircle", "bigcircle.png");
        self.load.image("player", "player.png");
    }
    def create(self):
        self.bigCircle = self.add.sprite(self.game.config.width / 2, self.game.config.height / 2, "bigcircle");
        self.bigCircle.displayWidth = gameOptions.bigCircleRadius;
        self.bigCircle.displayHeight = gameOptions.bigCircleRadius;
        self.player = this.add.sprite(self.game.config.width / 2, (self.game.config.height - self.gameOptions.bigCircleRadius - self.gameOptions.playerRadius) / 2, "player");
        self.player.displayWidth = self.gameOptions.playerRadius;
        self.player.displayHeight = self.gameOptions.playerRadius;
        self.player.currentAngle = -90;
        self.player.jumpOffset = 0;
        self.player.jumps = 0;
        self.player.jumpForce = 0;
        '''
        self.input.on("pointerdown", function(e){
            if(this.player.jumps < 2){
                this.player.jumps ++;
                this.player.jumpForce = gameOptions.jumpForce[this.player.jumps - 1];
            }
        }, this);
        '''

    def update(self):
        if(self.player.jumps > 0):
            self.player.jumpOffset += self.player.jumpForce;
            self.player.jumpForce -= self.gameOptions.worldGravity;
            if(self.player.jumpOffset < 0):
                self.player.jumpOffset = 0;
                self.player.jumps = 0;
                self.player.jumpForce = 0;
        self.player.currentAngle = PHASER.Math.Angle.WrapDegrees(self.player.currentAngle + self.gameOptions.playerSpeed);
        radians = PHASER.Math.DegToRad(self.player.currentAngle);
        distanceFromCenter = (self.gameOptions.bigCircleRadius + self.gameOptions.playerRadius) / 2 + self.player.jumpOffset;
        self.player.x = self.bigCircle.x + distanceFromCenter * Math.cos(radians);
        self.player.y = self.bigCircle.y + distanceFromCenter * Math.sin(radians);
        revolutions = self.gameOptions.bigCircleRadius / self.gameOptions.playerRadius + 1;
        self.player.angle = self.player.currentAngle * revolutions;


class Main:
    def __init__(self):
        self.game = None
        self.gameConfig = dict(
        thpe= PHASER.CANVAS,
        width= 800,
        height= 800,
        scene= [PlayGame]
    )
    def resize(self):
            canvas = document.querySelector("canvas");
            windowWidth = window.innerWidth;
            windowHeight = window.innerHeight;
            windowRatio = windowWidth / windowHeight;
            gameRatio = self.game.config.width / self.game.config.height;
        if(windowRatio < gameRatio):
            canvas.style.width = windowWidth + "px";
            canvas.style.height = (windowWidth / gameRatio) + "px";
        else:
            canvas.style.width = (windowHeight * gameRatio) + "px";
            canvas.style.height = windowHeight + "px";
    def main(self):
        self.game = PHASER.Game(self.gameConfig).new()
        window.focus()
        window.addEventListener("resize", self.resize, False)
        
        
if __name__ == "__main__":
    Main().main()