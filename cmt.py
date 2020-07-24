from selenium import webdriver 
import time
import getpass

PATH = "E:\seleniumauto\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

final_comments = []
 #with open('comment.txt') as comment:
comments = ("ft") #comment.readline()
striped_comment = comments.replace(' ',"")
for comment in striped_comment:
    final_comments.append(comment)
        
def auto_comment(striped_comment):
    your_email = ("becec49486@dnawr.com") #input("Enter Email")  #becec49486@dnawr.com
    your_password = ("FuckFuck@123") #getpass.getpass("Enter Password")  #FuckFuck@123
    driver = webdriver.Chrome(PATH)
    driver.get("https://mbasic.facebook.com")
    

    email = driver.find_element_by_css_selector("input[name='email']")
    email.send_keys(str(your_email))
    time.sleep(1)

    password = driver.find_element_by_css_selector("input[name='pass']")
    password.send_keys(str(your_password))
    button = driver.find_element_by_css_selector("input[type='submit']")
    button.click()
    time.sleep(2)

    driver.get("https://mbasic.facebook.com/photo.php?fbid=725405827913079&set=pb.100013310057764.-2207520000..&type=3&theater")

    for i in range(0, 10):
        cb = driver.find_element_by_css_selector("textarea[name='comment_text']")
        cb.send_keys(str(comments))

        button = driver.find_element_by_css_selector("input[type='submit']")
        button.click()

        time.sleep(3)
        print(f'{comments} comment is done !!')

if __name__ == "__main__":
    auto_comment(striped_comment)