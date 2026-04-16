import pygame
import random
from DominoTile import DominoTile, create_domino_set
from Player import Player, HumanPlayer, AIPlayer
from gameLogic import calculate_trick_winner, calculate_trick_winner_NT, calculate_bid_winner, calculate_game_winner
from ScreenElements import PlayerLabel, load_image_safe, ImageButton, create_bid_buttons, create_trump_buttons, TextLabel
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

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Texas 42")

# Load your felt texture image
felt_texture = pygame.image.load("images/green_felt_background.png").convert()
felt_texture = pygame.transform.scale(felt_texture, (screen.get_width(), screen.get_height()))
# Get the size of the texture
texture_width, texture_height = felt_texture.get_size()


# Colors
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

#font objects
font = pygame.font.SysFont('arial', 36)

game_state = "dealing"
dealing_complete = False
game_winner = None
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
highest_bid = 0


player_font = pygame.font.SysFont("arial", 36)
trick_font = pygame.font.SysFont("arial", 20)

'''player1_label = PlayerLabel(human1, 500, 5, player_font, (19, 126, 168), rotation=0)
player2_label = PlayerLabel(ai1, 1110, 350, player_font,(19, 126, 168), rotation=90)
player3_label = PlayerLabel(ai2, 500, 750, player_font, (19, 126, 168), rotation= 0)
player4_label = PlayerLabel(ai3, 40, 350, player_font,(19, 126, 168), rotation = 270)

trick1_label = TextLabel( 660, 390, "", trick_font, (19, 126, 168))
trick2_label = TextLabel( 660, 425, "", trick_font, (19, 126, 168))
trick3_label = TextLabel( 660, 460, "", trick_font, (19, 126, 168))
trick4_label = TextLabel( 660, 495, "", trick_font, (19, 126, 168))
trick5_label = TextLabel( 660, 530, "", trick_font, (19, 126, 168))
trick6_label = TextLabel( 660, 565, "", trick_font, (19, 126, 168))
trick7_label = TextLabel( 660, 600, "", trick_font, (19, 126, 168))'''

player1_label = PlayerLabel(human1, 500, 5, player_font, (255, 255, 255), rotation=0)
player2_label = PlayerLabel(ai1, 1110, 350, player_font,(white), rotation=90)
player3_label = PlayerLabel(ai2, 500, 750, player_font, ("white"), rotation= 0)
player4_label = PlayerLabel(ai3, 40, 350, player_font,("white"), rotation = 270)

trick1_label = TextLabel( 660, 390, "", trick_font, (255, 255, 255))
trick2_label = TextLabel( 660, 425, "", trick_font, (255, 255, 255))
trick3_label = TextLabel( 660, 460, "", trick_font, (255, 255, 255))
trick4_label = TextLabel( 660, 495, "", trick_font, (255, 255, 255))
trick5_label = TextLabel( 660, 530, "", trick_font, (255, 255, 255))
trick6_label = TextLabel( 660, 565, "", trick_font, (255, 255, 255))
trick7_label = TextLabel( 660, 600, "", trick_font, (255, 255, 255))

trick_labels = [trick1_label, trick2_label, trick3_label, trick4_label, trick5_label, trick6_label, trick7_label]

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
                if game_state == "game_over_display":
                    #reset for new game
                    dealing_complete = False
                    current_bidder = 1
                    trump = None
                    played_dominoes.clear()
                    trick_num = 1
                    team_1_trick_points = 0
                    team_2_trick_points = 0
                    trick_history.clear()
                    # Clear all trick labels
                    for label in trick_labels:
                        label.text = ""
                    # Clear all player hands
                    human1.hand.clear()
                    ai1.hand.clear()
                    ai2.hand.clear()
                    ai3.hand.clear()
                    game_state = "dealing"
                elif game_state == "dealing":
                    game_state = "bidding"
                elif game_state == "bidding":
                    game_state = "calculate_bid_winner"
                elif game_state == "calculate_bid_winner":
                    game_state = "trump_selection"
                elif game_state == "trump_selection":
                    game_state = "trick_play"
                elif game_state == "trick_play":
                    game_state = "calculate_trick_winner"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Allow players to make bids
            if game_state == "bidding":
                #if current_player.is_human:  # if player is human, player has to click a bid button
                try:
                    for bid_value in bid_buttons.keys():
                        if bid_buttons[bid_value].is_clicked((mouse_x, mouse_y)):
                            current_player.bid = bid_value
                            print(f'{current_player.name} bid {bid_value}')
                            update_bid_buttons(bid_value)
                            current_bidder += 1
                            break
                except KeyError as e:
                    print(f"Bid button key error: {e}")
                #else:           #if player is NOT human (i.e. AI Players), they automatically bid "pass"
                    #current_player.bid = 'pass'
                    #current_bidder += 1

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

            if game_state == "trick_play":
                if current_trick_player is not None:
                    for domino in current_trick_player.hand:
                        if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                            print(f"{current_trick_player.name} playing {domino.name}!")
                            played_dominoes.append((current_trick_player, domino))
                            current_trick_player.hand.remove(domino)
                            if len(played_dominoes) == 4:
                                print("Trick complete! Played dominos:")
                                if trump == 'no_trump':
                                    game_state = "calculate_trick_winner_NT"# ← Change state!
                                else:
                                    game_state = "calculate_trick_winner"  # ← Change state!
                                break

                                for player, domino in played_dominoes:
                                    print(f"  {player.name} played {domino.name}")

                            current_trick_player_index = (current_trick_player_index + 1) % 4

                            current_trick_player = players[current_trick_player_index]

                            print(f"Next player: {current_trick_player.name}")
                            break

    #fill screen with black
    #screen.fill(black)
    # Fill the screen with the texture
    for x in range(0, screen.get_width(), texture_width):
        for y in range(0, screen.get_height(), texture_height):
            screen.blit(felt_texture, (0, 0))


    player1_label.draw(screen)
    player2_label.draw(screen)
    player3_label.draw(screen)
    player4_label.draw(screen)

    for label in trick_labels:
        label.draw(screen)

    # Move all trick dominoes to the bottom of the screen, shrunk
    corner_x = 400
    corner_y = 390
    for trick_index, trick in enumerate(trick_history):   # changed trick_num to trick_index to avoid variable shadowing
        for domino_num, (player, domino) in enumerate(trick):
            domino_image = domino_images[domino.name]
            small_domino = pygame.transform.scale(domino_image, (46, 26))
            x_pos = corner_x + (domino_num * 66)
            y_pos = corner_y + (trick_index * 35)
            screen.blit(small_domino, (x_pos, y_pos))

#start the dealing process
    if game_state == "dealing" and not dealing_complete:
        # Shuffle and deal dominos
        random.shuffle(all_dominoes)
        for i in range(7):
            human1.receive_domino(all_dominoes[i])
            ai1.receive_domino(all_dominoes[i + 7])
            ai2.receive_domino(all_dominoes[i + 14])
            ai3.receive_domino(all_dominoes[i + 21])
        dealing_complete = True
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

    def update_bid_buttons(bid_value):
        global highest_bid
        if bid_value != "pass":
            highest_bid = max(highest_bid, bid_value)
            # Disable buttons with bid values <= highest_bid
            for bid, button in bid_buttons.items():
                if bid != "pass" and bid <= highest_bid:
                    button.is_enabled = False
                else:
                    button.is_enabled = True

    if game_state == "bidding" and current_bidder <=4:
        mouse_pos = pygame.mouse.get_pos()
        for button in bid_buttons.values():
            button.update(mouse_pos)
            button.draw(screen)
        current_player = players[current_bidder - 1]

        '''#check if player needs input (i.e. is human)
        if current_player.needs_input:
            pass    #go ahead with click-handling for player's bid
        else: # if player is NOT human, automatically bid pass
            print(f"{current_player.name} passes.")
            current_player.bid = "pass"
            current_bidder += 1'''

        # Make player bid prompt
        bidder_text = font.render(f"Player {current_bidder} make your bid:", True, white)
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

        bidder_text = font.render(f"{bid_winner.name} chose your trump:", True, white)
        screen.blit(bidder_text, (400, 200))


    if game_state == "trick_play":
        trump_text = font.render(f"{bid_winner.name} won the bid with {highest_bid}. Trump is: {trump}", True, white)
        screen.blit(trump_text, (300, 200))

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
            current_trick_player_index = players.index(bid_winner)  # Initializes the bid_winner as the new current_trick_player
            current_trick_player = players[current_trick_player_index]
            print(f"Starting trick play. First player: {current_trick_player.name}")

        elif current_trick_player is not None:  # Safety check
            # Check for Player 1 (human1)
            if current_trick_player == human1:
                for domino in human1.hand:
                    if domino.rect is not None and domino.rect.collidepoint(mouse_x, mouse_y):
                        print(f"{current_trick_player.name} playing {domino.name}!")
                        played_dominoes.append((player, domino))
                        human1.hand.remove(domino)
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
                        print(f"Next player: {current_trick_player.name}")
                        break

            # Move all trick dominoes to the bottom of the screen, shrunk
            corner_x = 400  #specifies x-coordinate of upper left corner of first domino
            corner_y = 390  #specifies y-coordinate of upper left corner of first domino
            for trick_index, trick in enumerate(trick_history):  # Loop through each trick
                for domino_num, (player, domino) in enumerate(trick):  # Loop through each domino in the trick
                    domino_image = domino_images[domino.name]  # Get the image
                    small_domino = pygame.transform.scale(domino_image, (46, 26))  # Shrink it
                    x_pos = corner_x + (domino_num * 66)    #first domino (index 0) will be at the original corner-x, next 66 pixels to the right
                    y_pos = corner_y + (trick_index * 35)   ##first domino (index 0) will be at the original corner-y, next 66 pixels downward
                    screen.blit(small_domino, (x_pos, y_pos))   # Now draw small_domino at the appropriate position

    if game_state == "calculate_trick_winner_NT":
        trick_winner, trick_points = calculate_trick_winner_NT(played_dominoes)
        if trick_winner.team == 1:
            team_1_trick_points += trick_points
        else:
            team_2_trick_points += trick_points
        # change the text in the trick label
        trick_labels[trick_num - 1].text = f"{trick_winner.name} won trick {trick_num} for {trick_points} points"

        #print(f"Set label text: {trick_labels[trick_num - 1].text}")
        #print(f"Label position: x={trick_labels[trick_num - 1].rect.x}, y={trick_labels[trick_num - 1].rect.y}")
        #print(f"Label text: '{trick_labels[trick_num - 1].text}'")
        pygame.display.update()
        # If this is trick 7, add a delay so the label is visible
        #if trick_num == 7:
            #pygame.time.delay(2000)  # 2 second delay to see trick 7 result
        current_trick_player = trick_winner # Trick winner plays first in the next trick
        current_trick_player_index = players.index(trick_winner)
        trick_history.append(played_dominoes.copy()) # Add the trick to trick_history to eventually determine game winner
        print(f'Trick winner is {trick_winner.name}')
        trick_num += 1
        if trick_num > 7:
            game_state = "calculate_game_winner"
            print("Calculating game winner")
        else:
            played_dominoes.clear()
            game_state = "trick_play"

    elif game_state == "calculate_trick_winner":
        trick_winner, trick_points = calculate_trick_winner(played_dominoes, trump)
        if trick_winner.team == 1:
            team_1_trick_points += trick_points
        else:
            team_2_trick_points += trick_points
        # change the text in the trick label
        trick_labels[trick_num - 1].text = f"{trick_winner.name} won trick {trick_num} for {trick_points} points."
        #print(f"Set label text: {trick_labels[trick_num - 1].text}")
        #print(f"Label position: x={trick_labels[trick_num - 1].rect.x}, y={trick_labels[trick_num - 1].rect.y}")
        #print(f"Label text: '{trick_labels[trick_num - 1].text}'")
        pygame.display.update()
        # If this is trick 7, add a delay so the label is visible
        #if trick_num == 7:
            #pygame.time.delay(2000)  # 2 second delay to see trick 7 result
        current_trick_player = trick_winner
        current_trick_player_index = players.index(trick_winner)
        trick_history.append(played_dominoes.copy())
        print(f'Trick winner is {trick_winner.name}')
        trick_num += 1
        if trick_num > 7:
            game_state = "calculate_game_winner"
            #print("Calculating game winner")
        else:
            played_dominoes.clear()
            game_state = "trick_play"

    if game_state == "calculate_game_winner":
        game_winner = calculate_game_winner(bid_winner, highest_bid, team_1_trick_points, team_2_trick_points)
        if highest_bid == 84: # if the bid was 84...
            games_to_add = 2  # add two games
        else:                 # if not...
            games_to_add = 1  #add one game

        if game_winner == 1:
            team_1_games_won += games_to_add
        else:
            team_2_games_won += games_to_add

        print(f"Team {game_winner} won the game.")

        print(f'Team 1 has won {team_1_games_won} games.')
        print(f'Team 2 has won {team_2_games_won} games.')

        if team_1_games_won >= 7:
            #match_winner = team 1
            print(f'Team 1 won the match')
        elif team_2_games_won >= 7:
            #match_winner = team 2
            print(f'Team 2 won the match')
        else:
            pass
        game_state = "game_over_display"

    if game_state == "game_over_display":
        # Display who won
        if game_winner == 1:
            winner_text = font.render(f"Team 1 wins the game!", True, white)
        else:
            winner_text = font.render(f"Team 2 wins the game!", True, white)

        screen.blit(winner_text, (400, 150))

        # Display current game score
        score_text = font.render(f"Team 1: {team_1_games_won}  Team 2: {team_2_games_won}", True, white)
        screen.blit(score_text, (400, 200))

        # Display continue prompt
        continue_text = font.render("Press SPACE to start next game", True, white)
        screen.blit(continue_text, (350, 250))




    # Update the display
    pygame.display.flip()
    clock.tick(60)  #