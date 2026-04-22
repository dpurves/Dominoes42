# DominoTile Class
class DominoTile:
    def __init__(self, image, name, hi_num, lo_num, count, is_double):
        self.image = image
        self.name = name
        self.hi_num = hi_num
        self.lo_num = lo_num
        self.count = count
        self.is_double = is_double
        self.rect = None

    def __str__(self):
        return f"Domino {self.name}: high={self.hi_num}, low={self.lo_num}, count={self.count}"

    def has_number(self, num):
        return self.hi_num == num or self.lo_num == num

    def is_trump(self, trump_num):
        return self.has_number(trump_num)

    def get_non_trump_num(self, trump):
        if self.hi_num == trump:
            return self.lo_num
        elif self.lo_num == trump:
            return self.hi_num
        else:
            return -1

    def get_non_lead_num(self, lead_suit):
        if self.hi_num == lead_suit:
            return self.lo_num
        else:
            return self.hi_num



# Creates and returns all 28 dominoes in a standard double-six set
def create_domino_set():
    all_dominoes = [
    DominoTile("images/Domino00.png", "0-0", 0, 0, 0, is_double=True),
    DominoTile("images/Domino01.png", "0-1", 1, 0, 0, is_double=False),
    DominoTile("images/Domino02.png", "0-2", 2, 0, 0, is_double=False),
    DominoTile("images/Domino03.png", "0-3", 3, 0, 0, is_double=False),
    DominoTile("images/Domino04.png", "0-4", 4, 0, 0, is_double=False),
    DominoTile("images/Domino05.png", "0-5", 5, 0, 5, is_double=False),
    DominoTile("images/Domino06.png", "0-6", 6, 0, 0, is_double=False),
    DominoTile("images/Domino11.png", "1-1", 1, 1, 0, is_double=True),
    DominoTile("images/Domino12.png", "1-2", 2, 1, 0, is_double=False),
    DominoTile("images/Domino13.png", "1-3", 3, 1, 0, is_double=False),
    DominoTile("images/Domino14.png", "1-4", 4, 1, 5, is_double=False),
    DominoTile("images/Domino15.png", "1-5", 5, 1, 0, is_double=False),
    DominoTile("images/Domino16.png", "1-6", 6, 1, 0, is_double=False),
    DominoTile("images/Domino22.png", "2-2", 2, 2, 0, is_double=True),
    DominoTile("images/Domino23.png", "2-3", 3, 2, 5, is_double=False),
    DominoTile("images/Domino24.png", "2-4", 4, 2, 0, is_double=False),
    DominoTile("images/Domino25.png", "2-5", 5, 2, 0, is_double=False),
    DominoTile("images/Domino26.png", "2-6", 6, 2, 0, is_double=False),
    DominoTile("images/Domino33.png", "3-3", 3, 3, 0, is_double=True),
    DominoTile("images/Domino34.png", "3-4", 4, 3, 0, is_double=False),
    DominoTile("images/Domino35.png", "3-5", 5, 3, 0, is_double=False),
    DominoTile("images/Domino36.png", "3-6", 6, 3, 0, is_double=False),
    DominoTile("images/Domino44.png", "4-4", 4, 4, 0, is_double=True),
    DominoTile("images/Domino45.png", "4-5", 5, 4, 0, is_double=False),
    DominoTile("images/Domino46.png", "4-6", 6, 4, 10, is_double=False),
    DominoTile("images/Domino55.png", "5-5", 5, 5, 10, is_double=True),
    DominoTile("images/Domino56.png", "5-6", 6, 5, 0, is_double=False),
    DominoTile("images/Domino66res2.png", "6-6", 6, 6, 0, is_double=True),
    ]
    return all_dominoes