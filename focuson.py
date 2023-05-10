import time

def focus_timer(duration):
    while True:
        print("Focus timer started for {} minutes.".format(duration))
        time.sleep(duration*60)
        print("Time's up! Focus timer ended.")
