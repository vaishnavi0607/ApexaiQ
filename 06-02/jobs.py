import requests
import json

class JobsAPI:
    def __init__(self, api_key, api_host):
        self.api_key = api_key
        self.api_host = api_host
        self.base_url = "https://active-jobs-db.p.rapidapi.com/active-ats-7d"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.api_host
        }

    def fetch_jobs(self, title_filter, location_filter, limit, date_filter):
        querystring = {
            "title_filter": title_filter,
            "location_filter": location_filter,
            "limit": limit,
            "date_filter": date_filter
        }
        response = requests.get(self.base_url, headers=self.headers, params=querystring)
        print(json.dumps(response.json(), indent=4))
        return response.json()

    def save_to_file(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


jobs_api = JobsAPI("944ff58fe7mshd12b6e6d37f3870p1a8080jsna7dd2eb5760d","active-jobs-db.p.rapidapi.com")
jobs_data = jobs_api.fetch_jobs("software engineer","India","20","2025-01-01")
jobs_api.save_to_file(jobs_data, "jobs_data.json")