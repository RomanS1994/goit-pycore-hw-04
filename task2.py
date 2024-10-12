from pathlib import Path
import re

cats_file = Path('./cats_file.txt')

def get_cats_info(path):
    
    result_obj = []
    pattern = r"(?P<id>[a-f0-9]+),(?P<name>[A-Z][a-z]+),(?P<age>\d+)"

    # Відкриваємо файл у режимі читання
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line)
            # print(match)
            if match:
                cat_id = match.group("id")
                name = match.group("name")
                age = int(match.group("age"))
                # Додаємо дані про котів у результат
                result_obj.append({"id": cat_id, "name": name, "age": age})
                
    return result_obj

cats_info = get_cats_info(cats_file)
print(cats_info)
