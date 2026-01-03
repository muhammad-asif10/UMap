from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Colors:
    SUCCESS = Fore.GREEN + Style.BRIGHT
    ERROR = Fore.RED + Style.BRIGHT
    INFO = Fore.CYAN + Style.BRIGHT
    WARNING = Fore.YELLOW + Style.BRIGHT
    PATH = Fore.MAGENTA + Style.BRIGHT
    RESET = Style.RESET_ALL
