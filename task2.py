from pathlib import Path
import re

cats_file = Path('./cats_file.txt')

def get_cats_info(path: str) -> list:
    '''
    Reads information about cats from a file cats_file.txt and returns their data.

    Parameters:
    file path(str) with information about cats
    Returns:
    list - with cats data
    '''
    result_obj = []
    pattern = r"(?P<id>[a-f0-9]+),(?P<name>[A-Z][a-z]+),(?P<age>\d+)"
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(pattern, line)
                # print(match)
                if match:
                    cat_id = match.group("id")
                    name = match.group("name")
                    age = int(match.group("age"))

                    result_obj.append({"id": cat_id, "name": name, "age": age})
        return result_obj
    except FileNotFoundError:
        print("File is not found") 
    except Exception:
        print("Other Errors")       


cats_info = get_cats_info(cats_file)
print(cats_info)
