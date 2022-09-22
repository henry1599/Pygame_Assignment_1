SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

TARGET_FPS = 60

GAME_NAME = "POP BALL POP"
GAME_NAME_TEXT_SIZE = 100
GAME_NAME_COLOR = (255, 255, 255)
GAME_NAME_COLOR_OUTLINE = (0, 0, 0)

START_TITLE = "Let's Go"
CREDIT_TITLE = "Credits"
QUIT_TITLE = "Quit"
TITLE_TEXT_SIZE = 50
TITLE_COLOR = (255, 255, 255)


# * CREDIT
DEVELOPERS_NAME = [
    "Nguyễn Chí Trung",
    "Phan Đinh Minh Toàn",
    "Đoàn Tây Đô",
    "Lê Trung Hiếu"
]
DEVELOPERS_NAME_TEXT_SIZE = 50
DEVELOPERS_NAME_TEXT_COLOR  = (255, 255, 255)

VOLUME_TEXT = "Volume : "
VOLUME_TEXT_SIZE = 80

ON_TEXT = "ON"
TOGGLE_TEXT_SIZE = 80
OFF_TEXT = "OFF"

BACK_TEXT = "Back"
BACK_TEXT_SIZE = 80

BLACK_COLOR = (0, 0, 0, 255)
WHITE_COLOR = (255, 255, 255, 255)
BALL_RAW_COLOR = [BLACK_COLOR, WHITE_COLOR]
MINE_RAW_COLOR = [BLACK_COLOR, (255, 153, 0), (255, 51, 0), (255, 80, 80)]

ROTATE_FACTOR = [-1, 1]

SCORE_TEXT = "Score : "
SCORE_TEXT_COLOR = (255, 255, 255)
SCORE_TEXT_SIZE = 50
SCORE_POSITION = (25, 25)

FONT_PATH  = '../_fonts/Dosis/Dosis-Bold.ttf'

CURSOR_PATH = '../_assets/Cursors/Normal.png'
CURSOR_SIZE = (285, 285)

BACKGROUND_PATH = '../_assets/Backgrounds/Background 6.png'
BACKGROUND_WIDTH = 1300
BACKGROUND_HEIGHT = 866

SETTING_ICON_PATH = '../_assets/Setting/Setting.png'
SETTING_ICON_SIZE = (2048, 2048)

GRID_PATH = '../_assets/Backgrounds/Grid_4x2.png'
GRID_WIDTH = 878
GRID_HEIGHT = 456
GRID_SIZE = (GRID_WIDTH, GRID_HEIGHT)
GRIDS_POS = [
    (319, 252),
    (530, 252),
    (741, 252),
    (952, 252),
    (319, 464),
    (530, 464),
    (741, 464),
    (952, 464)
]

SOUND_THEME = '../_sounds/Theme.wav'
BEGIN_THEME = '../_sounds/Begin.wav'
SOUND_CLICK_THE_BALL = '../_sounds/Click_the_ball.wav'
SOUND_CLICK_NOTHING = '../_sounds/Click_nothing.wav'
SOUND_CLICK_THE_MINE = '../_sounds/Bomb.wav'

BALL_PATH = '../_assets/Enemies/Balls/ball.png'
MINE_PATH = '../_assets/Enemies/Mines/mine.png'
MINE_WIDTH = 512
MINE_HEIGHT = 512
BALL_WIDTH = 500
BALL_HEIGHT = 500
MINE_SIZE = (MINE_WIDTH, MINE_HEIGHT)
BALL_SIZE = (BALL_WIDTH, BALL_HEIGHT)

# Current score : (ball each turn, ball life time)
LEVEL_CONFIG = {
    10 : (1, 3000),
    20 : (2, 2500),
    50 : (2, 2000),
    70 : (3, 2000),
    85 : (3, 1500),
    100 : (4, 1500),
    150 : (4, 1000),
    200 : (5, 1000),
    500 : (6, 800),
}

BALL_EACH_TURN = LEVEL_CONFIG[10][0]
BALL_SPAWN_INTERVAL = 1000
BALL_LIFE_TIME = LEVEL_CONFIG[10][1]
