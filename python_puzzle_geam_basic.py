import pygame
import random

# 初期化
pygame.init()

# 画面サイズ
SIZE = 400
TILE_SIZE = SIZE // 4
FONT = pygame.font.Font(None, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# タイルの初期配置
def create_board():
    numbers = list(range(1, 16)) + [None]
    random.shuffle(numbers)
    return [numbers[i:i+4] for i in range(0, 16, 4)]

board = create_board()

# 空白の座標を取得
def get_empty():
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile is None:
                return x, y

# タイルを移動
def move_tile(x, y):
    ex, ey = get_empty()
    if (abs(x - ex) == 1 and y == ey) or (abs(y - ey) == 1 and x == ex):
        board[ey][ex], board[y][x] = board[y][x], board[ey][ex]

# 描画
def draw_board(screen):
    screen.fill(WHITE)
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile is not None:
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLACK, rect)
                text = FONT.render(str(tile), True, WHITE)
                screen.blit(text, (x * TILE_SIZE + 20, y * TILE_SIZE + 20))
    pygame.display.flip()

# メインループ
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("15 Puzzle")
running = True

while running:
    draw_board(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
            move_tile(x, y)

pygame.quit()
