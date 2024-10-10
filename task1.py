from pathlib import Path 

file_name = Path('./salary_file.txt')

def total_salary(path) -> str:
    if not file_name.exists():
        print(f"Файл {file_name} не знайдено.")
    else:
        print("Файл знайдено. Читаємо вміст...")

        total = 0
        count = 0

        with open(path, "r") as file:
            for line in file:
                salary = line.strip().split(',').pop(1)
                total += int(salary)
                count +=1
        
        average = int(total / count)
    return print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total_salary(file_name)