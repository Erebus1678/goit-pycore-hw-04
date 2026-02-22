from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats: List[Dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for _, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    continue

                cat_id, name, age = parts

                cat_id = cat_id.strip()
                name = name.strip()
                age = age.strip()

                if not cat_id or not name or not age:
                    continue

                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не знайдено: {path}") from e
    except OSError as e:
        raise OSError(f"Помилка при роботі з файлом: {e}") from e

    return cats



result = get_cats_info("task2/cats.txt")
print(result)