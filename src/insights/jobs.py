from typing import List
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()
        self.jobs_type = list()
        self.jobs_filtered = list()
        self.delimiter = ','
        self.quotechar = '"'

    def read(self, path) -> List[dict]:
        with open(path, enconding='utf-8') as file:
            file_reader = csv.DictReader(file,
                                         delimiter=self.delimiter,
                                         quotechar=self.quotechar)
            self.jobs_list = list(file_reader)
            print(self.jobs_list[1])
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        jobs = [job["job_type"] for job in self.jobs_list]
        self.jobs_type = list(set(jobs))
        return self.jobs_type

    def filter_by_multiple_criteria(self, jobs, filter) -> List[dict]:
        if not isinstance(filter, dict):
            raise TypeError
        for key, value in filter.items():
            jobs = [job for job in jobs if job[key] == value if job[key] != '']

        self.jobs_filtered = jobs
        return self.jobs_filtered
