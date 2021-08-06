import Utils

def add_score(diff):
    POINTS_OF_WINNING = ((diff * 3) + 5)
    scores = open(Utils.SCORES_FILE_NAME, "a")
    scores.write('\n' + str(POINTS_OF_WINNING))
    scores.close()