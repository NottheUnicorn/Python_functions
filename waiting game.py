import time
import random



def wait_game():
    target = random.randint(2,4)
    print('\n Your target time is {} second'.format(target))

    input('Press Enter to Begin Please!!!!!!!!!')
    start = time.perf_counter()

    input('\n........Press Enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start

    print('/nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('(Awesome...Perfect Timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))


wait_game()