import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title=[]
company_name=[]
location_name=[]
job_skill=[]

result=requests.get("https://wuzzuf.net/search/jobs/?q=machine+learning&a=hpb")

src=result.content


soup=BeautifulSoup(src,"lxml")

job_titels=soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a",{"class":"css-17s97q8"})
location_names=soup.find_all("span",{"class":"css-5wys0k"})
job_skills=soup.find_all("div",{"class":"css-y4udm8"})

for i in range(len(job_titels)):
    job_title.append(job_titels[i].text)
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    job_skill.append(job_skills[i].text)

file_list=[job_title,company_name,location_name,job_skill]
exported=zip_longest(*file_list)


#location to save the file to
with open("D:\Python\Wep scrabbing\jobstest.csv","w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["Job titels","Company name","location","skiils"])
    wr.writerows(exported)