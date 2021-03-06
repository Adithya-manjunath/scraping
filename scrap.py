  
from selenium import webdriver
from urllib.parse import urlencode
import webbrowser
import sqlite3
import json
import os



pincode_file = open('IN.csv','r')
l = pincode_file.read().split('\n')
l.pop(0)
l.pop()
q = input("Different varieties of stores can be scraped,Enter the type of the store you want to scrape : ")

#q = input("These catogories are can be scraped,choose any option to continue\n 1)Groceries Shop\n 2)Xerox shop \n 3)Clinic \n 4)Medicine shop \n 5)Super market \n 6)Electronic shop\n")
#dic={"1":"Groceries Shop","2":"Xerox shop","3":"Clinic","4":"Medicine shop","5":"Super market","6":"Electronic shop"}

for i,line in enumerate(l):
	pincode = line[line.find('/')+1:line.find(',')]
	print(i,pincode)
	print("running.....")
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	browser = webdriver.Chrome(options=options)


	_dir = "."       


	_dir = os.path.join(_dir,'%s' % q)

	if not os.path.exists(_dir):
		os.makedirs(_dir)


	place = pincode
	search = q
	
	f_path = f'{q}/{place}.json'
	file = open(f_path,'w')

	#file.write('name,rating,detail,location,opening_time,phone\n')

	mydict = {"query": search, "place":place}

	gmapsurl = f"https://www.google.com/maps/search/{search}+near+{place}/"
	print(gmapsurl)

	url = gmapsurl + urlencode(mydict)
	browser.get(url)

	no = 1
	data = []
	a = {}
	while True:
		titles = browser.find_elements_by_class_name("section-result-title")
		ratings = browser.find_elements_by_class_name("section-result-rating")
		details = browser.find_elements_by_class_name("section-result-details")
		locations = browser.find_elements_by_class_name("section-result-location")
		openings = browser.find_elements_by_class_name("section-result-opening-hours")
		phone_nos = browser.find_elements_by_class_name("section-result-phone-number")

		for title,rating,detail,location,opening,phone in zip(titles,ratings,details,locations,openings,phone_nos):
			try:
				if title.text == '':
					tilte_checked = "None"
				else:
					title_checked = title.text
			except:
				tilte_checked = "None"

			try:
				if rating.text == '':
					rating_checked = "None"
				else:
					rating_checked = rating.text
			except:
				rating_checked = "None"

			try:
				if detail.text == '':
					detail_checked = "None"
				else:
					detail_checked = detail.text
			except:
				detail_checked = "None"

			try:
				if location.text == '':
					location_checked = "None"
				else:
					location_checked = location.text
			except:
				location_checked = "None"

			try:
				if opening.text == '':
					opening_checked = "None"
				else:
					opening_checked = opening.text
			except:
				opening_checked = "None"

			try:
				if phone.text == '':
					phone_checked = "None"
				else:
					phone_checked = phone.text
			except:
				phone_checked = "None"
	    	# print('\nNo :',no)
	    	# print('Tiltle :',title_checked)
	    	# print('Rating :',rating_checked)
	    	# print('Detail :',detail_checked)
	    	# print('Location :',location_checked)
	    	# print('Opens at :',opening_checked)
	    	# print('Phone no: ',phone_checked)
			no += 1

			a = {
	                "name" : title_checked,
	                "rating" : rating_checked,
	                "detail" : detail_checked,
	                "location" : location_checked,
	                "open_at" : opening_checked,
	                "phone" : phone_checked
	            }

			data.append(a)
	    	# new_record = f"{title_checked},{rating_checked},{detail_checked},{location_checked},{opening_checked},{phone_checked}\n"
	    	# file.write(new_record)


		try:
			browser.find_element_by_id("n7lv7yjyC35__section-pagination-button-next").click()
			print("went on next page")
		except:
	        #file.close()
			print("program read all data")
			break


	last = {
		"pincode" : place,
		"data" : data
	}
	json.dump(last, file)
	file.close()
	print(f"file {place}.json successfully created")
	browser.close()
	


print("program finished with downloading 5000 files")