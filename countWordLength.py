__author__ = 'pstragie'

class CountLetters():
    """ Count letters script panel """
    def __init__(self, woord):
        self.woord = woord

    def countLettersInWord(self):
        count = len(self.woord)
        print("woord: ", self.woord)
        print("lengte: ", count)
        return count


if __name__ == '__main__':
    woord = "appel"
    CountLetters(woord).countLettersInWord()
