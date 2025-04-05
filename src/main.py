import pygame
import sys

# ========== 사용자 입력 ==========
try:
    a = float(input("계수 a 값을 입력하세요 (예: 1, -2.5 등): "))
except ValueError:
    print("숫자를 입력해주세요.")
    sys.exit()

mode = input("정비례(y=ax)는 p / 반비례(y=a/x)는 i 를 입력하세요: ").lower()
if mode not in ['p', 'i']:
    print("잘못된 입력입니다. 'p' 또는 'i'만 입력하세요.")
    sys.exit()

# ========== pygame 설정 ==========
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("그래프 시각화")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (255, 100, 100)

origin_x = WIDTH // 2
origin_y = HEIGHT // 2
scale = 40 
def draw_axes():
    pygame.draw.line(screen, BLACK, (0, origin_y), (WIDTH, origin_y), 2)  # x축
    pygame.draw.line(screen, BLACK, (origin_x, 0), (origin_x, HEIGHT), 2)  # y축

def draw_proportional(a):
    for x in range(-200, 200):
        real_x1 = x / 20
        real_x2 = (x + 1) / 20
        y1 = a * real_x1
        y2 = a * real_x2

        x1 = origin_x + int(real_x1 * scale)
        y1 = origin_y - int(y1 * scale)
        x2 = origin_x + int(real_x2 * scale)
        y2 = origin_y - int(y2 * scale)

        pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 2)

def draw_inverse(a):
    for x in range(-200, 200):
        real_x1 = x / 20
        real_x2 = (x + 1) / 20
        if real_x1 == 0 or real_x2 == 0:
            continue
        y1 = a / real_x1
        y2 = a / real_x2

        x1 = origin_x + int(real_x1 * scale)
        y1 = origin_y - int(y1 * scale)
        x2 = origin_x + int(real_x2 * scale)
        y2 = origin_y - int(y2 * scale)

        pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 2)

# ========== 메인 루프 ==========
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    draw_axes()

    if mode == 'p':
        draw_proportional(a)
    elif mode == 'i':
        draw_inverse(a)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        a += 0.05
    if keys[pygame.K_DOWN]:
        a -= 0.05

    pygame.display.set_caption(f"{'정비례' if mode=='p' else '반비례'} 그래프 | a = {a:.2f}")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
