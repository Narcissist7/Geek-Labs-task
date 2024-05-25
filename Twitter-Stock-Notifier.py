import time
import schedule
import subprocess
import itertools
import threading
import sys

def run_project():
    subprocess.run(['python', r'c:\Users\Adham Ashraf\Desktop\PythonApps\task.py'])

schedule.every(15).minutes.do(run_project)

def spinner():
    # Spinner animation function with an extended set of characters
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\', '◴', '◷', '◶', '◵', '⠁', '⠂', '⠄', '⠂', '⠁', '⠈', '⠉', '⠊', '⠋', '⠌', '⠍', '⠎', '⠏'])
    while True:
        sys.stdout.write(next(spinner_cycle) + '\r')
        sys.stdout.flush()
        time.sleep(0.1)

def countdown(minutes):
    # Countdown timer for the specified number of minutes
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        sys.stdout.write(f'Time remaining: {timer}  \r')
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    sys.stdout.write('Time remaining: 00:00  \n')
    sys.stdout.flush()

if __name__ == "__main__":
    run_project()
    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.daemon = True
    spinner_thread.start()

    # Infinite loop to keep running scheduled tasks and show countdown
    while True:
        schedule.run_pending()
        countdown(15)  # 15-minute countdown
        time.sleep(1)