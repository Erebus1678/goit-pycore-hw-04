import sys
from pathlib import Path
from colorama import Fore, Style, init


INDENT = " " * 4  # 4 пробіли на рівень вкладеності


def print_tree(root: Path) -> None:
    root = root.resolve()

    # Друкуємо корінь
    print(Fore.BLUE + f"{root.name}/" + Style.RESET_ALL)

    def walk(current: Path, level: int) -> None:
        try:
            entries = list(current.iterdir())
        except PermissionError:
            print(INDENT * level + Fore.RED + "[permission denied]" + Style.RESET_ALL)
            return

        for entry in entries:
            prefix = INDENT * level

            if entry.is_dir():
                print(prefix + Fore.BLUE + f"{entry.name}/" + Style.RESET_ALL)
                walk(entry, level + 1)
            else:
                print(prefix + Fore.GREEN + entry.name + Style.RESET_ALL)

    walk(root, 1)


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Помилка: шлях не існує -> {path}" + Style.RESET_ALL)
        return

    if not path.is_dir():
        print(Fore.RED + f"Помилка: вказаний шлях не є директорією -> {path}" + Style.RESET_ALL)
        return

    print_tree(path)