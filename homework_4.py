from pathlib import Path


def total_salary(name: Path):
    try:
        with open(name, mode='r') as file:
            total = 0
            counter = 0
            for element in file:
                fam, salary = element.split(sep=',')
                salary = salary.strip()
                total += int(salary)
                counter += 1
            average = total / counter
        return total, average
    except FileNotFoundError:
        print(f'Такого файла не існує')

if __name__ == '__main__':
    path = Path('files/some.txtyg')
    print(total_salary(path))
