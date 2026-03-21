#functions for doing calculations in the game
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


def calculate_trick_winner(played_dominoes, trump):
    trick_winner = None
    trick_points = 1

    lead_player, lead_domino = played_dominoes[0]
    if trump != "no trump" and lead_domino.is_trump(trump):
        lead_suit = trump
    else:
        lead_suit = lead_domino.hi_num

    # Define best_player and best_domino as the first player/domino in played_dominoes
    best_player = played_dominoes[0][0]
    best_domino = played_dominoes[0][1]
    trump_dominoes = [] # Find trump dominos in the trick and make a list of them

    for player, domino in played_dominoes:
        if trump != "no trump" and domino.is_trump(trump):
            trump_dominoes.append((player, domino))
            print(f" {player.name} played trump: {domino.name}")

    #If the first domino played was a trump:
    # Check each player/domino in trump_dominoes to see whether it beats the first domino played i the trick.
    for player, domino in trump_dominoes[1:]:
        # Check if this domino is the double trump
        if domino.hi_num == trump and domino.lo_num == trump:
            best_domino = domino
            best_player = player
        # Check if current best is double trump (if so, don't replace it)
        elif best_domino.hi_num == trump and best_domino.lo_num == trump:
            pass  # Keep best_domino as is
        # Otherwise compare non-trump numbers
        elif domino.get_non_trump_num(trump) > best_domino.get_non_trump_num(trump):
            best_domino = domino
            best_player = player

# if trump is not the lead suit but a trump was played
    if lead_suit != trump and len(trump_dominoes) > 0:
        best_player, best_domino = trump_dominoes[0]
        for player, domino in trump_dominoes[1:]:
            # Check if this domino is the double trump
            if domino.hi_num == trump and domino.lo_num == trump:
                best_domino = domino
                best_player = player
            # Check if current best is double trump (if so, don't replace it)
            elif best_domino.hi_num == trump and best_domino.lo_num == trump:
                pass  # Keep best_domino as is
            # Otherwise compare non-trump numbers
            elif domino.get_non_trump_num(trump) > best_domino.get_non_trump_num(trump):
                best_domino = domino
                best_player = player

    # if there are no trumps in the trick, check dominoes against lead suit
    if not trump_dominoes:
        best_player, best_domino = played_dominoes[0]
        for player, domino in played_dominoes[1:]:
            if domino.hi_num == lead_suit and domino.lo_num == lead_suit:
                best_domino = domino
                best_player = player
            elif domino.has_number == lead_suit:
                domino.get_non_lead_num(lead_suit)
                if domino.get_non_lead_num(lead_suit) > best_domino.get_non_lead_num(lead_suit):
                    best_domino = domino
                    best_player = player
    for player, domino in played_dominoes:
        trick_points += domino.count

    trick_winner = best_player
    return trick_winner, trick_points



def calculate_game_winner(bid_winner, highest_bid, team_1_trick_points, team_2_trick_points):
    if bid_winner.team == 1:            #check who won the bid
        if team_1_trick_points >= highest_bid: # check that they got as many points as they bid
            return 1                    #winning team's number
        else:
            return 2                    #winning team's number

    if bid_winner.team == 2:  #check who won the bid
        if team_2_trick_points >= highest_bid:
            return 2
        else:
            return 1

    return game_winner


    # continue_text = font.render("Press SPACE to continue", True, green)
    # screen.blit(continue_text, (400, 600))
