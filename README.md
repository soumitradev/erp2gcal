# erp2gcal

## Features

* Enroll/unenroll batch from cms.
* Create google calendar events with ease.

## Usage

1. [Download](https://github.com/pnicto/erp2gcal/archive/refs/heads/master.zip) the repo.
2. [Visit](https://developers.google.com/calendar/api/quickstart/python) and follow the prerequisites or read more below.
   <details>
   <summary>Click to read more</summary>

   1. <a href="https://console.cloud.google.com/">Visit</a> in the side bar choose APIs & Services -> Library Search for google calendar and enable it.
   2. Now go to APIs & Services -> Credentials, Create a project and then Create Credentials -> Oauth client ID -> Desktop app as application type after creating download it as json.
   </details>
3. Rename the downloaded file as `credentials.json` and place it along with the downloaded files from step 1.
4. Run
   ```
   pip install -r requirements.txt
   ```
5. Run
   ```py
    python main.py
    ```
6. Choose the options shown on terminal and login when propmpted.

## TODO

* Fix known issues.

## Known Issues

1. The day you run the script the calendar will be filled with all classes.
2. Workshop Practical is counted as a regular lab class and takes 2 hours instead of 3.

## Troubleshooting

1. Problem: `Authorization Error Error 403: Access_denied`<br/>
   Solution: [Visit](https://console.cloud.google.com/), goto APIs & Services -> OAuth consent screen, select the app you created in step 3 of `Usage` and add your email under `Test Users`.
2. Problem: `Unauthenticated`<br/>Solution: Delete the token.json and rerun the script with `Create calendar events`.
