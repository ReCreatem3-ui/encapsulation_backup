import os
import time
from fan import Fan

class Spacer:
    """Utility class to print a spacer line."""
    
    @staticmethod
    def equal_spacer(count = 60):
        return "=" * count

    def dash_spacer(count = 60):
        return "-" * count

    def one_line_spacer():
        print()
    
    def small_spacer():
        for i in range(3):
            print()

    def medium_spacer():
        for i in range(5):
            print()

    def large_spacer():
        for i in range(10):
            print()

    def big_spacer():
        for i in range(20):
            print()

    def screen_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Effects:
    """Utility class to print various effects"""
    
    @staticmethod
    def slowtype(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class ASCIIArt:
    """Utility class to return ASCII art strings."""
    def title():
        return("""                             /$$$$$$$$                        /$$$$$$  /$$                         /$$             /$$                        
                                | $$_____/                       /$$__  $$|__/                        | $$            | $$                        
                                | $$    /$$$$$$  /$$$$$$$       | $$  \__/ /$$ /$$$$$$/$$$$  /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
                                | $$$$$|____  $$| $$__  $$      |  $$$$$$ | $$| $$_  $$_  $$| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
                                | $$__/ /$$$$$$$| $$  \ $$       \____  $$| $$| $$ \ $$ \ $$| $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
                                | $$   /$$__  $$| $$  | $$       /$$  \ $$| $$| $$ | $$ | $$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
                                | $$  |  $$$$$$$| $$  | $$      |  $$$$$$/| $$| $$ | $$ | $$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
                                |__/   \_______/|__/  |__/       \______/ |__/|__/ |__/ |__/ \______/ |__/ \_______/   \___/   \______/ |__/      """)

    def fan_model():
        return("""⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                ⢀⣀⣤⣤⠤⢤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠁⠀⠀⢀⣤⠤⢤⣬⣉⡛⠶⣄⡀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠈⠙⠳⣬⡙⣦⡀⠀⠀⠀
                                                                        ⠀⠀⢠⡞⠁⠀⢀⣀⣀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⢻⡌⢳⡄⠀⠀
                                                                        ⠀⢠⡟⣠⡴⠛⠉⠉⠉⠉⠓⢦⣄⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⡇⠀⢹⡄⠀
                                                                        ⠀⡾⢰⠏⠀⠀⠀⠀⠀⠀⠀⣠⡽⠷⠶⢧⣄⠀⠀⠀⠀⠀⣸⠇⠀⠀⢿⠀
                                                                        ⢸⡇⣾⠀⠀⠀⠀⠀⠀⠀⢰⠋⣰⠞⠲⣦⠙⣆⠀⠀⢀⡴⠋⠀⠀⠀⢸⡇
                                                                        ⢸⡇⢹⠀⠀⠀⠀⠀⣠⡴⢿⡀⢿⣀⣀⡾⢀⡿⠶⠚⠉⠀⠀⠀⠀⠀⢸⡇
                                                                        ⠈⣧⠸⣇⠀⠀⢀⡾⠁⠀⠀⡿⢦⣤⣥⡴⢿⣀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁
                                                                        ⠀⠸⡆⠙⢦⡤⠞⠁⠀⠀⢸⡇⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⢦⡀⠀⢰⠇⠀
                                                                        ⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⣠⠏⠀⠀
                                                                        ⠀⠀⠀⠘⢷⣄⠀⠀⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⢀⣠⠞⣁⡼⠃⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠉⠳⣤⣀⠀⠀⠀⠈⠛⠶⣤⣤⡴⠞⣋⣥⠞⠉⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⠶⠦⠤⠤⠴⠶⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⣀⣀⣀⣀⣹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⣀⡤⠶⠚⠋⠉⠉⠉⠉⠉⠉⠉⠉⠙⠓⠶⢤⣀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⡾⠁⠀⢠⡄⠀⣤⠀⢠⡄⠀⣤⠀⠀⡴⢶⡄⠀⠈⢷⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠠⡇⠀⠀⠀⠃⠀⠙⠀⠘⠁⠀⠋⠀⠀⠙⠚⠁⠀⠀⢸⡃⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠛⠚⠓⠛⠓⠛⠛⠚⠓⠛⠚⠓⠛⠚⠓⠛⠚⠛⠒⠛⠀⠀⠀⠀
                """)
    
