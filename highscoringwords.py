__author__ = 'codesse'
"""
Python Version : 3.8
"""

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

        self.board_score = self._build_board_score_table()

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """

        return self._ordered_scored_words(self.board_score)

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """

        # Finds all available combinations from the letters provided as starting_letters
        letter_combinations = []

        def findCombs(curr_comb, letters):

            if curr_comb:
                letter_combinations.append(curr_comb)

            for i in range(len(letters)):
                findCombs(curr_comb + letters[i],
                          letters[:i] + letters[i + 1:len(letters)])

        findCombs("", starting_letters)

        # create a score table of words from the current list of words
        score_table = {}
        for combination in letter_combinations:
            if combination in self.board_score:
                score_table[combination] = self.board_score[combination]

        return self._ordered_scored_words(score_table)

    def _score_word(self, word):
        """
        return the score of a word
        :param word: a word
        :return: The score of word as an integer
        """
        score = 0
        for letter in word:
            score += self.letter_values[letter]

        return score

    def _build_board_score_table(self):
        """
        Builds the board table with all the scores
        :return: A dictionary of every word with the score
        """
        score_table = {}
        for word in self.valid_words:
            score_table[word] = self._score_word(word)

        return score_table

    def _ordered_scored_words(self, score_table):
        """

        :param words_list: Gets as an input the words
        :return: Returns a list with MAX_LEADERBOARD_LENGTH with list ordered first based on score desc and after
                alphabetically asc
        """
        return list(dict(sorted(score_table.items(), key=lambda item: (-item[1], item[0]))).keys())[
               :HighScoringWords.MAX_LEADERBOARD_LENGTH]
