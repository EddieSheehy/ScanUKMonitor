# ScanUKMonitor

In January of 2021 I started this project, during this time there was a big GPU shortage which caused the market for Graphics Cards to inflate drastically due to demand. I made this script to take advantage of this to secure my own GPU as well as GPU's for others.
When the script was ran it would monitor the Scan.co.uk website for a graphics card to be uploaded to their products listed on the website.

The challenging I found with this project is it was a big learning curve as the website had bot protection preventing the likes of this being done which I had to overcome.

The script opened a HTML instance and solved the 2Captcha by calling an API to get the token of a solved 2Captcha. This then allowed this 2Captcha to be sent to the website and access their products list.

Another issue I had to overcome was a website Monitor has to be run 24/7 to be affective. I then researched Heroku and learned I could upload my script to Heroku with a Procfile while called the command to run 'Scan_UK.py' and also learned that I needed a 'requirments.txt'. As
each time the script was ran it needed to install the different modules needed to run the script.

Overall this project took a long time but was a very good learning experience and was a successful task for me to take on.

## How to run
```bash
python3 Scan_UK.py
```

## Example of Discord Webhook
![Here](images/)
