import time


def time_regulator(time_max, start_time):
    time_diff = time.time() - start_time
    print("--- Image processing weight %.3f s ---" % time_diff)
    if time_diff < time_max:
        time.sleep(time_max - time_diff)
    else:
        print("### WARNING, PROCESSING TIME TOO LARGE ###")
