

DEFAULT_WORK_TIME = 1  # 25
DEFAULT_SHORT_BREAK = 1 # 5
DEFAULT_LONG_BREAK = 1 # 15
DEFAULT_NO_OF_CYCLES = 3

import os
import time

def play_sound(title, message):
    try:
        os.system('afplay /System/Library/Sounds/Ping.aiff 2> /dev/null || echo -e "\a"')
        # os.system(f'notify-send "{title}" "{message}"')
    except Exception as e:
        print(e)
        print('\a')


def start_the_timer(timer_minute):
    timer_second = timer_minute
    while timer_second > 0:
        minutes = timer_second // 60
        seconds = timer_second % 60
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
        timer_second -=1

    play_sound("Time Up",f"Pomodoro Timer of '{timer_minute} minutes'completed")


def start_pomodoro():
    print(f" -- Pomodoro timer started -- ")
    current_cycle = 0
    short_break = 0

    while current_cycle < DEFAULT_NO_OF_CYCLES:

        start_the_timer(DEFAULT_WORK_TIME)
        current_cycle+=1
        print(f"Pomodoro timer cycle '{current_cycle}' of '{DEFAULT_NO_OF_CYCLES}' finished.")

        if current_cycle == DEFAULT_NO_OF_CYCLES:
            print(f"Pomodoro timer cycle {current_cycle} of {DEFAULT_NO_OF_CYCLES} completed. \nYou can take a Long break of {DEFAULT_LONG_BREAK} minutes")
            start = input("Do you want to start the short break now ? (Y/N) ")
            if start.lower() == 'y':
                start_the_timer(DEFAULT_LONG_BREAK)
            break
    
        print(f"\nYou can take a Short break '{short_break+1}' of '{DEFAULT_NO_OF_CYCLES}' for '{DEFAULT_SHORT_BREAK}' minutes")
        start = input("Do you want to start the short break now ? (Y/N) ")
        if start.lower() == 'y':
            start_the_timer(DEFAULT_SHORT_BREAK)
            short_break+=1
        start = input("Do you want to start the next cycle of Pomodoro timer now ? (Y/N) ")
        if start.lower() != 'y':
            break


def main():
    print("*"*10 + "The Pomodoro Technique:" + "*"*10)
    print("1. Choose a task to work on\n2. Work for 25 minutes (one Pomodoro)\n3. Take a 5-minute short break\n4. After 3 Pomodoros, take a 15-minute long break")
    start = input("Do you want to start the Pomodoro Timer ? (Y/N) ")

    if start.lower() == 'y':
        start_pomodoro()
        restart = input("Do you want to restart the Pomodoro Timer with another Task ? (Y/N) ")
        if restart.lower() == 'y':
            start_pomodoro()
    print("Thank you for using the Pomodoro Timer. Stay productive!")
   
if __name__ == '__main__':
    main()
