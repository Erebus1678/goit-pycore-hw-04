from pathlib import Path
from typing import Tuple

def total_salary(path: str| Path) -> Tuple[int, float]:

        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                clear_line = line.strip()
                if not clear_line:
                    continue
                
                try:
                    parts = clear_line.split(',')
                    if len(parts) != 2:
                        print(f"Invalid format in line {clear_line}")
                        continue
                    else:
                        salary = int(parts[1].strip())
                    
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid integer and will be skipped.")
                    
            if count == 0:
                raise ValueError("No valid salary entries found in the file.")
            avg = total / count 
        return (total, avg)
    
        
salary_txt = Path('./task_1/salary.txt')
print(total_salary(salary_txt))