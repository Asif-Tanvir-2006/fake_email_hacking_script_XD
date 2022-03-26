from random import randint, choice
from time import sleep

BANNER = """
 _______       ___           _______. __    __        .______   ____    ____ 
|       \     /   \         /       ||  |  |  |       |   _  \  \   \  /   /        
|  .--.  |   /  ^  \       |   (----`|  |__|  |       |  |_)  |  \   \/   /  
|  |  |  |  /  /_\  \       \   \    |   __   |       |   ___/    \_    _/   
|  '--'  | /  _____  \  .----)   |   |  |  |  |       |  |          |  |      
|_______/ /__/     \__\ |_______/    |__|  |__|  _____| _|          |__|     
                                                                    
   ____     ___           _______. __   _______                              
  / __ \   /   \         /       ||  | |   ____|                             
 / / _` | /  ^  \       |   (----`|  | |  |__                                
| | (_| |/  /_\  \       \   \    |  | |   __|                               
 \ \__,_/  _____  \  .----)   |   |  | |  |                                  
  \____/__/     \__\ |_______/    |__| |__|                                  
                                                                                                                  
                             
                       ______
                    .-"      "-.
                   /            |
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)   
"""

# Lists, for email generation
FIRST_NAMES = [
    "olivia", 
    "emma", 
    "amelia", 
    "ava", 
    "sophia", 
    "charlotte", 
    "isabella", 
    "mia", 
    "luna", 
    "harper", 
    "liam", 
    "noah", 
    "oliver", 
    "elijah", 
    "lucas", 
    "levi", 
    "mason", 
    "asher", 
    "james", 
    "ethan", 
]

SURNAMES = [
    "smith",
    "johnson",
    "williams",
    "brown",
    "jones",
    "garcia",
    "miller",
    "davis",
    "rodriguez",
    "martinez",
    "hernandez",
    "lopez",
    "gonzales",
    "wilson",
    "anderson",
    "thomas",
    "taylor",
    "moore",
    "jackson",
    "martin",
]

EMAIL_PROVIDERS = [
    "gmail.com", 
    "outlook.com", 
    "yahoo.com", 
    "aol.com", 
    "yandex.com", 
]

# Color vars, for use in ctext function
COLOR_NORMAL = "\x1b[0m"
COLOR_RED = "\x1b[31m"
COLOR_GREEN = "\x1b[32m"
COLOR_YELLOW = "\x1b[33m"
COLOR_BLUE = "\x1b[34m"
COLOR_MAGENTA = "\x1b[35m"
COLOR_CYAN = "\x1b[36m"

# I put this here because it needs to be above the message variables +
# I don't know where else to put it. Move if you want.
def ctext(text, color=COLOR_NORMAL):
    """
    A simple function to create coloured text
    """
    # Add the ANSI modifier to the beginning, and append the regular 
    # modifier to the end so no problems stem later.
    return color + text + COLOR_NORMAL

# List of messages. 
MSG_STARTING = ctext("Starting attack...", COLOR_RED)
MSG_TARGET_LIST = ctext("Loading list of targets...")
MSG_FINDING_TARGET = ctext("Indexing target...", COLOR_MAGENTA)
MSG_RETRIEVING_CREDS = ctext("Retrieving data...", COLOR_CYAN)
MSG_FOUND_DATA = ctext("Found data! Email:", COLOR_BLUE)
MSG_CHECKING_VULNS = ctext("Checking possible vulnerabilities")
MSG_RETRIEVING_FAIL = ctext("Failed to retrieve credentials!", COLOR_RED)
MSG_RETRIEVING_SUCCESS = ctext("Succesfully retrieved credentials!", COLOR_GREEN)
MSG_CRACKING = ctext("Cracking hash...", COLOR_RED)
MSG_CRACKING_DONE = ctext("Cracked! Appended to cracked_hashes.txt", COLOR_GREEN)
MSG_PROCEEDING = ctext("Proceeding to next target")

def spinning_cursor(refreshes, delay=0.1):
    """
    A function to print an animated spinning cursor
    """
    # List of cursors. Though it looks weird, two backslashes are 
    # necessary (one to escape the other).
    cursor_list = "|/-\\"
    cursor_count = len(cursor_list)
    
    for i in range(refreshes):
        # Use modulo operator to get current cursor. 
        # TODO: Refactor later
        cursor = cursor_list[i % cursor_count]

        # Print backspace (to smoothen animation), then the cursor, 
        # then set the seperator & end to empty
        print("\b", cursor, sep="", end="", flush=True)

        sleep(delay)

    # Print an empty newline (to avoid problems)
    print()


def progress_bar(segments=20, delay=0.05):
    """
    A function to print an animated progress bar
    """
    # Progress bar should look like this:
    # [|||||               ] 25%

    # If the number of segments is not divisible by 100%
    if (100 % segments) != 0:
        raise ArithmeticError("100 is not divisible by number of segments")

    # Get quotient (what the % will increase by for each loop)
    quotient = 100 / segments
    for i in range(segments):
        # Store the progress + the percentage in variables for ease of
        # use
        progress = "❙" * (i+1)
        percent = int(quotient * (i+1))

        # Combine each part of the output seperately
        output = f"\r" # Carriage return (bring to start of line)
        output += f"[{progress:<{segments}}] " # Progress, padded to segments
        output += f"{percent}%" # Add the x% at the end
        print(output, end="", flush=True)

        sleep(delay)

    # Print an empty newline
    print()

def generate_email():
    first_name = choice(FIRST_NAMES)
    surname = choice(SURNAMES)
    random_number = randint(1, 100)
    email_provider = choice(EMAIL_PROVIDERS)

    return f"{first_name}.{surname}.{random_number}@{email_provider}"

def main():
    print(BANNER, "\n")

    sleep(5)

    print(MSG_STARTING)
    progress_bar()
    print()
    
    while True:
        print(MSG_TARGET_LIST, " ", end="")
        spinning_cursor(35)

        print(MSG_FINDING_TARGET, " ", end="")
        spinning_cursor(20)

        print(MSG_RETRIEVING_CREDS, " ", end="")
        spinning_cursor(10)

        print(MSG_FOUND_DATA, generate_email(), "\n")


        print(MSG_CHECKING_VULNS, " ", end="")
        spinning_cursor(10)

        if randint(1, 3) != 1:
            print(MSG_RETRIEVING_SUCCESS, "\n")

            print(MSG_CRACKING)
            progress_bar()

            print(MSG_CRACKING_DONE)
        else:
            print(MSG_RETRIEVING_FAIL)

        sleep(1)
        print(MSG_PROCEEDING)

if __name__ == "__main__": 
    main()
