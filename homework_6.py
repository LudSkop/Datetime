from colorama import Fore
from pathlib import Path

def scaner(path: Path):
    path = Path(path)
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.LIGHTGREEN_EX + f' {element}')
            scaner(element)
        else:
            print(Fore.LIGHTRED_EX + f' {element}')







if __name__ == "__main__":
    scaner('files')
