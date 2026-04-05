import pygame
from Player import Player


#Base class for anything that appears on screen
class ScreenElement:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        #Override this in subclasses
        pass

    def is_clicked(self, mouse_pos):
        #Check if this element was clicked
        return self.rect.collidepoint(mouse_pos)


class Button(ScreenElement):
    #A clickable button with text
    def __init__(self, x, y, width, height, text, font, bg_color, text_color):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen):
        # Draw button background
        pygame.draw.rect(screen, self.bg_color, self.rect)
        # Draw text centered
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class ImageButton(ScreenElement):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = pygame.transform.scale(image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class TextLabel(ScreenElement):
    #Non-clickable text display
    def __init__(self, x, y, text, font, color):
        # Text doesn't need width/height for clicking, but we can calculate it
        temp_surface = font.render(text, True, color)
        super().__init__(x, y, temp_surface.get_width(), temp_surface.get_height())
        self.text = text
        self.font = font
        self.color = color

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x, self.rect.y))

class PlayerLabel(ScreenElement):   #needs to stay on the screen all the time and not change
    def __init__(self, player, x, y, font, color, rotation=0):
        # Calculate width/height from rendered text for the rect
        temp_surface = font.render(f'{player.name} (Team {player.team})', True, color)
        super().__init__(x, y, temp_surface.get_width(), temp_surface.get_height())
        self.player = player
        self.font = font
        self.color = color
        self.rotation = rotation

    def draw(self, screen):
        # Show name and team
        text = f"{self.player.name} (Team {self.player.team})"
        text_surface = self.font.render(text, True, self.color)

    # rotate if needed
        if self.rotation != 0:
            text_surface = pygame.transform.rotate(text_surface, self.rotation)

        screen.blit(text_surface, (self.rect.x, self.rect.y))

def load_image_safe(image_path, width=None, height=None):
    # exception handling for image loading. Returns image or fallback surface."""

        try:
            image = pygame.image.load(image_path)
            if width and height:
                image = pygame.transform.scale(image, (width, height))
            return image
        except (pygame.error, FileNotFoundError) as e:
            print(f"Error loading image {image_path}: {e}")
            # Return a fallback surface
            size = (width or 50, height or 50)
            fallback = pygame.Surface(size)
            fallback.fill((0, 0, 0))
            return fallback


def create_bid_buttons(bid_images, y_position=300):
    """Create all bid buttons and return them in a dictionary"""
    buttons = {}
    x_positions = {
        30: 350,
        31: 450,
        32: 550,
        84: 650,
        'pass': 750
    }

    for bid_value, x_pos in x_positions.items():
        if bid_value == 'pass':
            width = 65
        else:
            width = 50
        buttons[bid_value] = ImageButton(x_pos, y_position, width, 50, bid_images[bid_value])

    return buttons


def create_trump_buttons(trump_images, y_position=400):
    """Create all trump buttons and return them in a dictionary"""
    buttons = {}
    x_positions = {
        0: 200,
        1: 275,
        2: 350,
        3: 425,
        4: 500,
        5: 575,
        6: 650,
        'no_trump': 750
    }

    for trump_value, x_pos in x_positions.items():
        if trump_value == 'no_trump':
            width = 120
        else:
            width = 50
        buttons[trump_value] = ImageButton(x_pos, y_position, width, 50, trump_images[trump_value])

    return buttons