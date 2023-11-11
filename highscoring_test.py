import unittest
from highscoringwords import HighScoringWords


class TestHighScoringWords(unittest.TestCase):
    def setUp(self):
        self.high_scoring_words = HighScoringWords()

    def test_build_leaderboard_for_word_list(self):
        leaderboard = self.high_scoring_words.build_leaderboard_for_word_list()
        self.assertEqual(leaderboard[0],"razzamatazzes")
        self.assertEqual(100, len(leaderboard))

    def test_build_leaderboard_for_letters(self):
        starting_letters = 'deo'
        leaderboard = self.high_scoring_words.build_leaderboard_for_letters(starting_letters)
        self.assertEqual(['doe', 'ode', 'de', 'do', 'ed', 'od', 'oe'], leaderboard)

    def test_score_word(self):
        word_score = self.high_scoring_words._score_word('apple')
        self.assertEqual(9, word_score)

    def test_build_board_score_table(self):
        board_score = self.high_scoring_words._build_board_score_table()
        self.assertEqual(board_score["razzamatazzes"],51)
        self.assertEqual(len(board_score), len(self.high_scoring_words.valid_words))

    def test_ordered_scored_words(self):
        # Mock a score table for testing
        score_table = {'word1': 3, 'word2': 8, 'word4': 5}
        result = self.high_scoring_words._ordered_scored_words(score_table)
        self.assertEqual(result, ['word2', 'word4', 'word1'])


if __name__ == '__main__':
    unittest.main()
