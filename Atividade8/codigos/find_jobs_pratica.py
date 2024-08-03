from bs4 import BeautifulSoup
import requests
import re
import time

def find_jobs(user_skills=None):
    # fazer o request do site com o python 
    html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(html.text, 'lxml') # objeto da BeautifulSoup criado utilizando o parser "lxml"
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') #ocorrencias de todas as tags "li" no html

    for job in jobs: # é realizado o scraping em cada vaga de emprego
        posted = job.find('span', class_='sim-posted')
        if  posted.span.text == 'Posted few days ago': # se é uma vaga recente
            company_name = job.find('h3', class_='joblist-comp-name').text.strip() # separa os titulos e remove espaços em branco desnecessários
            skills = re.sub(r'\s+,',',', (job.find('span', class_='srp-skills').text.strip())) # filtro de regex para melhorar a formataçao final da resposta
            skills_vector = [skill.strip() for skill in skills.split(',')] # list comprehension para separar as skills em um vetor para, posteriormente, verificar se bate com o parametro de entrada
            more_info = job.find('a')['href'] 
            
            if user_skills is not None: # filtra apenas os trabalhos com as skills passadas para a função
                for user_skill in user_skills:
                    if any(user_skill.lower() in skill.lower() for skill in skills_vector):
                        print(f'Company Name: {company_name}\nRequired Skills: {skills}\nMore info: {more_info}\n')
                        break
            else:
                print(f'Company Name: {company_name}\nRequired Skills: {skills}\nMore info: {more_info}\n')

        
if __name__ == '__main__':
    user_skills = (input("Which skills do you have (comma separated):"))
    user_skills = re.sub(r'\s+', '', user_skills).split(',')
    find_jobs(user_skills)
    wait = 10
    print(f"Waiting {wait} minutes...")
    time.sleep(wait*60)


 
