# vera.samantha.main.py
from browser import window
PHASER = window.Phaser
 
class Main:
    def __init__(self):
        self.game = None
        self.gameConfig = dict(
        thpe= PHASER.CANVAS,
        width= 800,
        height= 800,
        scene= ["playGame"]
    )
    def resize(self):
        window.resize();
    def main(self):
        game = new Phaser.Game(self.gameConfig);
        window.focus()
        window.addEventListener("resize", self.resize, False);
        
        
if __name__ == "__main__"
    Main().main()