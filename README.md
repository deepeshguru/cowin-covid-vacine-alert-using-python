# cowin-covid-vacine-alert-using-python
These python script give alert sound or send sms to your mobile when Coronavirus (COVID-19) vaccines slot is available for your desire pincode at Cowin - Government of India https://www.cowin.gov.in/home

### cowin_vaccine_alert.py script give sound alert in your systems.
### cowin_vaccine_alert_with_sms.py send text message at your mobile number and give sound alert in your systems.

## prerequisite to run cowin_vaccine_alert.py
git clone https://github.com/deepeshguru/cowin-covid-vacine-alert-using-python.git

install google chrome browser in you system

After google chrome installation download chromedriver from https://chromedriver.chromium.org/downloads according to your OS and google chrome version

Unzip Chromedriver zip file to inside cowin-covid-vacine-alert-using-python folder

python version >= 3.6

install selenium using below command

python -m pip install selenium

## To run cowin_vaccine_alert.py script

python cowin_vaccine_alert.py --pincode pincode

e.g. python cowin_vaccine_alert.py --pincode 560020

## prerequisite to run cowin_vaccine_alert_with_sms.py

git clone https://github.com/deepeshguru/cowin-covid-vacine-alert-using-python.git

Reference for sending text message using python is taken from "https://www.geeksforgeeks.org/send-text-messages-to-any-mobile-number-using-fast2sms-api-in-python/"

In cowin_vaccine_alert_with_sms.py script I am using fast2sms API for sending text message

you need fast2sms account, singup at https://www.fast2sms.com/

After login fast2sms go to Dev API section and copy the  API Authorization and Sender_ID from there and paste in place of star(***)

Note Only 10 sms/day you can send in free

install google chrome browser in you system

After google chrome installation download chromedriver from https://chromedriver.chromium.org/downloads according to your OS and google chrome version

Unzip Chromedriver zip file to inside cowin-covid-vacine-alert-using-python folder


python version >= 3.6

install selenium using below command

python -m pip install selenium


## To run cowin_vaccine_alert_with_sms.py
python cowin_vaccine_alert_with_sms.py --pincode pincode --mobile_number mobile_number

e.g. python cowin_vaccine_alert_with_sms.py --pincode 560020 --mobile_number 8888888888

### Note:- While running script don't turn off your system and screen. if screen turn off your will not get audio sound alert.
