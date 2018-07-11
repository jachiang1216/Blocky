# Global Settings and List of Levels
# Game Settings
TITLE = "Blocky!"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT = 'times new roman'

# Player Properties
ACC = 0.5
FRICTION = -0.12
JUMP = 15

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
TURQUOISE = (0, 255, 196)
WHITE = (255, 255, 255)

# Level List
# Level 1

Platforms_1 = [(0, 590, 200, 10), (60, 500, 145, 10), (0, 400, 100, 10), (50, 300, 160, 10), (150, 210, 200, 10),
             (300, 140, 200, 10), (270, 400, 230, 10), (650, 350, 150, 10)]
Walls_1 = [(200, 300, 10, 300)]
Win_Condition_1 = (750, 320, 30, 30)
Player_1 = (150, 550)


Platforms_2 = [(0, 590, 100, 10), (170, 590, 50, 10), (290, 590, 50, 10), (410, 590, 50, 10), (530, 550, 50, 10),
             (650, 470, 200, 10), (350, 400, 200, 10), (290, 300, 50, 10), (240, 250, 50, 10), (190, 200, 50, 10),
             (0, 150, 160, 10), (150, 90, 10, 10)  ]
Walls_2 = [(150, 0, 10, 100)]
Win_Condition_2 = (50, 50, 30, 30)
Player_2 = (50, 550)

# Array Containing Levels
Win_Condition_Array = [Win_Condition_1, Win_Condition_2]
Platforms_Array = [Platforms_1, Platforms_2]
Walls_Array = [Walls_1, Walls_2]
Player_Array = [Player_1, Player_2]