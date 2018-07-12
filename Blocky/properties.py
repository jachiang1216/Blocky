# Global Settings and List of Levels
# Game Settings
TITLE = "Blocky!"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT = 'times new roman'
SPRITESHEET = 'items_spritesheet.png'

# Player Properties
ACC = 0.5
FRICTION = -0.12
JUMP = 15

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
TURQUOISE = (0, 255, 196)
WHITE = (255, 255, 255)
PINK = (255, 0, 255)

# Level List
# Level 1

Platforms_4 = [(0, 590, 200, 10), (60, 500, 145, 10), (0, 400, 100, 10), (50, 300, 160, 10), (150, 210, 200, 10),
             (300, 140, 200, 10), (270, 400, 230, 10), (650, 350, 150, 10)]
Walls_4 = [(200, 300, 10, 300)]
PowerUp_4 = ()
Win_Condition_4 = (750, 320, 30, 30)
Player_4 = (150, 550)


Platforms_2 = [(0, 590, 100, 10), (170, 590, 50, 10), (290, 590, 50, 10), (410, 590, 50, 10), (530, 550, 50, 10),
             (650, 470, 200, 10), (350, 400, 200, 10), (290, 300, 50, 10), (240, 250, 50, 10), (190, 200, 50, 10),
             (0, 150, 160, 10), (150, 90, 10, 10)]
Walls_2 = [(150, 0, 10, 100)]
PowerUp_2 = ()
Win_Condition_2 = (50, 50, 30, 30)
Player_2 = (50, 550)

Platforms_3 = [(750, 100, 50, 10), (600, 550, 100, 10), (400, 300, 100, 10), (250, 250, 100, 10), (250, 350, 100, 10),
               (50, 70, 70, 10), (0, 400, 60, 10), (0, 270, 60, 10), (0, 550, 150, 10), (60, 465, 55, 10), (60, 350, 55, 10)]
Walls_3 = [(110, 75, 10, 400)]
PowerUp_3 = [(610, 520), (260, 220)]
Win_Condition_3 = (40, 300, 30, 30)
Player_3 = (750, 30)

Platforms_1 = [(750, 100, 50, 10), (600, 550, 100, 10), (400, 300, 100, 10), (250, 250, 100, 10), (250, 400, 100, 10),
               (50, 70, 70, 10), (0, 400, 60, 10), (0, 270, 60, 10), (0, 550, 150, 10), (60, 465, 55, 10), (60, 350, 110, 10)]
Walls_1 = [(110, 75, 10, 400)]
PowerUp_1 = [(610, 520), (260, 220)]
Win_Condition_1 = (40, 300, 30, 30)
Player_1 = (750, 30)

# Array Containing Levels
Win_Condition_Array = [Win_Condition_1, Win_Condition_2, Win_Condition_3, Win_Condition_4]
Platforms_Array = [Platforms_1, Platforms_2, Platforms_3, Platforms_4]
Walls_Array = [Walls_1, Walls_2, Walls_3, Walls_4]
Player_Array = [Player_1, Player_2, Player_3, Player_4]
PowerUp_Array = [PowerUp_1, PowerUp_2, PowerUp_3, PowerUp_4]
