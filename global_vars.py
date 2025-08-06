import pygame, chess

LIGHT_COLOR = pygame.Color('#EEEED5')
DARK_COLOR = pygame.Color('#7D945D')
LABEL_COLOR = pygame.Color('#A6A695')
BORDER_COLOR = pygame.Color('#53534A')
L_SELECT_COLOR = pygame.Color(196, 97, 109)
D_SELECT_COLOR = pygame.Color(110, 153, 192)
LINE_COLOR = pygame.Color('#53534A')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

TILE_COUNT = 8
LABEL_SIZE = 25
BOARD_SIZE = 735
BORDER_SIZE = 2
LINE_SIZE = -1
PIECE_SCALE = 0.9
SELECT_SCALE = 0.8
MOVE_SCALE = 0.5

TILE_SIZE = BOARD_SIZE / TILE_COUNT
TILE_DIMENSIONS = (TILE_SIZE, TILE_SIZE)
BOARD_DIMENSIONS = (BOARD_SIZE, BOARD_SIZE)
BOARD = chess.Board(chess.STARTING_FEN)

FLAGS = pygame.RESIZABLE | pygame.SCALED
SCREEN_SIZE = BOARD_SIZE + LABEL_SIZE
SCREEN_DIMENSIONS = (SCREEN_SIZE, SCREEN_SIZE)
SCREEN = pygame.display.set_mode(SCREEN_DIMENSIONS, FLAGS)
CLOCK = pygame.time.Clock()

