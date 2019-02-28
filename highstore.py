import time


def game_time(start_time):

    end_time = time.time()
    time_ = round(end_time - start_time, 2)

    return time_



def get_user_score(char_stats, play_time):
    final_score = str(int(char_stats["EXP"] * 3.14 * int(play_time)))

    return final_score


def print_score(char_stats, play_time, final_score):
    play_time = time.strftime('%H:%M:%S', time.gmtime(play_time))
    string = "\n\nYou played for {} and gainded {} EXP points. Your score is {}\n\n"
    formating = [play_time, char_stats["EXP"] + 10 * (char_stats["LVL"] - 1), final_score]
    print(string.format(*formating))



def save_final_score(file_name, user_score):
    with open(file_name, "a+") as my_file:
        user_score = ';'.join(user_score)
        my_file.write(user_score + "\n")