# SMU-IS459-Big-Data_Wong-Kin-Hou
For submission of SMU-IS459 Big Data Architecture Assignments (Wong Kin Hou).

Step 1: Start MongoDB on Port = '27017'
Step 2: cd to this folder's file location (folder name: 'assignement_1_wong_kin_hou')
Step 3: run 'scrapy crawl assignement_1_wong_kin_hou' in command prompt
Step 4: view results in:
						Database: assignment_1_wong_kin_hou
						Table: PC_Game_thread
Alternatively, access assignement_1_wong_kin_hou\Results to view the results in CSV or JSON format. (Results were scrapped on 31st August 7pm)

Sorry if my script takes longer to load as I am trying to scrape responsibly on HWZ.
If you would like to reduce the time taken, please commnent out the following lines in settings.py:
line 28: DOWNLOAD_DELAY = 3
line 71: AUTOTHROTTLE_ENABLED = True