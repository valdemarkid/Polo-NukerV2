from pystyle import Add, Center, Anime, Colors, Colorate
import time
import sys
import ctypes
import os
import subprocess
ctypes.windll.kernel32.SetConsoleTitleW(" ! PRESS ENTER ! ")
ascii_art = """
                                ██████╗  ██████╗ ██╗      ██████╗ 
                                ██╔══██╗██╔═══██╗██║     ██╔═══██╗
                                ██████╔╝██║   ██║██║     ██║   ██║
                                ██╔═══╝ ██║   ██║██║     ██║   ██║
                                ██║     ╚██████╔╝███████╗╚██████╔╝
                                ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝                                    
"""
cursor_prompt = "user@death-raider >"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def set_terminal_title(title):
    if os.name == 'nt':  
        os.system(f'title {title}')
    else:  
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()
def typing_effect(text, delay=0.05):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
def main():
    set_terminal_title("@PRESS-ENTER>")
    clear_screen()
    Anime.Fade(Center.Center(ascii_art), Colors.red_to_black, Colorate.Vertical, interval=0.030, enter=True)
    try:
        subprocess.run(['main.exe'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()