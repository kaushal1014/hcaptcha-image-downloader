from selenium import webdriver
import time, requests, shutil
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\\pythonProjects\\spotify on loop player\\chromedriver.exe")
search_url = "https://www.43einhalb.com/en"
images_url = []
driver.maximize_window()

# open browser and begin search
driver.get(search_url)
time.sleep(10)

count=1

#number of pics you will get that is "number_of_runs" x 9
number_of_runs=3

#finding the checkbox
for i in range(number_of_runs):
    all_links=[]
    pics=1
    print(all_links)
    try:
        cookies= driver.find_element_by_xpath('//*[@id="cmpwelcomebtnyes"]/a')
        cookies.click()
    except NoSuchElementException:
        pass

    time.sleep(10)


    #switching the frame 
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='cf-hcaptcha-container']/iframe"))

    i_am_human = driver.find_element_by_id("checkbox")
    i_am_human.click()
    time.sleep(5)

    #switching the main frame
    driver.switch_to.default_content()
    time.sleep(5)

    #switching the frame 
    try:
        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[8]/div[1]/iframe'))
    except NoSuchElementException:
        try:
            driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[7]/div[1]/iframe'))
        except NoSuchElementException:
            try:
                driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[6]/div[1]/iframe'))
            except NoSuchElementException:
                try:
                    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[5]/div[1]/iframe'))
                except NoSuchElementException:
                    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[4]/div[1]/iframe'))


    
    #getting the url of the image
    for i in range(9):

        images=driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div[{pics}]/div[1]/div')
                
        bg_url = images.value_of_css_property('background') 
        list=bg_url.split()

        url=list[4]


        url_link=url.split('"')
        final_link=url_link[1]



        all_links.append(final_link)

        pics=pics+1
        

    print(all_links)
    #Downloading the images
    for link in all_links:
        response = requests.get(link)
        with open(f'image{count}.png', 'wb') as f:
            f.write(response.content)
        
        """Remember to make an image folder and link the path"""
        
        original = f'C:\\pythonProjects\\selenium-photodownloader\\image{count}.png'
        target = f'C:\\pythonProjects\\selenium-photodownloader\\images'
        shutil.move(original,target)
        count+=1
    all_links.clear()
    print("cleared links",all_links)

    driver.refresh()