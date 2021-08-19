# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        pass

    def get_masked_word(self):
        return len(self.word) * '_'

    def get_status(self):
        return self.status
