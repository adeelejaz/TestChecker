#!/usr/bin/python

from selenium import webdriver
# for explicit wait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import requests
import json

import random
import os
# for date manipulation
import datetime
from threading import Timer
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BookingID = "";
ReferenceNo = "";
Earliest_Date= "15/07/21";
Latest_Date = "30/08/21";
customer = "07720883959";

def global_variable():
    global testbook

def go_to_website(username, password, desired_date, latest_date, x_location, y_location):
        testbook = "false"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.experimental_options["debuggerAddress"] = "127.0.0.1:1111"
        driver = webdriver.Chrome(executable_path=r"/home/ubuntu/chromedriver", chrome_options=chrome_options)  # for mac
        # driver = webdriver.Chrome(r"C:/Users/Kashif/Python/Scripts/chromedriver")

        format = "%d/%m/%y"
        desired_date_format= datetime.datetime.strptime(desired_date,format)
        desired_date_final= desired_date_format.date()
        desired_date_button = desired_date_final.strftime('%d/%m/%y')
        desired_date_data = desired_date_final.strftime("%Y-%m-%d")
        print("Desired_date_Data: ", desired_date_data)

        last_date_format=datetime.datetime.strptime(latest_date, format)
        last_date=last_date_format.date()
        last_date_button = last_date.strftime('%d/%m/%y')
        last_date_data = last_date.strftime("%Y-%m-%d")
        print("Last date: " , last_date_data)
        #landing_page = driver.get("https://www.gov.uk/change-driving-test")
        #link = driver.find_element_by_link_text('Start now')
        #link.click()
        # fill out form, check if captcha, submit if deal_with_captcha didn't already submit
        #username_box = driver.find_element_by_name('username')
        # username_box.send_keys(DR_LIC_NUM)
        #username_box.send_keys(username)

        #password_box = driver.find_element_by_name('password')
        # password_box.send_keys(APP_REF_NUM)

        #password_box.send_keys(password)

        # if not deal_with_captcha(driver):
        #continue_btn = driver.find_element_by_name('booking-login')
        #continue_btn.click()
        driver.get("https://driverpracticaltest.dvsa.gov.uk/manage?execution=e1s1")
        t.sleep(random.randint(5,10))

        # find and click Change button
        change_button = driver.find_element_by_id('date-time-change')
        change_button.click()
        t.sleep(random.randint(1,2))

        radio_btn = driver.find_element_by_id('test-choice-date')
        radio_btn.click()
        t.sleep(random.randint(1,2))

        choose_date = driver.find_element_by_id('test-choice-calendar')
        choose_date.clear()
        driver.execute_script("document.getElementById('test-choice-calendar').value='" + desired_date_button + "'")
        t.sleep(random.randint(1,2))

        search_button = driver.find_element_by_id("driving-licence-submit")
        search_button.submit()

        present = True
        try:
            table = driver.find_element_by_class_name("BookingCalendar-datesBody")
        except NoSuchElementException:
            present = False

        if not present:
            return

        cell = table.find_elements_by_tag_name("tr")

        for tds in cell:

            td_data = tds.find_elements_by_tag_name('td')
            a_data = tds.find_elements_by_tag_name("a")
            for inside_data in a_data:
                required_date= inside_data.get_attribute('data-date')
                format = "%Y-%m-%d"
                internal_dates = datetime.datetime.strptime(required_date, format)
                internal_date = internal_dates.date()


                div = inside_data.find_element_by_xpath('..')
                td = div.find_element_by_xpath('..')

                if internal_date < last_date and internal_date > desired_date_final:


                    if td.get_attribute('class') == "BookingCalendar-date--bookable ":

                        inside_date = inside_data.get_attribute('data-date')
                        print(inside_date)
                        inside_data.click()
                        bottom_data = driver.find_element_by_id('date-' + inside_date)
                        bottom_data_title = bottom_data.find_element_by_tag_name('p')
                        bottom_data_title_text = bottom_data_title.text
                        driver.implicitly_wait(5) # seconds

                        bottom_data_time = bottom_data.find_element_by_tag_name('strong')
                        bottom_data_time_text = bottom_data_time.text
                        # print(bottom_data_title_text)
                        # print(bottom_data_time_text)
                        #bottom_data_time.click()
                        ActionChains(driver).move_to_element(bottom_data_time).click(bottom_data_time)
                        driver.implicitly_wait(10) # seconds

                        slot_picker_days = driver.find_element_by_class_name('SlotPicker-days')
                        active_slot = driver.find_element_by_css_selector('li.is-active')
                        #active_slot = slot_picker_days.find_element_by_class_name('is-active')

                        xslot_picker_days = driver.find_element_by_class_name('SlotPicker-days')
                        xactive_slot =xslot_picker_days.find_element_by_css_selector('li.is-active')
                        slot_picker_day_title = active_slot.find_element_by_class_name('SlotPicker-dayTitle')
                        print(slot_picker_day_title.text)
                        xslot_picker_day_title = xactive_slot.find_element_by_css_selector('label.unchecked')
                        print(xslot_picker_day_title.text)
                        xslot_picker_day_title.click()
                        slot_picker = xslot_picker_day_title.get_attribute('data-datetime-label')
                        print('end')
                        find_date = xslot_picker_day_title.text + slot_picker_day_title.text
                        print(find_date)

                        submit_form = driver.find_element_by_id('slot-chosen-submit')
                        submit_form.submit()
                        continue_book = driver.find_element_by_id('slot-warning-continue')
                        continue_book.click()
                        print(driver.page_source)
                        Iam = driver.find_element_by_id('i-am-candidate')
                        Iam.click()

                        for x in range(10):
                            code = random.randint(1,999999)
                          #print (random.randint(1,999999))
                        print(code)
                        sender = "07984382541";

                        str1= 'Your date is available' + str(find_date) ;
                        str2 = ' Please reply: ';
                        yes = 'Yes';
                        str3 = f"{yes}{code}"
                        print(str3)
                        #print((str1,customer,str2,code))
                        sms = f"{str1} {BookingID} {customer}{str2}{yes}{code}"
                        print(sms)

                        api_key = "tRPMEalx2Pv1EK3Gd7cq6snz9IgbeQ"
                        end_point = "sendsms"
                        url_args = {
                            "apiKey": api_key,
                            "to": customer,
                            "from": sender,
                            "message" : sms
                            }

                        def send_api_message(end_point, url_args):

                            url = "https://www.firetext.co.uk/api/" + end_point
                            response = requests.post(url, params = url_args)
                            return response.text

                        resp = send_api_message(end_point, url_args)
                        #print (resp)


                        print("waiting... ")

                        t.sleep(870) # wait for sender for 15 minutes

                        ########### Respond to an incoming text message

                        ###### GET MESSAGE #####
                        api_key = "tRPMEalx2Pv1EK3Gd7cq6snz9IgbeQ"
                        end_point = "receivedmessages"
                        url_args = {
                            "apiKey": api_key,
                            "sentTo": sender,
                            "receivedFrom": customer
                        }

                        def get_api_message(end_point, url_args):

                            url = "https://www.firetext.co.uk/api/" + end_point + "/json"
                            response = requests.post(url, params = url_args)
                            return response.text

                        results = get_api_message(end_point, url_args)
                        #print (results)


                        # change the JSON string into a JSON object
                        jsonObject = json.loads(results)

                        # print the keys and values
                        for key in jsonObject:
                            value = jsonObject[key]
                            #print("The key and value are ({}) = ({})".format(key, value))
                            if(key == 'data'):
                                #print(value[2])
                                for key in value:
                                    #print (key)
                                                # Transform json input to python objects
                                    input_dict = value
                                    #print("INPUT", input_dict)
                                    # Filter python objects with list comprehensions
                                    output_dict = [x for x in input_dict if  x['receivedFrom'] == customer ]
                                    #print(output_dict)
                                    output = [obj for obj in output_dict if(   (obj['message'] == str3) and obj['receivedFrom'] == customer) ] #customer
                                    output = json.dumps(output, indent=4, sort_keys=True)
                                    print(output)
                                    #SEND CONFIRMATION
                                    if(output !='[]'):

                                        api_key = "tRPMEalx2Pv1EK3Gd7cq6snz9IgbeQ"
                                        end_point = "sendsms"
                                        url_args = {
                                            "apiKey": api_key,
                                            "to": customer,
                                            "from": sender,
                                            "message" : "Your Booking is confirmed.=>" + str(find_date)

                                            }

                                        def send_api_message(end_point, url_args):

                                            url = "https://www.firetext.co.uk/api/" + end_point
                                            response = requests.post(url, params = url_args)
                                            return response.text

                                        resp = send_api_message(end_point, url_args)

                                        confirm_changes = driver.find_element_by_id('confirm-changes')
                                        confirm_changes.click()
                                        testbook = "true"
                                        driver.quit()

                                    else:
                                        go_to_website(BookingID, ReferenceNo,  Earliest_Date, Latest_Date, 'Sale (Manchester)', 'West Didsbury (Manchester)')
                                        #continue
                    #else: #if its not bookable
                        #continue

while True:

    go_to_website(BookingID, ReferenceNo,  Earliest_Date, Latest_Date, 'Sale (Manchester)', 'West Didsbury (Manchester)')
    t.sleep(random.randint(50,60))
    print(global_variable())
    testbook = global_variable()
    if (testbook == "true"):
        driver.quit()
    else : print("Re-Run")
