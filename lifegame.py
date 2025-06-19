from typing import Literal

SupportedIndexOfRule = list[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]]

def GenerateGosperGliderGun(size: int = 50) -> list[list[bool]]:
    rs = [[False for _ in range(size)] for _ in range(size)]
    if size < 36:
        raise IndexError("I can't put Gosper Glider Gun into this grid (Size is lower than 36)")
    rs[0][24] = True
    for i in [22, 24]:
        rs[1][i] = True
    for i in [12, 13, 20, 21, 34, 35]:
        rs[2][i] = True
    for i in [11, 15, 20, 21, 34, 35]:
        rs[3][i] = True
    for i in [0, 1, 10, 16, 20, 21]:
        rs[4][i] = True
    for i in [0, 1, 10, 14, 16, 17, 22, 24]:
        rs[5][i] = True
    for i in [10, 16, 24]:
        rs[6][i] = True
    for i in [11, 15]:
        rs[7][i] = True
    for i in [12, 13]:
        rs[8][i] = True
    return rs

def NextGeneration(grid: list[list[bool]] | list[list[Literal[0, 1]]], birth: SupportedIndexOfRule = [3], survive: SupportedIndexOfRule = [2, 3]) -> list:
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new grid
    tng = [[False for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            # Calculate 8 neighbors
            nb = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx == 0 and dy == 0) \
                    or (i == 0 and dx == -1) \
                    or (j == 0 and dy == -1) \
                    or (i == rows-1 and dx == 1) \
                    or (j == cols-1 and dy == 1):
                        continue
                    x = (i + dx) % rows
                    y = (j + dy) % cols
                    nb += int(grid[x][y])
            
            # Apply the rule (B3S23)
            if grid[i][j]:
                tng[i][j] = nb in survive
            else:
                tng[i][j] = nb in birth
                
    return tng

# Set their other name
gggg = GenerateGosperGliderGun
ng = NextGeneration

def main():
    import time, os
    gosper = gggg(36)
    os.system("cls")
    for _ in range(100):
        gosper = ng(ng(ng(ng(gosper))))
    
        for row in gosper:
            print(" ".join([str("#" if cell else "-") for cell in row]))
        time.sleep(0.2)
        os.system("cls")

if __name__ == "__main__":
    main()
