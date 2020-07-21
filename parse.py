from selenium import webdriver
from urllib.parse import urlencode
import webbrowser
import sqlite3

options = webdriver.ChromeOptions()

options.add_argument('headless')

browser = webdriver.Chrome(options=options)

conn = sqlite3.connect('gmap.sqlite')

cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS gdata;

    CREATE TABLE gdata(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name TEXT,
    Rating TEXT,
    Detail TEXT,
    Location TEXT,
    Closing_time TEXT,
    Phone TEXT
    )
    ''')
#url = "https://www.google.com/maps/place/Papa+John's+Pizza/@12.3216081,75.5001326,8z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687"
#url = "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"
#url = "https://www.google.com/maps/place/Gobind+Medical+Stores/@28.6581233,77.0934676,11z/data=!4m8!1m2!2m1!1smedicine+shops+near+delhi!3m4!1s0x390cfd1b385c6c3d:0x13f0c0df9496b950!8m2!3d28.6581233!4d77.2335433"
gmapsurl = "https://www.google.com/maps/search/?api=1&"
#url = "https://www.google.com/maps/place/Mall+Of+Mysore/@12.2975437,76.6622001,17z/data=!3m1!4b1!4m5!3m4!1s0x3baf7018a81e0e5d:0x5b736aafd8221b5d!8m2!3d12.2975437!4d76.6643888"
#place = input("Enter the place : ")


search = input("What are u looking for? ")

mydict = {"query": search}

#gmapsurl = f"https://www.google.com/maps/search/{search}+near+{place}/"

url = gmapsurl + urlencode(mydict)
print(url)
global no
no = 1
browser.get(url)

while 1:
    try:
        titles = browser.find_elements_by_class_name("section-result-title")
        ratings = browser.find_elements_by_class_name("section-result-rating")
        details = browser.find_elements_by_class_name("section-result-details")
        locations = browser.find_elements_by_class_name("section-result-location")
        description = browser.find_elements_by_class_name("section-result-descriptions")
        openings = browser.find_elements_by_class_name("section-result-opening-hours")
        phone_nos = browser.find_elements_by_class_name("section-result-phone-number")

        
        for title,rating,detail,location,opening,phone in zip(titles,ratings,details,locations,openings,phone_nos):
            print('\nNo :',no)
            print('Tiltle :',title.text)
            print('Rating :',rating.text)
            print('Detail :',detail.text)
            print('Location :',location.text)
            print('Opens at :',opening.text)
            print('Phone no: ',phone.text)
            no += 1
            cur.execute('''INSERT INTO gdata (Name, Rating, Detail, Location, Closing_time, Phone)
                VALUES (?,?,?,?,?,?)''',(title.text,rating.text,detail.text,location.text,opening.text,phone.text,))
        
        browser.find_element_by_id("n7lv7yjyC35__section-pagination-button-next").click()
        conn.commit()
    
    except:
        print("that's all the results!")
        break



'''
while 1:
    try:
        name_element = browser.find_elements_by_class_name("section-result-text-content")
        for i in name_element:
            print(i.text)
            print()
    
        browser.find_element_by_id("n7lv7yjyC35__section-pagination-button-next").click()
    except:
        print("that's all the results!")
        break

    res = input("get more results??")
    if res == 'yes':
        browser.find_element_by_id("n7lv7yjyC35__section-pagination-button-next").click()
    elif res == 'no':
        break









name_element = browser.find_elements_by_class_name("section-result-title")
for i in name_element:   ugiz4pqJLAG__primary-text gm2-body-2
                         ugiz4pqJLAG__primary-text gm2-body-2
    print(i.text)

address_element = browser.find_elements_by_class_name("section-result-details-container")
for i in address_element:
    print(i.text)






name_element = browser.find_elements_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1/span[1]')[0]
name = name_element.text
print(name)
# review titles / username / Person who reviews

address_element = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[12]/button/div/div[2]/div[1]')
address = address_element.text //*[@id="pane"]/div/div[1]/div/div/div[8]/button/div/div[2]/div[1]
print(address)

status_element = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[13]/div[1]/div/div[1]/span[1]/span[1]')
status = status_element.text
print(status)

phone_element = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[15]/button/div/div[2]/div[1]')
phone = phone_element.text
print(phone)

stars_element = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[31]/div/div[2]/button')
stars = stars_element.text
print(stars)

review_titles = browser.find_elements_by_class_name("section-review-title")

print([a.text for a in review_titles])

# review text / what did they think

review_text = browser.find_elements_by_class_name("section-review-review-content")

print([a.text for a in review_text])

# get the number of stars

stars = browser.find_elements_by_class_name("section-review-stars")

first_review_stars = stars[0]

active_stars = first_review_stars.find_elements_by_class_name("section-review-star-active")

print(f"the stars the first review got was {len(active_stars)}")'''
