import json

# Load the JSON data from response.json
with open('response.json', 'r') as f:
    job_posts = json.load(f)  

# Test to check if job is from India
def test_job_location_from_india():
    for job_post in job_posts:  
        location_country = job_post["locations_raw"][0]["address"]["addressCountry"]
        assert location_country == "India", f"Expected 'India', but got '{location_country}'"

# Test to check if URL is provided
def test_job_url():
    for job_post in job_posts: 
        job_url = job_post.get("url")
        assert job_url is not None and job_url != "", "Job URL should be provided"