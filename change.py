from selenium import webdriver
import time

def access_website():
    driver = webdriver.Chrome()
    driver.get('http://localhost:7897')
    
    # ここに必要な操作を追加

    return driver

# http://localhost:7897 にアクセス
driver = access_website()

# スクリプトが終了しないように待機（例: 10秒）
time.sleep(10)