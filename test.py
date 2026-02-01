WIDTH=20
HEIGHT=15

def gen_maze():
    maze = [
    [ {'north': True, 'east': True, 'south': True, 'west': True} for col in range(width) ]
    for row in range(height)
    ]