from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint

########################################################
###                  ローカル変数                    ###
########################################################

#Chromeを操作
driver = webdriver.Chrome(executable_path="/Users/kztmr/Downloads/chromedriver")
#Macは⌘キー
ctrl = Keys.COMMAND

#driver.set_window_size(500, 600)
########################################################
###               クリック募金サイト                 ###
########################################################

#スポクリ
driver.get("https://spocli.com/sponsor_sports/jms/goudou/jms_goudou.html")
btn = driver.find_element(By.XPATH, "//*[@class='click-btn link-btn']")
btn.click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#兵庫県肢体不自由児者協会
driver.get("http://hyoshikyo.com/c-bokin.aspx")
btn = []
for i in range(6):
  btn.append(driver.find_elements(By.XPATH, "//*[@id='grid_HyperLink1_%d']" % i))

actions = ActionChains(driver)
actions.key_down(ctrl)
for i in btn:
  for j in i:
    actions.click(j)
else:
  actions.perform()

for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
  driver.switch_to.window(window)
  if i == 0:
    continue
  driver.close()
else:
  driver.switch_to.window(driver.window_handles[0])

#JWord
driver.get("http://www.jword.jp/campaign/charity/")
del(btn)
btn = driver.find_elements(By.XPATH, "//*[@class='bokin clearfix']/ul/li")
for i in btn:
  i.click()

for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
  driver.switch_to.window(window)
  if i == 0:
    continue
  driver.close()
else:
  driver.switch_to.window(driver.window_handles[0])

#東日本大震災クリック募金
driver.get("https://www.dff.jp/click/view/83/loading.html?t=1531050396146")
time.sleep(1)
del(btn)
btn = driver.find_element(By.XPATH, "//img[@alt='東北の学生を応援する']")
time.sleep(2)
btn.click()

#アンダ・クリック募金
driver.get("https://www.andaresort.jp/eco/flash/")
btn = driver.find_element(By.XPATH, "//embed[@src='click120530.swf']")
btn.click()

#やまがた被害者支援センター
driver.get("http://yvsc.jp/")
del(btn)
driver.execute_script("window.scrollTo(0, 3500);")
time.sleep(1)
#btn = driver.find_elements(By.XPATH, "//aside[@class='banner_container']/ul/li/a")
btn = driver.find_elements(By.XPATH, "//img[@class='bnr-img']")
for i in btn:
  i.click()
for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
  driver.switch_to.window(window)
  if i == 0:
    continue
  driver.close()
else:
  driver.switch_to.window(driver.window_handles[0])

#いわて被害者支援センター
driver.get("https://www.iwate-vsc.jp/")
del(btn)
time.sleep(1)
btn = driver.find_elements(By.XPATH, "//div[@class='campaignbnr']/ul/li/a")
for i in btn:
  i.click()
for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
  driver.switch_to.window(window)
  if i == 0:
    continue
  driver.close()
else:
  driver.switch_to.window(driver.window_handles[0])

#大阪市市民活動総合ポータルサイト
driver.get("http://kyodo-portal.city.osaka.jp/click/")
del(btn)
time.sleep(1)
btn = driver.find_elements(By.XPATH, "//ul[@class='bnr']/li/a/img")
pprint(btn)
for i in btn:
  i.click()
for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
  driver.switch_to.window(window)
  if i == 0:
    continue
  driver.close()
else:
  driver.switch_to.window(driver.window_handles[0])

#最終画面
driver.get("http://goldstacks.xyz/click_donate/")
#driver.get("./index.html")
time.sleep(10)

driver.quit()
