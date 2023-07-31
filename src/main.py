import requests
import schedule
import time
from plyer import notification

prev_data = None

def fetchLink(url):
    # Send the GET request
    response = requests.get(url)

    # Make sure the request was successful
    assert response.status_code == 200

    # Get the JSON from the response
    return response.text

def send_notification():
    notification.notify(title='CinemaCity', message='Oppenheimer is ready')

def job():
    global prev_data
    url = "https://www.cinemacity.cz/cz/data-api-service/v1/quickbook/10101/dates/in-group/prague/with-film/5297s2r/until/2024-07-31?attr=&lang=cs_CZ"
    data = fetchLink(url)
    if prev_data == None:
        print("First call successful")
    elif prev_data != data:
        print("NEW DATA AVAILABLE!!!")
        send_notification()
    else:
        print("Nothing new")
    prev_data = data

# Schedule the job every minute
schedule.every(1).minutes.do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

