
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import subprocess

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import sys

# 先開 cmd 輸入下面指令
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9527 --user-data-dir="~/ChromeProfile"


options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9527")
browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()

#直接購票網址可以選座位票數的那個網址
browser.get('https://kktix.com/events/932ce4db-01ajfsj/registrations/new?_gl=1*sgbxnm*_ga*NDQ2MTgwMDQuMTcyNDMzNDM0NQ..*_ga_SYRTJY65JB*MTcyNDk4OTk3Ny40LjEuMTcyNDk5MDcxMS42MC4wLjA.\
            *MjAxMjQ1MDM3NC4xNzI0MDcyOTQ2*_ga_SYRTJY65JB*MTcyNDIzNjM2OC40LjEuMTcyNDIzNzk3Mi4zMC4wLjA.')
#print(browser.title)


# 等待页面加载
#time.sleep(0.5)  # 根据需要调整等待时间





try:
    # 找到class="display-table" 的ID 要改
    ticket_div = browser.find_element(By.ID, 'ticket_772691')
    
    if ticket_div:
        # 找到input元素
        input_element = ticket_div.find_element(By.CSS_SELECTOR, 'input[type="text"]')

        if input_element:
            # 修改value属性
            input_element.clear()  # 清空当前值
            input_element.send_keys('2')  # 輸入張數要更改數字
            #time.sleep(0.5) 
            # 找到同意条款的复选框并点击
            check_box = browser.find_element(By.ID, value="person_agree_terms").click()
        
            #time.sleep(0.5) 
            # 查找並點擊 "下一步" 或 "電腦配位" 按鈕
            button_texts_to_find = ["下一步", "電腦配位"]
            buttons = browser.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text in button_texts_to_find:
                    button.click()  # 點擊按鈕
                    print(f"點擊了按鈕：{button.text}")
                    break
            else:
                print(f"未找到按鈕：{button_texts_to_find}")
        else:
            print("未找到input元素")
    else:
        print("未找到id为ticket_706521的div")
except Exception as e:
    print("出现错误:", e)
finally:
    print("完成")
    # 关闭浏览器
    # time.sleep(5)  # 等待几秒以查看结果