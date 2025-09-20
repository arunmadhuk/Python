import os
import time

DEFAULT_WORK_TIME = 1  # 25
DEFAULT_SHORT_BREAK = 1 # 5
DEFAULT_LONG_BREAK = 1 # 15
DEFAULT_NO_OF_CYCLES = 3

def play_sound(title, message):
    print(f"play_sound function called")
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
    
def start_short_break():
    print(f"Short break started")
    break_timer_seconds = DEFAULT_SHORT_BREAK
    while break_timer_seconds > 0:
        minutes = break_timer_seconds // 60
        seconds = break_timer_seconds % 60
        print(f"{minutes:02d}:{seconds:02d}", end="\r") 
        time.sleep(1)
        break_timer_seconds -=1    
    play_sound("Time Up",f"Pomodoro Timer of '{DEFAULT_SHORT_BREAK} minutes'completed")


def start_long_break():
    print(f"Long break started")
    break_timer_seconds = DEFAULT_LONG_BREAK
    while break_timer_seconds > 0:
        minutes = break_timer_seconds // 60
        seconds = break_timer_seconds % 60
        print(f"{minutes:02d}:{seconds:02d}", end="\r") 
        time.sleep(1)
        break_timer_seconds -=1    
    play_sound("Time Up","Pomodoro Timer of '{DEFAULT_LONG_BREAK} minutes'completed")
    print("Long Break finisheds")
    
def start_pomodoro():
    print(f"Pomodoro timer started -- ")
    current_cycle = 1
    short_break = 1
    
    while current_cycle <= DEFAULT_NO_OF_CYCLES:
        print(f"current_cycle : {current_cycle}, DEFAULT_NO_OF_CYCLES : {DEFAULT_NO_OF_CYCLES}")
        start_the_timer(DEFAULT_WORK_TIME)
        print(f"Pomodoro timer cycle {current_cycle} of {DEFAULT_NO_OF_CYCLES} finished.")
        
        print("\nYou can take a Short break of {DEFAULT_SHORT_BREAK} minutes")
        if short_break <DEFAULT_NO_OF_CYCLES:
            start = input("Do you want to start the short break now ? (Y/N) ")
            if start.lower() == 'y':
                start_the_timer(DEFAULT_SHORT_BREAK)
            
            start = input("Do you want to start the next cycle of Pomodoro timer now ? (Y/N) ")
            if start.lower() == 'y':
                current_cycle+=1
                short_break+=1
            else:
                break
        elif short_break==DEFAULT_NO_OF_CYCLES:
            print(f"Pomodoro timer cycle {current_cycle} of {DEFAULT_NO_OF_CYCLES} completed. \nYou can take a Long break of {DEFAULT_LONG_BREAK} minutes")
            start = input("Do you want to start the short break now ? (Y/N) ")
            if start.lower() == 'y':
                start_the_timer(DEFAULT_LONG_BREAK)
                

    
def main():
    print("*"*10 + "The Pomodoro Technique:" + "*"*10)
    print("1. Choose a task to work on\n2. Work for 25 minutes (one Pomodoro)\n3. Take a 5-minute short break\n4. After 3 Pomodoros, take a 15-minute long break")
    start = input("Do you want to start the Pomodoro Timer ? (Y/N) ")

    if start.lower() == 'y':
        start_pomodoro()


if __name__ == '__main__':
    main()
