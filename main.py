import copy
import pygame
import sys
from logic import State, square
from player import Player

pygame.init()

# إعداد المصفوفات (الرقع)
array1 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(3, True), square(0, False),
    square(0, False), square(3, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False)
]
array2 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(3, True), square(1, False),
    square(0, False), square(1, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(3, False), square(0, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(4, True), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(4, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
]
array3 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(0, False), square(2, True),
    square(3, True), square(4, True), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(0, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(1, False), square(1, False),
    square(1, False), square(2, False), square(0, False),
    square(3, False), square(4, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
]

# دالة لاختيار اللون بناءً على الرقم
def get_color_by_num(num):
    if num == 0:
        return (255, 255, 255)  # أبيض للخلايا الفارغة
    elif num == 1:
        return (100, 100, 100)  # رمادي
    elif num == 2:
        return (0, 255, 0)      # أخضر
    elif num == 3:
        return (0, 0, 255)      # أزرق
    elif num == 4:
        return (255, 0, 0)      # أحمر
    else:
        return (128, 128, 128)  # لون افتراضي

# إعداد اللعبة
boards = [array1, array2, array3]
current_board_index = 0

square_size = 40  # يمكن تعديل الحجم حسب الحاجة
num_columns = 6
num_rows = (len(boards[0]) + num_columns - 1) // num_columns

# تحديد حجم الشاشة بناءً على عدد الأعمدة والصفوف
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Board")

# وظيفة عرض اللوحة
def draw_board(current_board):
    screen.fill((255, 255, 255))  # الخلفية بيضاء
    for index, square in enumerate(current_board):
        x = (index % num_columns) * square_size
        y = (index // num_columns) * square_size
        color = get_color_by_num(square.num)
        pygame.draw.rect(screen, color, (x, y, square_size, square_size))

        # إضافة النص
        font = pygame.font.Font(None, 36)
        text = font.render(str(square.num), True, (255, 255, 255) if square.num != 0 else (0, 0, 0))
        screen.blit(text, (x + square_size // 3, y + square_size // 3))

# دالة لتحديد مربعات قابلة للحركة
def initialize_player(current_board):
    movable_squares = [index for index, square in enumerate(current_board) if square.is_movable]
    return Player(current_board, movable_squares) if movable_squares else None

# حلقة اللعبة الرئيسية
running = True
while running:
  current_board =boards[current_board_index]
  player_instance = initialize_player(current_board) 
    
    # عرض الرقعة قبل بدء اللعبة
  draw_board(current_board)
  pygame.display.flip()  # تحديث الشاشة لعرض الرقعة

    # التحقق من الفوز عند البدء
  while player_instance and player_instance.game():
        draw_board(current_board)
        pygame.display.flip()
        
        # الانتقال للرقعة التالية إذا انتهت الحركات
        current_board_index += 1
        if current_board_index >= len(boards):  # إذا انتهت جميع الرقعات
            print("لقد انتهيت من جميع الرقعات!")
            running = False
            break
        else:
            current_board = boards[current_board_index]
            player_instance = initialize_player(current_board)
            draw_board(current_board)
            pygame.display.flip()
    # التحقق من أحداث pygame
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
            break

pygame.quit()
sys.exit()
