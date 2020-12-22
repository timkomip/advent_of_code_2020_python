class Map:
    def __init__(self, lines):
        self.lines = [line.strip() for line in lines]
        self.width = len(self.lines[0])
        self.height = len(self.lines)
    
    def get(self, x, y):
        row = self.lines[y]

        return row[x % self.width]
    
    def is_tree(self, x, y):
        return self.get(x,y) == "#"


class Marker:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map
        self.trees_encountered = set()

        self.record_location()
    
    def move(self, x, y):
        self.x += x
        self.y = min(self.map.height - 1, self.y + y)
        self.record_location()

    def record_location(self):
        if self.map.is_tree(self.x, self.y):
            self.trees_encountered.add((self.x, self.y))

    @property
    def at_bottom(self):
        return self.y == self.map.height - 1

    @property 
    def pos(self):
        return (self.x, self.y)

lines = []
with open('input.txt') as f:
    lines = f.readlines()

forest_map = Map(lines)
marker = Marker(0,0, forest_map)

while True:
    if marker.at_bottom:
        break
    marker.move(3, 1)

print(f'Trees encountered: {len(marker.trees_encountered)}')