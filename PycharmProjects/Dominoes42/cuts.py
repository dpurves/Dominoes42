
import pygame

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
dt = 0
running = True


while running:
        # Handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        newplace1 = pygame.draw.rect(screen, "#96ceb4", (200, 530, 46, 26), width=2)
        newplace2 = pygame.draw.rect(screen, "#96ceb4", (200, 560, 46, 26), width=2)
        newplace3 = pygame.draw.rect(screen, "#96ceb4", (200, 590, 46, 26), width=2)
        newplace4 = pygame.draw.rect(screen, "#96ceb4", (200, 620, 46, 26), width=2)

        newplace5 = pygame.draw.rect(screen, "#96ceb4", (260, 530, 46, 26), width=2)
        newplace6 = pygame.draw.rect(screen, "#96ceb4", (260, 560, 46, 26), width=2)
        newplace7 = pygame.draw.rect(screen, "#96ceb4", (260, 590, 46, 26), width=2)
        newplace8 = pygame.draw.rect(screen, "#96ceb4", (260, 620, 46, 26), width=2)

        newplace9 = pygame.draw.rect(screen, "#96ceb4", (400, 530, 46, 26), width=2)
        newplace10 = pygame.draw.rect(screen, "#96ceb4", (400, 560, 46, 26), width=2)
        newplace11 = pygame.draw.rect(screen, "#96ceb4", (400, 590, 46, 26), width=2)
        newplace12 = pygame.draw.rect(screen, "#96ceb4", (400, 620, 46, 26), width=2)

        newplace13 = pygame.draw.rect(screen, "#96ceb4", (500, 530, 46, 26), width=2)
        newplace14 = pygame.draw.rect(screen, "#96ceb4", (500, 560, 46, 26), width=2)
        newplace15 = pygame.draw.rect(screen, "#96ceb4", (500, 590, 46, 26), width=2)
        newplace16 = pygame.draw.rect(screen, "#96ceb4", (500, 620, 46, 26), width=2)





        screen.blit(P1_font, P1_font_rect)
           screen.blit(P2_font, P2_font_rect)
           screen.blit(P3_font, P3_font_rect)
           screen.blit(P4_font, P4_font_rect)

# Define the font
P1_font = pygame.font.SysFont('arial', 36)
P2_font = pygame.font.SysFont('arial', 36)
P3_font = pygame.font.SysFont('arial', 36)
P4_font = pygame.font.SysFont('arial', 36)

# render the text as a surface
P1_font = P1_font.render('Player 1', True, '#137ea8')
P2_font = P2_font.render('Player 2', True, '#137ea8')
P2_font = pygame.transform.rotate(P2_font, 90)
P3_font = P3_font.render('Player 3', True, '#137ea8')
P4_font = P4_font.render('Player 4', True, '#137ea8')
P4_font = pygame.transform.rotate(P4_font, 270)

# create a rect
P1_font_rect = P1_font.get_rect()
P2_font_rect = P2_font.get_rect()
P3_font_rect = P3_font.get_rect()
P4_font_rect = P4_font.get_rect()

#1200, 800
#position the text on the screen
P1_font_rect = (600, 5)
P2_font_rect = (1110, 400)
P3_font_rect = (600, 750)
P4_font_rect = (40, 400)


        #dt = clock.tick(60)
        pygame.display.flip()

# Check if AI player - if not, show front of dominoes, if so, show back of dominoes
'''if ai1.show_hand_visual:

        else:
            domino_image = back_image_rotated'''

'''# Define the font
P1_font = pygame.font.SysFont('arial', 36)
P2_font = pygame.font.SysFont('arial', 36)
P3_font = pygame.font.SysFont('arial', 36)
P4_font = pygame.font.SysFont('arial', 36)

# render the text as a surface
P1_font = P1_font.render('Player 1', True, '#137ea8')
P2_font = P2_font.render('Player 2', True, '#137ea8')
P2_font = pygame.transform.rotate(P2_font, 90)
P3_font = P3_font.render('Player 3', True, '#137ea8')
P4_font = P4_font.render('Player 4', True, '#137ea8')
P4_font = pygame.transform.rotate(P4_font, 270)

# create a rect
P1_font_rect = P1_font.get_rect()
P2_font_rect = P2_font.get_rect()
P3_font_rect = P3_font.get_rect()
P4_font_rect = P4_font.get_rect()

#1200, 800
#position the text on the screen
P1_font_rect = (600, 5)
P2_font_rect = (1110, 400)
P3_font_rect = (600, 750)
P4_font_rect = (40, 400)'''

'''screen.blit(P1_font, P1_font_rect)
    screen.blit(P2_font, P2_font_rect)
    screen.blit(P3_font, P3_font_rect)
    screen.blit(P4_font, P4_font_rect)'''

for domino in all_dominoes:
    try:
        loaded_image = pygame.image.load(domino.image)
        domino_images[domino.name] = loaded_image
    except pygame.error as e:
        print(f"Error loading {domino.image}: {e}")

try:
    back_image = pygame.image.load('images/DominoBack.png')
    back_image_rotated = pygame.transform.rotate(back_image, 90)
except pygame.error as e:
    print(f"Error loading back image: {e}")

'''# make bidding buttons
        button_rect1 = pygame.Rect(400, 300, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rect1)
        button_text1 = font.render("30", True, green)
        text_rect1 = button_text1.get_rect(center=button_rect1.center)
        screen.blit(button_text1, text_rect1)

        button_rect2 = pygame.Rect(500, 300, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rect2)
        button_text2 = font.render("31", True, green)
        text_rect2 = button_text2.get_rect(center=button_rect2.center)
        screen.blit(button_text2, text_rect2)

        button_rect3 = pygame.Rect(600, 300, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rect3)
        button_text3 = font.render("32", True, green)
        text_rect3 = button_text3.get_rect(center=button_rect3.center)
        screen.blit(button_text3, text_rect3)

        button_rect5 = pygame.Rect(700, 300, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rect5)
        button_text5 = font.render("84", True, green)
        text_rect5 = button_text5.get_rect(center=button_rect5.center)
        screen.blit(button_text5, text_rect5)

        button_rect6 = pygame.Rect(800, 300, 65, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rect6)
        button_text6 = font.render("pass", True, green)
        text_rect6 = button_text6.get_rect(center=button_rect6.center)
        screen.blit(button_text6, text_rect6)'''

#possible alternative for bidding buttons
if event.type == pygame.MOUSEBUTTONDOWN:
    mouse_pos = event.pos  # This is already a tuple (x, y)

    if game_state == "bidding":
        if bid30_button.is_clicked(mouse_pos):
            print(f"{current_player.name} bid 30")
            current_player.bid = 30
            current_bidder += 1
        elif bid31_button.is_clicked(mouse_pos):
            print(f"{current_player.name} bid 31")
            current_player.bid = 31
            current_bidder += 1

  if game_state == "trump_selection":
                if trump0_button.is_clicked((mouse_x, mouse_y)):
                    trump = 0
                    print(f'Trump is: {trump}')
                elif trump1_button.is_clicked((mouse_x, mouse_y)):
                    trump = 1
                    print(f'Trump is: {trump}')
                elif trump_.collidepoint(mouse_x, mouse_y):
                    trump = 2
                    print(f'Trump is: {trump}')
                elif button_rectT3.collidepoint(mouse_x, mouse_y):
                    trump = 3
                    print(f'Trump is: {trump}')
                elif button_rectT4.collidepoint(mouse_x, mouse_y):
                    trump = 4
                    print(f'Trump is: {trump}')
                elif button_rectT5.collidepoint(mouse_x, mouse_y):
                    trump = 5
                    print(f'Trump is: {trump}')
                elif button_rectT6.collidepoint(mouse_x, mouse_y):
                    trump = 6
                    print(f'Trump is: {trump}')
                elif button_rectNT.collidepoint(mouse_x, mouse_y):
                    trump = "no trump"
                    print(f'Trump is: {trump}')

button_rectT0 = pygame.Rect(200, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT0)
        button_textT0 = font.render(f"0", True, blue)
        text_rectT0 = button_textT0.get_rect(center=button_rectT0.center)
        screen.blit(button_textT0, text_rectT0)

        button_rectT1 = pygame.Rect(275, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT1)
        button_textT1 = font.render(f"1", True, blue)
        text_rectT1 = button_textT1.get_rect(center=button_rectT1.center)
        screen.blit(button_textT1, text_rectT1)

        button_rectT2 = pygame.Rect(350, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT2)
        button_textT2 = font.render(f"2", True, blue)
        text_rectT2 = button_textT2.get_rect(center=button_rectT2.center)
        screen.blit(button_textT2, text_rectT2)

        button_rectT3 = pygame.Rect(425, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT3)
        button_textT3 = font.render(f"3", True, blue)
        text_rectT3 = button_textT3.get_rect(center=button_rectT3.center)
        screen.blit(button_textT3, text_rectT3)

        button_rectT4 = pygame.Rect(500, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT4)
        button_textT4 = font.render(f"4", True, blue)
        text_rectT4 = button_textT4.get_rect(center=button_rectT4.center)
        screen.blit(button_textT4, text_rectT4)

        button_rectT5 = pygame.Rect(575, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT5)
        button_textT5 = font.render(f"5", True, blue)
        text_rectT5 = button_textT5.get_rect(center=button_rectT5.center)
        screen.blit(button_textT5, text_rectT5)

        button_rectT6 = pygame.Rect(650, 400, 50, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectT6)
        button_textT6 = font.render(f"6", True, blue)
        text_rectT6 = button_textT6.get_rect(center=button_rectT6.center)
        screen.blit(button_textT6, text_rectT6)

        button_rectNT = pygame.Rect(750, 400, 120, 50)  # (x, y, width, height) defines the rectangle
        pygame.draw.rect(screen, red, button_rectNT)
        button_textNT = font.render(f"no trump", True, blue)
        text_rectNT = button_textNT.get_rect(center=button_rectNT.center)
        screen.blit(button_textNT, text_rectNT)


# Draw bid buttons
        bid30_button.draw(screen)
        bid31_button.draw(screen)
        bid32_button.draw(screen)
        bid84_button.draw(screen)
        pass_button.draw(screen)

# draw trump buttons
trump0_button.draw(screen)
trump1_button.draw(screen)
trump2_button.draw(screen)
trump3_button.draw(screen)
trump4_button.draw(screen)
trump5_button.draw(screen)
trump6_button.draw(screen)
notrump_button.draw(screen)

'''if bis_button.is_clicked((mouse_x, mouse_y)):
                   bid_text30 = font.render(f"Player {current_bidder} bid 30", True, green)
                   screen.blit(bidder_text, (400, 200))
                   print(f"{current_player.name} bid 30")
                   current_player.bid = 30
                   current_bidder += 1
               elif bid31_button.is_clicked((mouse_x, mouse_y)):
                   print(f"{current_player.name} bid 31")
                   current_player.bid = 31
                   current_bidder += 1
               elif bid32_button.is_clicked((mouse_x, mouse_y)):
                   print(f"{current_player.name} bid 32")
                   current_player.bid = 32
                   current_bidder += 1
               elif bid84_button.is_clicked((mouse_x, mouse_y)):
                   print(f"{current_player.name} bid 84")
                   current_player.bid = 84
                   current_bidder += 1
               elif pass_button.is_clicked((mouse_x, mouse_y)):
                   print(f"{current_player.name} passed")
                   current_bidder += 1'''


'''# Special bids
bid_buttons['pass'] = load_image_safe('images/BidPass.png', 50, 50)
bid_buttons[84] = load_image_safe('images/Bid84.png', 50, 50)

bid30_button = ImageButton(350, 300, 70, 70, bid_buttons[30])
bid31_button = ImageButton(425, 300, 70, 70, bid_buttons[31])
bid32_button = ImageButton(500, 300, 70, 70, bid_buttons[32])
bid84_button = ImageButton(575, 300, 70, 70, bid_buttons[84])
pass_button = ImageButton(650, 300, 95, 70, bid_buttons['pass'])'''

'''# Special Trumps
trump_buttons['notrump'] = load_image_safe('images/Trump7.png', 50, 50)

trump0_button = ImageButton(300, 300, 70, 70, trump_buttons[0])
trump1_button = ImageButton(375, 300, 70, 70, trump_buttons[1])
trump2_button = ImageButton(450, 300, 70, 70, trump_buttons[2])
trump3_button = ImageButton(525, 300, 70, 70, trump_buttons[3])
trump4_button = ImageButton(600, 300, 70, 70, trump_buttons[4])
trump5_button = ImageButton(675, 300, 70, 70, trump_buttons[5])
trump6_button = ImageButton(750, 300, 70, 70, trump_buttons[6])
notrump_button = ImageButton(825, 300, 150, 70, trump_buttons['notrump'])'''





pygame.quit()
