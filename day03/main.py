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
    def __init__(self, init_x, init_y, map):
        self.init_x = init_x
        self.init_y = init_y
        self.map = map
        self.reset()
    
    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
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

def count_trees_to_corner(map, slope):
    marker = Marker(0,0, map)
    while True:
        if marker.at_bottom:
            break
        marker.move(*slope)
    return len(marker.trees_encountered)

lines = []
with open('input.txt') as f:
    lines = f.readlines()

forest_map = Map(lines)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

result = 1
for slope in slopes:
    count = count_trees_to_corner(forest_map, slope)
    print(f'Trees encountered for slope {slope}: {count}')
    result *= count

print(f"Product of tree counts: {result}")