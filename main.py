from datetime import datetime
import time as t
import os
import math

# Global color variable to keep track of current color settings
current_color = "\033[0m"  # Default color (no effect)

# Helper functions
def get_greeting(hour):
    if 4 < hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Night"

def date_time(cmd):
    global current_color
    month_dict = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April', 
        '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    day_dict = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }
    now = datetime.now()
    date, time = now.date(), now.time()
    hour = now.hour
    greet = get_greeting(hour)
    date_str = f'{date.day} {month_dict[str(date.month).zfill(2)]} {date.year}, {day_dict[date.isoweekday()]}'

    if "date" in cmd:
        print(f'{current_color}Date is: {date_str}\033[0m')
    elif "time" in cmd:
        print(f'{current_color}Time is: {hour % 12 or 12} O` Clock and {time.minute} minutes of {greet}.\033[0m')
    else:
        print(f"{current_color}Please enter a valid command for date or time.\033[0m")

def color():
    global current_color
    txtcolor_dict = {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 
        'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37
    }
    effect_dict = {
        'no effect': 0, 'bold': 1, 'underline': 2, 'negative1': 3, 'negative2': 5
    }
    bkg_color_dict = {
        'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 
        'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47
    }

    def get_input(options, prompt):
        while True:
            choice = input(prompt).strip().lower()
            if choice in options:
                return options[choice]
            elif choice == "help":
                print(f"{current_color}Available options: {', '.join(options.keys())}\033[0m")
            else:
                print(f"{current_color}Invalid choice. Type 'help' for options.\033[0m")

    txt_color = get_input(txtcolor_dict, 'Enter the text color: ')
    effect = get_input(effect_dict, 'Enter the effect (no effect, bold, underline): ')
    bkg_color = get_input(bkg_color_dict, 'Enter the background color: ')
    # Update global color code
    current_color = f"\033[{effect};{txt_color};{bkg_color}m"
    print(f"{current_color}Color applied successfully! This color will persist until changed.\033[0m")

def wish():
    hour = datetime.now().hour
    greet = get_greeting(hour)
    print(f"{current_color}Good {greet.lower()} sir!   \nHow can I help you??\033[0m")

def factorial():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        result = math.factorial(num)
        print(f"{current_color}The factorial of {num} is {result}\033[0m")
    except ValueError:
        print(f"{current_color}Please enter a valid integer.\033[0m")

def date_difference():
    try:
        date_format = "%Y-%m-%d"
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")
        delta = abs((datetime.strptime(date1, date_format) - datetime.strptime(date2, date_format)).days)
        print(f"{current_color}The difference between the dates is {delta} days.\033[0m")
    except ValueError:
        print(f"{current_color}Please enter dates in the correct format.\033[0m")

def set_reminder():
    try:
        reminder_time = int(input("Set a reminder in seconds: "))
        message = input("Enter a reminder message: ")
        print(f"{current_color}Reminder set!\033[0m")
        t.sleep(reminder_time)
        print(f"\n{current_color}⏰ Reminder: {message}\033[0m")
    except ValueError:
        print(f"{current_color}Please enter a valid time in seconds.\033[0m")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main interaction function
def main():
    wish()
    
    while True:
        cmd = input(f'{current_color}\n\t✒ Enter your command --> \033[0m').strip().lower()
        try:
            if "date" in cmd or "time" in cmd:
                date_time(cmd)
            elif 'exit' in cmd or 'bye' in cmd:
                print(f"{current_color}Goodbye! Have a great day!\033[0m")
                wish()
                break
            elif 'color' in cmd or 'colour' in cmd:
                color()
            elif 'timer' in cmd:
                sec = int(input('Seconds: '))
                minutes = int(input('Minutes: '))
                hours = int(input('Hours: '))
                total_seconds = sec + (minutes * 60) + (hours * 3600)
                print(f"{current_color}Starting timer for {total_seconds} seconds...\033[0m")
                t.sleep(total_seconds)
                print(f"{current_color}Timer complete!\033[0m")
            elif 'menu' in cmd:
                print(f"{current_color}Specialty Menu:\n-> Change text color\n-> Time\n-> Set Reminder\n-> Calculate Factorial\n-> Date Difference Calculator\033[0m")
            elif 'factorial' in cmd:
                factorial()
            elif 'difference' in cmd:
                date_difference()
            elif 'reminder' in cmd:
                set_reminder()
            elif 'clear' in cmd:
                clear_screen()
            else:
                print(f"{current_color}Invalid command. Type 'menu' to see available options.\033[0m")
        except Exception as e:
            print(f"{current_color}An error occurred: {e}. Please follow the instructions.\033[0m")

if __name__ == "__main__":
    main()
