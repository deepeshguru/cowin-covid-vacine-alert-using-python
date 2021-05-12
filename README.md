# cowin-covid-vacine-alert-using-python
These python script give alert sound or send sms to your mobile when Coronavirus (COVID-19) vaccines slot is available for your desire pincode at Cowin - Government of India https://www.cowin.gov.in/home

### cowin_vaccine_alert.py script give sound alert in your systems.
### cowin_vaccine_alert_with_sms.py send text message at your mobile number and give sound alert in your systems.

## prerequisite to run cowin_vaccine_alert.py, open script change picode with your pincode
install google chrome browser in you system

After google chrome installation download chromedriver from https://chromedriver.chromium.org/downloads according to your OS and google chrome version

python version >= 3.6

install selenium using below command

python -m pip install selenium

## To run owin_vaccine_alert.py script

python owin_vaccine_alert.py

## prerequisite to run cowin_vaccine_alert_with_sms.py, open script change picode with your pincode and mobile number with your number

Reference for sending text message using python is taken from "https://www.geeksforgeeks.org/send-text-messages-to-any-mobile-number-using-fast2sms-api-in-python/"

In cowin_vaccine_alert_with_sms.py script I am using fast2sms API for sending text message

you need fast2sms account, singup at https://www.fast2sms.com/

After login fast2sms go to Dev API section and copy the  API Authorization and Sender_ID from there and paste in place of star(***)

Note Only 10 sms/day you can send in free

install google chrome browser in you system

After google chrome installation download chromedriver from https://chromedriver.chromium.org/downloads according to your OS and google chrome version

python version >= 3.6

install selenium using below command

python -m pip install selenium


## To run owin_vaccine_alert.py script
python cowin_vaccine_alert_with_sms.py

### Note:- While running script don't turn off your system and screen. if screen turn off your will not get audio sound alert.
