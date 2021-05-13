##This script give play system sound if vaccine slot is Available at your pincode

## prerequisite to run below code
# install google chrome browser in you system
# After google chrome installation download chromedriver from https://chromedriver.chromium.org/downloads according to your OS and google chrome version
# python version >= 3.6
# install selenium using below command
# python -m pip install selenium


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse
import platform

parser = argparse.ArgumentParser(description='Covid Vaccine Alert Program.')

parser.add_argument("-p", "--pincode", help="Enter your pincode.", default="470117")
args = parser.parse_args()
pincode = args.pincode

system = platform.system()
#set chromodriver path below
if system = 'Windows':
    chromedriver_path = r".\chromedriver_win32\chromedriver.exe"
elif system = 'Linux':
    chromedriver_path = r"./chromedriver_linux64/chromedriver"
elif system = "Darwin":
    chromedriver_path = r"./chromedriver_mac64/chromedriver"
else:
    print("your OS doesn't support chrome drive")
    exit()

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.implicitly_wait(0.5)

driver.get("https://www.cowin.gov.in/home")

while(1):
    try:
        driver.delete_all_cookies()
        driver.refresh()
        # increase time.sleep() value if your internet speed is slow
        time.sleep(5)
        m = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div/input")
        m.send_keys(pincode)
        time.sleep(5)
        m.send_keys(Keys.ENTER)
        time.sleep(5)
        m = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[7]/div/div")
        data = m.text
        for i in range(100):
            if str(i)+"\nCOVAXIN\nAge 18+" in data or str(i)+"\nCOVISHIELD\nAge 18+" in data:
                print("Status Available", i)
                # give alert for 10 sexconds
                for j in range(20):
                    time.sleep(0.5)
                    print('\a')
                break
        if str(i)+"\nCOVAXIN\nAge 18+" in data or str(i)+"\nCOVISHIELD\nAge 18+" in data:
            print('\a')
            print("Status: Available", i)
            break
        if "Booked\nCOVAXIN\nAge 18+" in m.text or "Booked\nCOVISHIELD\nAge 18+" in m.text:
            print("Status: All Solt Booked at your pincode")
        else:
            print("Status: Slot Unavailble at your pincode")
    except Exception as e:
        print(e)
        time.sleep(60)
