from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()
    industry = list()

    def get_unique_industries(self) -> List[str]:
        jobs = [job["industry"]
                for job in self.jobs_list if job['industry'] != '']
        self.industry = list(set(jobs))
        print(self.industry)
        return self.industry
