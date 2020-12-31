import time
import yaml
from selenium import webdriver

'''
- domain: work.weixin.qq.com
  expiry: 1608569020
  httpOnly: true
  name: ww_rtkey
  path: /'''

class TestCookie:
    def test_get_cookie(self):  # 复用浏览器拿到最新的token，token过期的话
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)  #留时间微信扫码，否则拿到的cookie是错误的
        cookie = driver.get_cookies()
        print(cookie)
        with open("cookies.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)