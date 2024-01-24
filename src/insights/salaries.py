from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [int(job['max_salary'])
                    for job in self.jobs_list if job["max_salary"].isdigit()]
        max_salary = max(list(salaries))
        self.max_salary = max_salary
        return self.max_salary

    def get_min_salary(self) -> int:
        salaries = [int(job['min_salary'])
                    for job in self.jobs_list if job["min_salary"].isdigit()]
        min_salary = min(list(salaries))
        self.min_salary = min_salary
        return self.min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
