import pygame  
import sys  
  
# 初始化pygame  
pygame.init()  
  
# 设置窗口大小和标题  
WIDTH, HEIGHT = 800, 600  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("弹球游戏")  
  
# 定义颜色  
WHITE = (255, 255, 255)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
  
# 设置球和挡板的速度  
ball_speed = [4, 4]  
paddle_speed = 5  
  
# 球的初始位置和尺寸  
ball_pos = [WIDTH // 2, HEIGHT - 30]  
ball_size = [20, 20]  
  
# 挡板的初始位置和尺寸  
paddle_pos = [WIDTH // 2, HEIGHT - 40]  
paddle_size = [100, 10]  
  
# 游戏主循环标志  
running = True  
  
while running:  
    # 处理事件队列  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
  
    # 获取键盘按键状态  
    keys = pygame.key.get_pressed()  
      
    # 根据按键状态移动挡板  
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:  
        paddle_pos[0] -= paddle_speed  
    if keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - paddle_size[0]:  
        paddle_pos[0] += paddle_speed  
  
    # 移动球  
    ball_pos[0] += ball_speed[0]  
    ball_pos[1] += ball_speed[1]  
  
    # 反弹检测  
    if ball_pos[0] < 0 or ball_pos[0] + ball_size[0] > WIDTH:  
        ball_speed[0] = -ball_speed[0]  
    if ball_pos[1] < 0 or ball_pos[1] + ball_size[1] > HEIGHT:  
        ball_speed[1] = -ball_speed[1]  
        # 可以在这里添加游戏结束的逻辑，比如显示“游戏结束”的文本  
  
    # 挡板与球碰撞检测  
    if (ball_pos[0] > paddle_pos[0] and  
        ball_pos[0] < paddle_pos[0] + paddle_size[0] and  
        ball_pos[1] + ball_size[1] > paddle_pos[1] and  
        ball_speed[1] > 0):  
        ball_speed[1] = -ball_speed[1]  
  
    # 绘制背景  
    WIN.fill(WHITE)  
  
    # 绘制球  
    pygame.draw.rect(WIN, RED, (ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]))  
  
    # 绘制挡板  
    pygame.draw.rect(WIN, GREEN, (paddle_pos[0], paddle_pos[1], paddle_size[0], paddle_size[1]))  
  
    # 更新显示  
    pygame.display.update()  
  
    # 控制帧率  
    pygame.time.Clock().tick(60)  
  
# 退出pygame  
pygame.quit()  
sys.exit()
