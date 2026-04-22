##functions for doing calculations in the game
import pygame
from DominoTile import DominoTile
from Player import Player, HumanPlayer, AIPlayer



'''def get_valid_plays(player, lead_domino, trump, trick_num):
    # Case 1: Player is first in the trick
    if lead_domino is None:
        if trick_num == 1:
            # Must play trump on first trick
            valid_plays = [d for d in player.hand if d.is_trump(trump)]

            if valid_plays:   #make sure the player HAS a trump in his hand
                return valid_plays
            else:
                return player.hand
        else:
            # Can play anything
            return player.hand

    # Case 2: Player is NOT first - must follow suit if possible
    else:
        # Determine the lead suit
        if lead_domino.is_trump(trump):
            # check if lead domino is a trump
            valid_plays = [d for d in player.hand if d.is_trump(trump)]
            if valid_plays:  # make sure the player HAS a trump in his hand
                return valid_plays
            else:
                return player.hand

        else:    #if the lead domino ws NOT a trump
            # Find all dominoes that match lead suit (excluding trump if lead is not trump!)
            valid_plays = [d for d in player.hand if d.has_number(lead_domino.hi_num) and not d.is_trump(trump)]

            # If we found matching dominoes, return those
            if valid_plays:
                return valid_plays
            else:
                # Can't follow suit - can play anything
                return player.hand'''


def draw_trick_history(screen, trick_history, domino_images, corner_x=400, corner_y=390):
    # To display all completed tricks as small dominoes at bottom of screen
    for trick_index, trick in enumerate(trick_history):
        for domino_num, (player, domino) in enumerate(trick):
            domino_image = domino_images[domino.name]
            small_domino = pygame.transform.scale(domino_image, (46, 26))
            x_pos = corner_x + (domino_num * 66)
            y_pos = corner_y + (trick_index * 35)
            screen.blit(small_domino, (x_pos, y_pos))

####################################################################################################################
def calculate_bid_winner(players):
    highest_bid = 0
    bid_winner = None
    all_bids = [(player, player.bid) for player in players]
    for player in players:
        if player.bid == "pass":
            continue
        bid_value = int(player.bid)
        if bid_value > highest_bid:
            highest_bid = bid_value
            bid_winner = player
    print(f'{bid_winner.name} won the bid.')
    return bid_winner, highest_bid
####################################################################################################################
def calculate_trick_winner_NT(played_dominoes):
    trick_winner = None
    trick_points = 1

    lead_player, lead_domino = played_dominoes[0]
    lead_suit = lead_domino.hi_num

    # Define best_player and best_domino as the first player/domino in played_dominoes
    best_player, best_domino = played_dominoes[0]

    for player, domino in played_dominoes[1:]:
        if domino.hi_num == lead_suit and domino.lo_num == lead_suit:  #check if domino is the double
            best_domino = domino
            best_player = player
        elif domino.has_number == lead_suit:
            if domino.get_non_lead_num(lead_suit) > best_domino.get_non_lead_num(lead_suit):
                best_domino = domino
                best_player = player
    for player, domino in played_dominoes:
        trick_points += domino.count

    trick_winner = best_player
    return trick_winner, trick_points
##############################################################################################

def calculate_trick_winner(played_dominoes, trump):
    # If no trump, redirect to the NT function
    if trump == "no trump":
        return calculate_trick_winner_NT(played_dominoes)

    trick_winner = None
    trick_points = 1

    lead_player, lead_domino = played_dominoes[0]
    if trump != "no trump" and lead_domino.is_trump(trump):
        lead_suit = trump
    elif trump == "no trump":
        lead_suit = lead_domino.hi_num
    else:
        lead_suit = lead_domino.hi_num

    trump_dominoes = [] # Find trump dominos in the trick and make a list of them

    for player, domino in played_dominoes:
        if trump != "no trump" and domino.is_trump(trump):
            trump_dominoes.append((player, domino))  #adds domino and its player to the list trump_dominoes for calculating trick winner
            print(f" {player.name} played trump: {domino.name}")

    # Case 1: if there are ANY trumps played in the trick
    if trump_dominoes:
        best_player, best_domino = trump_dominoes[0]  # set first trump as best domino and its player as best player

        # If the first trump is the double, it automatically wins - no need to check others!
        if best_domino.is_double:
            pass  # best_domino is already set to the double - nothing beats it
        else:
            # First trump is NOT the double, so check the rest
            for player, domino in trump_dominoes[1:]:
                # If we find the double trump, it wins immediately
                if domino.is_double:
                    best_domino = domino
                    best_player = player
                    break  # Stop checking - nothing beats the double
                # Otherwise compare non-trump numbers
                elif domino.get_non_trump_num(trump) > best_domino.get_non_trump_num(trump):
                    best_domino = domino
                    best_player = player

    # Case 2: if there are NO trumps in the trick, check dominoes against lead suit
    if not trump_dominoes:
        best_player, best_domino = played_dominoes[0] #initializes first player/domino as best
        if best_domino.is_double:
            pass    # double always wins, so stop checking
        else:
            for player, domino in played_dominoes[1:]:
                if best_domino.is_double: #checks if this domino is double
                    best_domino = domino
                    best_player = player
                    break #the double always wins, so stop checking
                elif domino.has_number(lead_suit):  #compare non-double dominoes that follow suit
                    if domino.get_non_lead_num(lead_suit) > best_domino.get_non_lead_num(lead_suit):
                        best_domino = domino
                        best_player = player

    for player, domino in played_dominoes:
        trick_points += domino.count

    trick_winner = best_player
    return trick_winner, trick_points

######################################################################################################################

def calculate_game_winner(bid_winner, highest_bid, team_1_trick_points, team_2_trick_points):

    if highest_bid == "84":  # 84 bid is a special case, you only need to win 42 points to win
        points_needed = 42
    else:
        points_needed = highest_bid

    if bid_winner.team == 1:            #check who won the bid
        if team_1_trick_points >= points_needed: # check that they got as many points as they bid
            return 1                    #winning team's number
        else:
            return 2                    #winning team's number

    if bid_winner.team == 2:  #check who won the bid
        if team_2_trick_points >= points_needed:
            return 2
        else:
            return 1

    raise ValueError(f"Invalid team number: {bid_winner.team}")

#############################################################################
'''def calculate_match_winner(team_1_games_won, team_2_games_won):
    if team_1_games_won == 7:
        return 1
    else:
        return 2
    return match_winner
    # not sure I really need a function for this, but I can't figure out how else to do it right now'''
##############################################################################
    # continue_text = font.render("Press SPACE to continue", True, green)
    # screen.blit(continue_text, (400, 600))