import pygame
import random
from DominoTile import DominoTile, create_domino_set
from Player import Player, HumanPlayer, AIPlayer
from gameLogic import calculate_trick_winner, calculate_bid_winner, calculate_game_winner
from ScreenElements import PlayerLabel, load_image_safe, ImageButton, create_bid_buttons, create_trump_buttons
all_dominoes = create_domino_set(DominoTile)
valid_bids = ["30", "31", "32", "84", "pass"]


# Load all domino images into a dictionary
domino_images = {}

# Load all images safely
for domino in all_dominoes:
    domino_images[domino.name] = load_image_safe(domino.image)

back_image = load_image_safe('images/DominoBack.png')
bid_button_image = load_image_safe('images/Bid30.png', 50, 50)

# Load all bid button images
bid_images = {}
for bid_value in [30, 31, 32, 84]:
    bid_images[bid_value] = load_image_safe(f'images/Bid{bid_value}.png', 50, 50)
bid_images['pass']  = load_image_safe(f'images/BidPass.png', 50, 50)

bid_buttons = create_bid_buttons(bid_images)



trump_images = {}
for trump_value in [0, 1, 2, 3, 4, 5, 6]:
    trump_images[trump_value] = load_image_safe(f'images/Trump{trump_value}.png', 50, 50)
trump_images['no_trump'] = load_image_safe(f'images/Trump7.png', 120, 50)

trump_buttons = create_trump_buttons(trump_images)


# Create players
human1 = HumanPlayer("Player 1", 1, None)
ai1 = AIPlayer("Player 2", 2, None)
ai2 = AIPlayer("Player 3", 1, None)
ai3 = AIPlayer("Player 4", 2, None)

players = [human1, ai1, ai2, ai3]

# Shuffle and deal dominos
random.shuffle(all_dominoes)
for i in range(7):
    human1.receive_domino(all_dominoes[i])
    ai1.receive_domino(all_dominoes[i + 7])
    ai2.receive_domino(all_dominoes[i + 14])
    ai3.receive_domino(all_dominoes[i + 21])

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Texas 42")

# Colors
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

#font objects
font = pygame.font.SysFont('arial', 36)

game_state = "dealing"
current_bidder = 1      # For the purposes of this project, Player 1 will bid first in game_state == "bidding"
current_trick_player = None         #initializes current_trick_player for game_state = "trick_play"
current_trick_player_index = None   #initializes current_trick_player_index for rotating playhers in game_state == "trick_play"
trump = None
played_dominoes = [] #List of tuples (player, domino)
lead_suit = None
trick_num = 1
lead_domino = None
all_bids = []
trick_history = [] # make this a tuple of 7 tricks
team_1_trick_points = 0
team_2_trick_points = 0
team_1_games_won = 0
team_2_games_won = 0
angle = 0

#display fonts
# fonts = pygame.font.get_fonts()
P1_font = pygame.font.SysFont("arial", 36)
P2_font = pygame.font.SysFont("arial", 36)
P3_font = pygame.font.SysFont("arial", 36)
P4_font = pygame.font.SysFont("arial", 36)

player1_label = PlayerLabel(human1, 500, 5, P1_font, (19, 126, 168), rotation=0)
player2_label = PlayerLabel(ai1, 1110, 350, P2_font,(19, 126, 168), rotation=90)
player3_label = PlayerLabel(ai2, 500, 750, P3_font, (19, 126, 168), rotation= 0)
player4_label = PlayerLabel(ai3, 40, 350, P4_font,(19, 126, 168), rotation = 270)


# Game loop
running = True
clock = pygame.time.Clock()

#Game Loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:  # Press SPACE to advance phases
                if game_state == "dealing":
                    game_state = "bidding"
                elif game_state == "bidding":
                    game_state = "calculate_bid_winner"
                elif game_state == "calculate_bid_winner":
                    game_state = "trump_selection"
                elif game_state == "trump_selection":
                    game_state = "trick_play"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Allow players to make bids
            if game_state == "bidding":
                if current_player.is_human:
                    try:
                        for bid_value in bid_buttons.keys():
                            if bid_buttons[bid_value].is_clicked((mouse_x, mouse_y)):
                                current_player.bid = bid_value
                                print(f'{current_player.name} bid {bid_value}')
                                current_bidder += 1
                                break
                    except KeyError as e:
                        print(f"Bid button key error: {e}")
                else:
                    current_player.bid = 'pass'
                    current_bidder += 1

                if current_bidder > 4:
                    game_state = "calculate_bid_winner"




            # winning_bidder makes a trump selection -
            # still have to figure out how to disallow other players from clicking trump buttons

            if game_state == "trump_selection":
                try:
                    for trump_value in trump_buttons.keys():
                        if trump_buttons[trump_value].is_clicked((mouse_x, mouse_y)):
                            trump = trump_value
                            print(f'Trump is: {trump}')
                            game_state = "trick_play"
                            break
                except KeyError as e:
                    print(f"Trump button key error: {e}")

                game_state = "trick_play"

            if game_state == "trick_play":
                if current_trick_player is not None:
                    for domino in current_trick_player.hand:
                        if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                            print(f"{current_trick_player.name} playing {domino.name}!")
                            played_dominoes.append((current_trick_player, domino))
                            current_trick_player.hand.remove(domino)
                            if len(played_dominoes) == 4:
                                print("Trick complete! Played dominos:")
                                for player, domino in played_dominoes:
                                    print(f"  {player.name} played {domino.name}")

                                game_state = "calculate_trick_winner"  # ← Change state!
                                break

                            current_trick_player_index = (current_trick_player_index + 1) % 4

                            current_trick_player = players[current_trick_player_index]

                            print(f"Next player: {current_trick_player.name}")
                            break


    #fill screen with black
    screen.fill(black)


    player1_label.draw(screen)
    player2_label.draw(screen)
    player3_label.draw(screen)
    player4_label.draw(screen)

#start the dealing process
    # Display Player 1's hand at the top
    x_start = 200
    y_position = 50  # top of screen
    x_spacing = 120  # Space between dominos
    for i, domino in enumerate(human1.hand):
        domino_image = domino_images[domino.name]
        x_position = x_start + (i * x_spacing)
        domino.rect = screen.blit(domino_image, (x_position, y_position)) #stores the rectangle

    # Display Player 2's hand at the right
    x_position = 1050  # right of screen
    y_start = 50
    y_spacing = 100  # Space between dominos
    for i, domino in enumerate(ai1.hand):

        domino_image = pygame.transform.rotate(domino_images[domino.name], 90)
        y_position = y_start + (i * y_spacing)
        screen.blit(domino_image, (x_position, y_position))
        domino.rect = screen.blit(domino_image, (x_position, y_position))

    # Display Player 3's hand at the bottom
    x_start = 200
    y_position = 700  # Bottom of screen
    x_spacing = 120  # Space between dominos
    for i, domino in enumerate(ai2.hand):
        domino_image = domino_images[domino.name]
        x_position = x_start + (i * x_spacing)
        domino.rect = screen.blit(domino_image, (x_position, y_position))

    # Display Player 4's hand at the left
    x_position = 90  # left of screen
    y_start = 50
    y_spacing = 100  # Space between dominos
    for i, domino in enumerate(ai3.hand):
        domino_image = pygame.transform.rotate(domino_images[domino.name], 90)
        y_position = y_start + (i * y_spacing)
        domino.rect = screen.blit(domino_image, (x_position, y_position))


    if game_state == "bidding" and current_bidder <=4:
        for button in bid_buttons.values():
            button.draw(screen)
        current_player = players[current_bidder - 1]
        #check if player needs input (i.e. is human)
        if current_player.needs_input:
            pass    #go ahead with click-handling for player's bid
        else: # if player is NOT human, automatically bid pass
            print(f"{current_player.name} passes.")
            current_player.bid = "pass"
            current_bidder += 1

        # Make player bid prompt
        bidder_text = font.render(f"Player {current_bidder} make your bid:", True, green)
        screen.blit(bidder_text, (400, 200))

    if game_state == "calculate_bid_winner":
        bid_winner, highest_bid = calculate_bid_winner(players)
        button_rectBW = pygame.Rect(400, 200, 350, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, black, button_rectBW)
        button_textBW = font.render(f"Player {bid_winner.name} won the bid with {highest_bid}", True, green)
        text_rectBW = button_textBW.get_rect(center=button_rectBW.center)
        screen.blit(button_textBW, text_rectBW)
        game_state = "trump_selection"

# make trump selection buttons
    if game_state == "trump_selection":
        #TODO: still need to make it so that only the bid_winner can click trump buttons!!!

        for button in trump_buttons.values():
            button.draw(screen)

        bidder_text = font.render(f"{bid_winner.name} chose your trump:", True, green)
        screen.blit(bidder_text, (400, 200))


    if game_state == "trick_play":
        trump_text = font.render(f"{bid_winner.name} won the bid with {highest_bid}. Trump is: {trump}", True, green)
        screen.blit(trump_text, (300, 200))
        # Initializes the bid_winner as the new current_trick_player
        # Sets positions for dominoes to move into when they are played
        play_positions = [
            (350, 300),  # Position for 1st domino played
            (475, 300),  # Position for 2nd domino played
            (600, 300),  # Position for 3rd domino played
            (725, 300)  # Position for 4th domino played
        ]

        for i, (player, domino) in enumerate(played_dominoes):
            if i < len(play_positions):  # Safety check
                try:
                    domino_image = domino_images[domino.name]
                    screen.blit(domino_image, play_positions[i])
                except KeyError as e:
                    print(f'Domino image not found: {e}')


        if current_trick_player is None:
            current_trick_player_index = players.index(bid_winner)
            current_trick_player = players[current_trick_player_index]
            print(f"Starting trick play. First player: {current_trick_player.name}")

        if current_trick_player is not None:  # Safety check
            # Check for Player 1 (human1)
            if current_trick_player == human1:
                for domino in human1.hand:
                    if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                        print(f"{current_trick_player.name} playing {domino.name}!")
                        played_dominoes.append((player, domino))
                        human1.hand.remove(domino)
                        #domino.rect
                        current_trick_player_index = (current_trick_player_index + 1) % 4
                        current_trick_player = players[current_trick_player_index]
                        print(f"Next player: {current_trick_player.name}")
                        break

            # Check for Player 2 (ai1)
            elif current_trick_player == ai1:
                for domino in ai1.hand:
                    if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                        print(f"{current_trick_player.name} playing {domino.name}!")
                        played_dominoes.append((player, domino))
                        ai1.hand.remove(domino)
                        current_trick_player_index = (current_trick_player_index + 1) % 4
                        current_trick_player = players[current_trick_player_index]
                        print(f"Next player: {current_trick_player.name}")
                        break

            # Check for Player 3 (ai2)
            elif current_trick_player == ai2:
                for domino in ai2.hand:
                    if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                        print(f"{current_trick_player.name} playing {domino.name}!")
                        played_dominoes.append((player, domino))
                        ai2.hand.remove(domino)
                        current_trick_player_index = (current_trick_player_index + 1) % 4
                        current_trick_player = players[current_trick_player_index]
                        print(f"Next player: {current_trick_player.name}")
                        break

            # Check for Player 4 (ai3)
            elif current_trick_player == ai3:
                for domino in ai3.hand:
                    if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                        print(f"{current_trick_player.name} playing {domino.name}!")
                        played_dominoes.append((player, domino))
                        ai3.hand.remove(domino)
                        current_trick_player_index = (current_trick_player_index + 1) % 4
                        current_trick_player = players[current_trick_player_index]
                        break

            # Move all trick dominoes to the bottom of the screen, shrunk
            corner_x = 480
            corner_y = 390
            for trick_index, trick in enumerate(trick_history):  # Loop through each trick
                for domino_num, (player, domino) in enumerate(trick):  # Loop through each domino in the trick
                    domino_image = domino_images[domino.name]  # Get the image
                    small_domino = pygame.transform.scale(domino_image, (46, 26))  # Shrink it
                    x_pos = corner_x + (domino_num * 66)
                    y_pos = corner_y + (trick_index * 35)
                    screen.blit(small_domino, (x_pos, y_pos))
                    # Now draw small_domino at the appropriate position'

        if len(played_dominoes) == 4:
            game_state = "calculate_trick_winner"
            #for player, domino in played_dominoes:
                #print(f"  {player.name} played {domino.name}")


    if game_state == "calculate_trick_winner":
        trick_winner, trick_points = calculate_trick_winner(played_dominoes, trump)
        if trick_winner.team == 1:
            team_1_trick_points += trick_points
        else:
            team_2_trick_points += trick_points
        current_trick_player = trick_winner
        current_trick_player_index = players.index(trick_winner)
        trick_history.append(played_dominoes.copy())
        played_dominoes.clear()
        print(f"{trick_winner.name} won trick #{trick_num} for {trick_points} points!")

        trick_num += 1
        #print(f'Debug: the trick number is {trick_num}')
        if trick_num > 7:
            game_state = "calculate_game_winner"
            print("Calculating game winner")
        else:
            game_state = "trick_play"

    if game_state == "calculate_game_winner":
        winning_team = calculate_game_winner(bid_winner, highest_bid, team_1_trick_points, team_2_trick_points)
        if highest_bid == 84: # if the bid was 84...
            games_to_add = 2  # add two games
        else:                 # if not...
            games_to_add = 1  #add one game

        if winning_team == 1:
            team_1_games_won += games_to_add
        else:
            team_2_games_won += games_to_add

        print(f"Team {winning_team} won the game.")
        game_text = font.render(f"{winning_team} won the game!", True, green)
        screen.blit(trump_text, (300, 200))
        print(f"Team 1 has won {team_1_games_won} games")
        print(f"Team 2 has won {team_2_games_won} games")
        team_1_trick_points = 0
        team_2_trick_points = 0
        trick_num = 1
        game_state = "dealing"
        # Draw UI every frame
        #trick_text = font.render(f"Trick Play - Trump is {trump}", True, green)
        #screen.blit(trick_text, (400, 200))

        #turn_text = font.render(f"{current_trick_player.name}'s turn", True, green)
        #screen.blit(turn_text, (400, 250))




    # Update the display
    pygame.display.flip()
    clock.tick(60)  #