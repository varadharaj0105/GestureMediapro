import time

def cooldown_passed(last_time, cooldown=1.2):
    return time.time() - last_time > cooldown

def update_last_time():
    return time.time()
