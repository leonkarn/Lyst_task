__author__ = 'codesse'


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """

        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

        self.words_set = set(self.valid_words)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """

        """ dictionary solution """

        return self.ordered_scored_words(self.valid_words)

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """

        # updates the combs with all the permutations
        combs = []
        def findCombs(curr_comb, letters):

            if curr_comb:
                combs.append(curr_comb)

            for i in range(len(letters)):
                findCombs(curr_comb + letters[i],
                          letters[:i] + letters[i + 1:len(letters)])

        # find all possible combinations from the strings
        findCombs("", starting_letters)

        # return only those that are in set
        return self.ordered_scored_words([word for word in combs if word in self.words_set])

    def score_word(self, word):
        """
        return the score of a word
        :param word: a word
        :return: The score of word
        """
        score = 0
        for letter in word:
            score += self.letter_values[letter]

        return score

    def ordered_scored_words(self, words_list):
        """

        :param words_list: Gets as an input the words
        :return: Returns a list with MAX_LEADERBOARD_LENGTH with list ordered first based on score desc and after
                alphabetically asc
        """
        score_board = {}
        for word in words_list:
            score_board[word] = self.score_word(word)

        return list(dict(sorted(score_board.items(), key=lambda item: (-item[1], item[0]))).keys())[
               :HighScoringWords.MAX_LEADERBOARD_LENGTH]
