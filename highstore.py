import time


def game_time(start_time):

    end_time = time.time()
    time_ = round(end_time - start_time, 2)

    return time_