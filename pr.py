import json, sys

CHARS = [' ', '░', '▒', '▓', '█']

def preview(grid_json: str):
    grid = json.loads(grid_json)
    rows = len(grid[0])
    for y in range(rows):
        line = ''
        for col in grid:
            lvl = col[y] if y < len(col) else 0
            line += CHARS[min(lvl, 4)] * 2
        print(line)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        preview(sys.argv[1])
    else:
        print('Usage: python pr.py \'[[0,1,2],[3,4,0]]\'')
