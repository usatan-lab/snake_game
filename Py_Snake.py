import pygame
import time
import random

pygame.init()

# 色の定義
white = (255, 255, 255)
yellow = (255, 255, 103)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
wall_color = (255, 0, 0)  # 壁の色を赤色に設定

# 画面の大きさ
dis_width = 800
dis_height = 600

# 蛇のサイズ
snake_block = 10
initial_speed = 10

# 画面の設定
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 45)
score_font = pygame.font.SysFont(None, 35)

def draw_walls():
    pygame.draw.rect(dis, wall_color, [0, 0, dis_width, snake_block])  # 上の壁
    pygame.draw.rect(dis, wall_color, [0, 0, snake_block, dis_height])  # 左の壁
    pygame.draw.rect(dis, wall_color, [0, dis_height - snake_block, dis_width, snake_block])  # 下の壁
    pygame.draw.rect(dis, wall_color, [dis_width - snake_block, 0, snake_block, dis_height])  # 右の壁

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def your_score(score):
    value = score_font.render('Your Score:'+ str(score),True,black)
    dis.blit(value,[0,0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    snake_speed = initial_speed
    score = 0
    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width - snake_block or x1 < snake_block or y1 >= dis_height - snake_block or y1 < snake_block:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        draw_walls()  # 壁を描画
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10
            snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
