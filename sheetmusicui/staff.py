import pygame
from pygame import Rect, transform, image
from sheetmusicui.style import colors
from sheetmusicui import notes


class Staff():
    """Staff that manages notes inside it"""
    STAFF_LINE_INTERVAL = 30  # Pixel interval between staff lines
    STAFF_LINE_PIXEL_WIDTH = 2  # Width in Pixel of staff line

    TREBLE_CLEF_FILE = "./assets/treble-clef.png"
    BASS_CLEF_FILE = "./assets/bass-clef.png"

    def __init__(self, clef=None, width=200, x=0, y=0):
        """
        Initializer
        :param type:    String. 'treble' or 'bass'.
        :param width:   Int. Width of entire staff.
        :param x:       Int. X-position of staff.
        :param y:       Int. Y-position of staff
        """
        self.clef = clef
        self.notes = []
        self.width = width
        self.x = x
        self.y = y

    def get_pos(self):
        """Returns tuple of staff position"""
        return self.x, self.y

    def _draw_notes(self):
        """Draw notes into the staff"""
        for note in self.notes:
            pass

    def draw(self, surface):
        """
        Draws the staff into the target surface
        :param surface:     PyGame Surface to draw on
        """
        # TODO: Store staff lines into Surface member of this class instead of drawing every time
        # Draw Rectangle bounding box of staff
        pygame.draw.rect(surface,
                         colors['BLACK'],
                         Rect(self.get_pos(), (self.width, Staff.STAFF_LINE_INTERVAL * 4)),
                         Staff.STAFF_LINE_PIXEL_WIDTH)

        # Draw Inner Lines
        for i in range(1, 4):
            pygame.draw.line(surface,
                             colors['BLACK'],
                             (self.x, self.y + self.STAFF_LINE_INTERVAL * i),
                             (self.x + self.width, self.y + self.STAFF_LINE_INTERVAL * i),
                             self.STAFF_LINE_PIXEL_WIDTH)

        # Draw the clefs
        if self.clef == 'treble':
            clef = image.load(self.TREBLE_CLEF_FILE)
            original_size = clef.get_size()
            clef = transform.smoothscale(clef, (int(original_size[0] * 0.13),
                                                int(original_size[1] * 0.13)))
            surface.blit(clef, (self.x, self.y - 20))
        elif self.clef == 'bass':
            clef = image.load(self.BASS_CLEF_FILE)
            original_size = clef.get_size()
            clef = transform.smoothscale(clef, (int(original_size[0] * 0.2),
                                                int(original_size[1] * 0.2)))
            surface.blit(clef, (self.x, self.y + 10))
        else:
            pass


class GrandStaff:
    """Class for grand staff"""
    def __init__(self, width=200, x=0, y=0):
        """
        :param width:   Width of grand staff
        :param x:       x position
        :param y:       y position
        """
        self.treble_clef = Staff('treble', width, x, y)
        self.bass_clef = Staff('bass', width, x, 180 + y)

    def draw(self, surface):
        """
        Draw the grand staff + notes
        :param surface: Pygame Surfae to draw the staffs to
        """
        self.treble_clef.draw(surface)
        self.bass_clef.draw(surface)
