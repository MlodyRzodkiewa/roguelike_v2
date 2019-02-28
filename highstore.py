import time
import rogal


def game_time(start_time):

    end_time = time.time()
    time_ = round(end_time - start_time, 2)

    return time_


def get_user_score(char_stats, play_time):
    final_score = str(int(char_stats["exp"] * 3 * int(len(rogal.otherlist) * 5)))

    return final_score


def game_time():
        second = 0
        while True:
                second += 1
                time.sleep(1)
        return seconds


def print_score(char_stats, play_time):
    string = "\n\nYou played for {} seconds and gainded {} EXP points. Your score is {}\n\n"
    formating = [play_time, char_stats["exp"] + 10 * (char_stats["lvl"] - 1), get_user_score(char_stats, play_time)]
    print(string.format(*formating))


def save_final_score(file_name, user_score):
    with open(file_name, "a+") as my_file:
        user_score = ';'.join(user_score)
        my_file.write(user_score + "\n")
