import os
import requests
import json
from datetime import datetime, timezone

def fetch_submissions(subreddit, since, until):
    base_url = f'https://api.pullpush.io/reddit/submission/search?html_decode=True&subreddit={subreddit}&since={since}&until={until}&size=100'
    

    response = requests.get(base_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def format_time(input):
    utc_datetime = datetime.fromtimestamp(input, timezone.utc)
    formatted_time = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_time

subreddit = "comics"
since_timestamp = int(datetime(2023, 12, 4).timestamp())
until_timestamp = int(datetime(2024, 12, 4).timestamp())
headers = {'Content-Type': 'application/json'}
API_ENDPOINT = 'http://localhost:8000/api/'
RESPONSES_FOLDER = 'responses/'

data = fetch_submissions(subreddit, since_timestamp, until_timestamp)

if not os.path.exists(RESPONSES_FOLDER):
    os.makedirs(RESPONSES_FOLDER)

sets_array = data['data']

for index, item in enumerate(sets_array):

    try:
        timestamp_int = item['created_utc']
        formatted_created_utc = format_time(timestamp_int)
        item['created_utc'] = formatted_created_utc
    except:
        print("Created_UTC not found.")

    try:
        created = item['created']
        formatted_created = format_time(created)
        item['created'] = formatted_created
    except:
        print("Create key not found.")

    json_data = json.dumps(item)

    response = requests.post(API_ENDPOINT, headers=headers, data=json_data)
    if response.status_code == 201:
        print("All ok!")

    else:
        print(f"Not ok - {response.status_code} - {response.text}")

    response_filename = f"{RESPONSES_FOLDER}response_{index}.json"
    save_to_json(response.json(), response_filename)

save_to_json(data, 'Updated_AbandonedPorn_submissions.json')