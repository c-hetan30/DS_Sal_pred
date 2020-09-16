import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/A188492/AI/WorkDir/Self_Study/assignments/DS_Sal_pred/DS_Sal_pred/Webdriver/chromedriver.exe"

df = gs.get_jobs('ML Engineer',150, True, path, 3)
df.to_csv('glassdoor_jobs_ML.csv', index = False)

# df = gs.get_jobs('AI Engineer',150, False, path, 3)
# df.to_csv('glassdoor_jobs_AI.csv', index = False)

# df = gs.get_jobs('Data Scientist',150, False, path, 3)
# df.to_csv('glassdoor_jobs_DS.csv', index = False)
