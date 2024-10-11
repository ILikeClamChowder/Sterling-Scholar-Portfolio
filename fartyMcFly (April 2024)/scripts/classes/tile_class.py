from scripts.settings import *


class Tile(pg.sprite.Sprite):

  def __init__(self, image, x, y, type):
    super(Tile, self).__init__()
    # pg.sprite.Sprite.__init__(self)
    self.image = pg.image.load(image)
    self.image = pg.transform.scale(self.image, (tileSize, tileSize))
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = x, y
    self.type = type
    self.killed=False

  def draw(self, surface):
    if not self.killed:
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap(pg.sprite.Sprite):

  def __init__(self, filename):
    super(TileMap, self).__init__()
    # pg.sprite.Sprite.__init__(self)
    self.start_x, self.start_y = 0, 0
    self.tiles = self.load_tiles(filename)
    self.map_surface = pg.Surface((self.map_w, self.map_h))
    self.map_surface.set_colorkey((0, 0, 0))
    self.load_map()

  def draw_map(self, surface):
    surface.blit(self.map_surface, (0, 0))

  def load_map(self):
    for tile in self.tiles:
      tile.draw(self.map_surface)

  def read_csv(self, filename):
    map = []
    with open(filename) as data:
      data = csv.reader(data, delimiter=',')
      for row in data:
        map.append(list(row))
    return map

  def load_tiles(self, filename):
    tiles = []
    map = self.read_csv(filename)
    x, y = 0, 0
    for row in map:
      x = 0
      for tile in row:
        #player
        if tile == "7":
          self.start_x, self.start_y = x * tileSize, y * tileSize

        #goal
        elif tile == "8":
          tiles.append(
              Tile('scripts/assets/placeHolder.jpg', x * tileSize, y * tileSize,
                   "goal"))

        #death things
        elif tile == "10":
          tiles.append(
              Tile('scripts/assets/tiles/10.png', x * tileSize, y * tileSize,
                   "kill"))
        elif tile == "11":
          tiles.append(
              Tile('scripts/assets/tiles/11.png', x * tileSize, y * tileSize,
                   "kill"))
        elif tile == "30":
          print("30 ong")
          tiles.append(
              Tile('scripts/assets/tiles/30.png', x * tileSize, y * tileSize,
                   "kill"))
        elif tile == "31":
          tiles.append(
              Tile('scripts/assets/tiles/31.png', x * tileSize, y * tileSize,
                   "kill"))

        #beans
        elif tile == "27":
          tiles.append(
              Tile('scripts/assets/tiles/27.png', x * tileSize, y * tileSize,
                   "beans"))

        #walls
        elif tile == "1":
          tiles.append(
              Tile('scripts/assets/tiles/1.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "3": # make it transparent
          tiles.append(
              Tile('scripts/assets/tiles/3.png', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "4":
          tiles.append(
              Tile('scripts/assets/tiles/4.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "5":
          tiles.append(
              Tile('scripts/assets/tiles/5.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "20":
          tiles.append(
              Tile('scripts/assets/tiles/20.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "22":
          tiles.append(
              Tile('scripts/assets/tiles/22.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "24":
          tiles.append(
              Tile('scripts/assets/tiles/24.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "25":
          tiles.append(
              Tile('scripts/assets/tiles/25.jpg', x * tileSize, y * tileSize,
                   "wall"))
        elif tile == "41":
          tiles.append(
              Tile('scripts/assets/tiles/41.jpg', x * tileSize, y * tileSize,
                   "wall"))

        #untouched walls
        elif tile == "0":
          tiles.append(
              Tile('scripts/assets/tiles/0.jpg', x * tileSize, y * tileSize,
                   ""))
        elif tile == "2":
          tiles.append(
              Tile('scripts/assets/tiles/2.jpg', x * tileSize, y * tileSize,
                   ""))
        elif tile == "21":
          tiles.append(
              Tile('scripts/assets/tiles/21.jpg', x * tileSize, y * tileSize,
                   ""))
        elif tile == "40":
          tiles.append(
              Tile('scripts/assets/tiles/40.jpg', x * tileSize, y * tileSize,
                   ""))
        elif tile == "42":
          tiles.append(
              Tile('scripts/assets/tiles/42.jpg', x * tileSize, y * tileSize,
                   ""))
        x += 1
      y += 1
    self.map_w, self.map_h, = x * tileSize, y * tileSize
    return tiles