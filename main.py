from highscoringwords import HighScoringWords

scoring_words = HighScoringWords()

print("The leaderboard for top scoring words for all the words is: ", scoring_words.build_leaderboard_for_word_list())
print()
print("The leaderboard for the top scoring words for the letters deora is: ",
      scoring_words.build_leaderboard_for_letters("deora"))
