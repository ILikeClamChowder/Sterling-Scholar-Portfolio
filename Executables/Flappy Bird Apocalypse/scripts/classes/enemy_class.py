from scripts.settings import *
from scripts.classes.bullet_class import Bullet

class Enemy(pg.sprite.Sprite):

    def __init__(self, game):
        super(Enemy, self).__init__()
        self.game=game
        self.image = pg.Surface([10*tileDivide,10*tileDivide])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed = 10


    def update(self):

        self.move()

        self.attack()


    def attack(self):
        bullet = Bullet()
        bullet.add(self.game.enemyBullets)
        bullet.add(self.game.all_sprites)

    def move(self):

        pass


