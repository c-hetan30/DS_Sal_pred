import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/A188492/AI/WorkDir/Self_Study/assignments/DS_Sal_pred/DS_Sal_pred/Webdriver/chromedriver.exe"

df = gs.get_jobs('data scientist',10, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)