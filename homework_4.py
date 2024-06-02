from pathlib import Path


def total_salary(name: Path):
    try:
        with open(name, mode='r') as file:
            total = 0
            avarage = 0
            caunter = 0
            for element in file:
                fam, salary = element.split(sep=',')
                salary = salary.strip()
                total += int(salary)
                caunter += 1
            avarage = total / caunter
        return total, avarage
    except FileNotFoundError:
        print(f' не існує файла')

if __name__ == '__main__':
    path = Path('files/some.txtyg')
    print(total_salary(path))
