import pygame
from pygame import Rect, transform, image
from sheetmusicui.style import colors
from sheetmusicui import notes


class Staff:
    """Staff that manages notes inside it"""
    STAFF_LINE_INTERVAL = 30  # Pixel interval between staff lines
    STAFF_LINE_PIXEL_WIDTH = 2  # Width in Pixel of staff line

    TREBLE_CLEF_FILE = "./assets/treble-clef.png"
    BASS_CLEF_FILE = "./assets/bass-clef.png"

    # Lines starts from the 1st top ledger line of the staff to the 1st bottom ledger line
    # Spaces start from within the 1st outer ledger lines
    NOTES_POS = {
        "treble": {
            "lines": ['A5', 'F5', 'D5', 'B4', 'G4', 'E4', 'C4'],
            "spaces": ['G5', 'E5', 'C5', 'A4', 'F4', 'D4']
        },
        "bass": {
            "lines": ['C4', 'A3', 'F3', 'D3', 'B2', 'G2', 'E2'],
            "spaces": ['B3', 'G3', 'E3', 'C3', 'A2', 'F2']
        },
    }

    def __init__(self, clef='', width=200, x=0, y=0):
        """
        Initializer
        :param clef:    String. 'treble' or 'bass'.
        :param width:   Int. Width of entire staff.
        :param x:       Int. X-position of staff.
        :param y:       Int. Y-position of staff
        """
        self.clef = clef.lower()
        self.width = width
        self.x = x
        self.y = y
        self.notes_pos = Staff.NOTES_POS[clef]

    def get_pos(self):
        """Returns tuple of staff position"""
        return self.x, self.y

    def draw_note(self, note, surface, x=0):
        """
        draw a single note into the staff. checks if it's a valid note to be on staff.
        :param note: Note. note to draw
        :param surface: Pygame Surfae.
        :param x: int. pixel x-coord of note
        :return bool: If note was drawn by the staff.
        """
        gap = Staff.STAFF_LINE_INTERVAL
        pos = 0
        offset = 0
        if note.tone_str in self.notes_pos["lines"]:
            pos = self.notes_pos["lines"].index(note.tone_str)
            offset = (pos * gap) - gap
        elif note.tone_str in self.notes_pos["spaces"]:
            pos = self.notes_pos["spaces"].index(note.tone_str)
            offset = (pos * gap) - (gap/2)
        else:
            return False

        note.draw(surface, x, self.y + offset)
        return True

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
        self.treble_staff = Staff('treble', width, x, y)
        self.bass_staff = Staff('bass', width, x, 180 + y)

    def draw(self, surface):
        """
        Draw the grand staff + notes
        :param surface: Pygame Surfae to draw the staffs to
        """
        self.treble_staff.draw(surface)
        self.bass_staff.draw(surface)

    def draw_note(self, note, surface, x=0):
        """Try to draw the note to its respective staff."""
        if not self.treble_staff.draw_note(note, surface, x) \
                and not self.bass_staff.draw_note(note, surface, x):
            raise ValueError("No staff can draw {} note".format(note.tone_str))


class StaffManager:
    """Manages the staff and the notes inside, only one staff can be created at a time"""
    def __init__(self):
        self.staff = None
        self._notes = []
        self._max_notes = None

    def add_note(self, *args, **kwargs):
        """
        Add the notes to the Manager
        :param args: string or Notes.
        :param kwargs: 'note_type'. str tones in args will be created with this NoteType
        :return:
        """
        for note in args:
            if type(note) == notes.Note:
                self._notes.append(note)
            elif type(note) == str:
                if kwargs.get("note_type"):
                    self._notes.append(notes.Note(note, note_type=kwargs["note_type"]))
                else:
                    self._notes.append(notes.Note(note))

    def draw(self, surface):
        """Draw staff and notes"""
        # Draw staff
        self.staff.draw(surface)

        # Draw notes
        for i, note in enumerate(self._notes):
            self.staff.draw_note(note, surface, 130 + (i * 40))

    def init_grand_staff(self, **kwargs):
        self.staff = GrandStaff(**kwargs)

    def init_staff(self):
        # TODO
        pass


if __name__ == '__main__':
    staff_manager = StaffManager()
    staff_manager.init_grand_staff(width=700, x=20, y=20)
    pass
