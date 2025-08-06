# Import necessary modules
import global_vars as G
import display_gui as gui
import ai_algorithms as ai
import chess, pygame, sys

# Game Configuration
TEST_MODE = False
AI_DELAY = 1  # Delay in seconds for AI moves
WHITE_AI_DEPTH = -1  # Set to -1 for human player, or > 0 for AI
BLACK_AI_DEPTH = 3  # Set to -1 for human player, or > 0 for AI

# Initial board setup
STARTING_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
G.BOARD.set_board_fen(STARTING_FEN)
gui.draw_board()
selected_square = None
game_outcome = None

# Function to get AI move based on a specified depth
def get_ai_move(difficulty_level):
    """
    Determines the best AI move based on the difficulty level.

        difficulty_level (int): The AI's difficulty setting.
                                0: No move
                                1: Random move
                                2: Positional move
                                >2: Predictive move (minimax)
    """
    move = None
    if difficulty_level == 0:
        move = chess.Move.null()
    elif difficulty_level == 1:
        move = ai.select_random()
    elif difficulty_level == 2:
        move = ai.select_positional()
    elif difficulty_level > 2:
        move = ai.select_predictive(difficulty_level - 2)
    
    if move:
        ai.make_ai_move(move, AI_DELAY)
    
    return move

# Main game loop
while not game_outcome:
    G.CLOCK.tick(60)
    current_move = None

    # Handle AI moves
    if G.BOARD.turn == chess.BLACK and BLACK_AI_DEPTH >= 0:
        current_move = get_ai_move(BLACK_AI_DEPTH)
    elif G.BOARD.turn == chess.WHITE and WHITE_AI_DEPTH >= 0:
        current_move = get_ai_move(WHITE_AI_DEPTH)

    # Process user input (if it's not an AI's turn)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            tile_num = gui.tile_pos_to_num(event.pos)
            gui.draw_board()

            # Logic for selecting and moving pieces with the mouse
            if selected_square is None:
                selected_square = gui.make_selection(tile_num)
            elif selected_square == tile_num:
                gui.draw_board()
                selected_square = None
            else:
                for move in G.BOARD.legal_moves:
                    if move.from_square == selected_square and move.to_square == tile_num:
                        gui.draw_select_square(move.from_square)
                        gui.draw_select_square(move.to_square)
                        gui.print_san(move)
                        G.BOARD.push(move)
                        selected_square = None
                
                if selected_square is not None:
                    selected_square = gui.make_selection(tile_num)

        elif event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    # Draw all pieces on the board
    for piece_type in range(1, 7):
        w_piece_tiles = G.BOARD.pieces(piece_type, chess.WHITE)
        for tile_num in w_piece_tiles:
            gui.draw_piece(tile_num, piece_type, chess.WHITE)

        b_piece_tiles = G.BOARD.pieces(piece_type, chess.BLACK)
        for tile_num in b_piece_tiles:
            gui.draw_piece(tile_num, piece_type, chess.BLACK)

    # Check for game end conditions
    game_outcome = G.BOARD.outcome()
    if not TEST_MODE and game_outcome:
        gui.determine_outcome(game_outcome)

    pygame.display.update()

# Final loop to keep the window open after the game ends
while True:
    G.CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()