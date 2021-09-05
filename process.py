from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from functools import lru_cache
from prettytable import PrettyTable


table = PrettyTable()
@lru_cache(maxsize=25)
def Searched(text):
    
    JobSearched = text
    print(f"Job searched> {JobSearched}")
    url1 = 'https://www.akhtaboot.com/en/jordan'

    #Selenium Open chrome and go the URL
    #Click on the Search 
    #and input text
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    browser = webdriver.Chrome('chromedriver',options=opt)
    browser.get(url1)
    browser.find_element_by_xpath('//*[@id="input-focus"]').send_keys(JobSearched)
    browser.find_element_by_xpath('//*[@id="headerimg"]/div/form/div/div[2]/button').click()


    url_page = browser.current_url


    html_text = requests.get(url_page).text
    print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')

    list_companies= []
    list_locations = []
    list_career = []
    list_date = []
    list_jobs =[]
    list_links =[]
    list_companies.clear()
    list_locations .clear()
    list_career.clear()
    list_date.clear()
    list_jobs.clear()
    
    #BeautifulSoup Scraps website
    #for requested tags
    jobs = soup.find_all('div',class_='col-xs-12 col-sm-12 col-md-10 job-content')
    for job in jobs:
        company_name = job.find('p', class_='no-margin').text.split("-")
        location = job.div.div.div.p.strong.span.text
        job_title = job.find('a', class_='job-link').text
        career_level = job.find('dd').text
        date_posted = job.find('small',class_='col-md-3 pull-right').text.replace(' ','').split("Posted")
        link_for_post = job.div.div.div.a['href']

        comp_name =company_name[0][2:]
        loc_name = location[1:]
        job_t = job_title[1:]
        career = career_level[14:]
        date_up = date_posted
        link = link_for_post

        #Store the data
        #so it can be returned
        list_companies.append(company_name[0][2:])
        list_locations.append(location[1:])
        list_jobs.append(job_title[1:])
        list_career.append(career_level[14:])
        list_date.append(date_posted)
        list_links.append(link_for_post)
        

        
        '''Testing
        print(f'Company Name:{company_name[0][2:]}')
        print(f'Location:{location[1:]}')
        print(f'Job:{job_title[1:]}')
        print(f'More Information: '+f'https://www.akhtaboot.com{link_for_post}'+'\n')
        print(f'Career Level:{career_level[14:]}'+'\n')
        print(f'Data Posted {date_posted}')
        '''

        '''Testing
        print(list_companies)
        print(list_locations)
        print(list_jobs)
        print(list_career)
        print(list_date)
        '''

        #Get length for double checking
        #if scraping was a full success 
        length_comp = len(list_companies)
        length_location = len(list_locations)
        length_jobs = len(list_jobs)
        length_career = len(list_career)
        length_date = len(list_date)
        length_links = len(list_links)

    #Create a table
    #For better view 
    table.add_column("Data",['Companies','locations','Jobs','Careers','Date','Links'])
    table.add_column("Count",[length_comp,length_location,length_jobs,length_career,length_date,length_links])
    print(table)

    #We Clear so everytime we search again
    #We will get a new table
    table.clear()

    #Return to view
    return (list_companies,list_locations,list_jobs,list_career,list_date,list_links,length_comp)

