
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

# 等待页面加载
#time.sleep(0.5)  # 根据需要调整等待时间

# 設定參數
url = "https://kktix.com/events/1089571a/registrations/new?_gl=1*3876qh*_ga*NDQ2MTgwMDQuMTcyNDMzNDM0NQ..*_ga_SYRTJY65JB*MTcyNDk5NTA4NS41LjEuMTcyNDk5NjEzNS41Mi4wLjA."
qty = 2  # 設定的票數量

def check_tickets():
    browser.get(url)
    # time.sleep(2)  # 等待頁面加載

    # 查找所有 input[type="text"] 元素
    inputs = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

    for input_element in inputs:
        try:
            input_element.clear()  # 清空輸入框
            input_element.send_keys(str(qty))  # 嘗試輸入設定的票數量
            # input_element.send_keys(Keys.TAB)  # 觸發輸入框的變化

            # 檢查輸入框中的值是否等於設定的票數量
            if input_element.get_attribute("value") == str(qty):
                # 點擊同意條款
                check_box = browser.find_element(By.ID, "person_agree_terms").click()
                time.sleep(0.5)

                # 查找並點擊 "下一步" 或 "電腦配位" 按鈕
                button_texts_to_find = ["下一步", "電腦配位"]
                buttons = browser.find_elements(By.TAG_NAME, "button")
                for button in buttons:
                    if button.text in button_texts_to_find:
                        button.click()  # 點擊按鈕
                        print(f"點擊了按鈕：{button.text}")
                        return True
                else:
                    print(f"未找到按鈕：{button_texts_to_find}")
                break  # 找到符合條件的 input 後跳出循環
            else:
                input_element.clear()  # 如果不能輸入設定的票數量，清空輸入框
        except Exception as e:
            print(f"錯誤：{e}")

    return False


# 主循環
while True:
    if check_tickets():
        break
    time.sleep(5)  # 每隔 5 秒刷新一次頁面