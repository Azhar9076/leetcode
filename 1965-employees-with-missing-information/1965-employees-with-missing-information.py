import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    a = employees.merge(salaries, on = 'employee_id', how='left')
    b = salaries.merge(employees, on = 'employee_id', how='left')

    result = pd.concat([a[a.salary.isna()][['employee_id']],
                       b[b.name.isna()][['employee_id']]
    ])
    return result.sort_values(by='employee_id')