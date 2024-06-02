from pathlib import Path

def get_cats_info(name_of_file):
    try:
        with open(name_of_file, mode='r', encoding='utf-8') as file:
            information_cat =[]
            for element in file:
                id, name, age = element.split(sep=',')
                age = age.strip()
                cat_info ={
                    'id': id,
                    'name': name,
                    'age': age,
                }
                information_cat.append(cat_info)
            return information_cat

    except FileNotFoundError:
        print(f'Такого файла не існує')

if __name__ == "__main__":
    print(get_cats_info('cats.txt'))
