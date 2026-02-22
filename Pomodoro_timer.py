from plyer import notification
import time
from rich.progress import Progress

sessionCount = 0

def askUser():
    minutes = input('How many minutes would you like to work?\n')
    seconds = int(minutes) * 60
    shortBreakM = int(input('How long should your short break be in minutes?\n')) 
    shortBreak = shortBreakM * 60
    sessions = int(input('How many sessions do you want to have?\n'))
    start = input('Press Enter to start')

    return sessions, seconds, shortBreak   
    
def Timer(seconds):
    with Progress() as progress:
        task = progress.add_task("[cyan]Counting down...", total=seconds)
        
        while not progress.finished:
            time.sleep(1)
            progress.update(task, advance=1)

def notify_user(title, message):
    print('\a') # Porduces a sound to warn
    notification.notify(
        title=title,
        message=message,
        app_name="Pomodoro Timer",
        timeout=10
    )


sessions, seconds, shortBreak = askUser()

while True:
    Timer(seconds)
    sessionCount += 1

    if sessionCount == sessions:
        sessionCount = 0
        notify_user('Timer completed', 'All sessions completed!')
        break
        

    else:
        notify_user('Break time! ☕', f'Session {sessionCount} completed, {int(shortBreak / 60)} minutes break!')
        print('Break time! ☕\n')

        Timer(shortBreak)
        
    notify_user('Break Over', f'Back to work! Session {sessionCount + 1} starting now!')
    print('Break over! Back to work!\n')





