import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#test
driver = webdriver.Chrome("E:\chromedriver.exe")

driver.get("http://portal.ecnu.edu.cn")
time.sleep(2)

thisis = driver.find_element_by_id('un')
pwd = driver.find_element_by_id('pd')
code = driver.find_element_by_name('code')
code_image = driver.find_element_by_id('codeImage')
login_button = driver.find_element_by_class_name('login_box_landing_btn')

my_id = "10165101161"
my_psd = "Zyw984076019"
my_code = input('code:')

thisis.send_keys(my_id)
pwd.send_keys(my_psd)
code.send_keys(my_code)

time.sleep(1)
login_button.click()
time.sleep(1)

undergraduate_teaching = driver.find_element_by_link_text('本科教学')
undergraduate_teaching.click()
time.sleep(1)

windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(1)

b = driver.find_element_by_css_selector('li.li_1 a.subMenu')
b.click()
time.sleep(1)

xuanke = driver.find_element_by_xpath(".//*[@mytitle='选    课']")
xuanke.click()
time.sleep(1)

benzhuanye = driver.find_element_by_xpath('//*[@id="electIndexNotice0"]/a')
benzhuanye.click()
time.sleep(1)

windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(1)

aa = {"0", "0"}
i = 1
while 1:
    driver.refresh()
    #time.sleep(1)
    try:
        mycourse_page = driver.find_element_by_xpath('//*[@id="electableLessonList_bar1_page"]/a[6]')
        mycourse_page.click()
    except:
        print("页面刷新获取失败")
        continue
    try:
        mycourse = driver.find_element_by_xpath('//*[@id="lesson500046"]/td[7]').text
        aa = mycourse.split('/')
    except:
        print("人数获取失败")
        continue

    print(i)
    i = i+1
    print(aa[0])
    print(aa[1])
    if aa[0] != aa[1]:
        try:
            chooseCourse = driver.find_element_by_xpath('//*[@id="lesson500046"]/td[10]/a').text
            print(chooseCourse)
            #alert = driver.switch_to_alert()
            #alert.accept()
            print("success!")
        except:
            print("选课失败")
            continue


    #mycourse.click()
    #time.sleep(2)




'''
lession_management = driver.find_element_by_link_text('课程管理')
lession_management = lession_management.parent
lession_management.click()
'''
