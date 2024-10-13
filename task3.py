import sys
from pathlib import Path
from colorama import Fore, init


init(autoreset=True)

def print_directory_structure(directory: Path, indent_level=0):
    if not directory.is_dir():
        print(Fore.RED + f"{directory} не є директорією.")
        return

    for item in directory.iterdir():
        indent = "    " * indent_level
        if item.is_dir():
            print(Fore.BLUE + f"{indent}[DIR] {item.name}")
            print_directory_structure(item, indent_level + 1)
        else:
            print(Fore.GREEN + f"{indent}[FILE] {item.name}")



# directory_path = Path('/Users/romanstrizhko/Documents/GitHub/projectsGoIT/')
try:
    directory_path = Path(sys.argv[1])
    print_directory_structure(directory_path)

except Exception as e:
    print(Fore.RED + f"Сталася помилка: {e}")


