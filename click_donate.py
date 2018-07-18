from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint

########################################################
###                   ローカル変数                     ###
########################################################

#Chromeを操作
driver = webdriver.Chrome(executable_path="/Users/kztmr/Downloads/chromedriver")
#Macは⌘キー
ctrl = Keys.COMMAND
#別タブで開く設定
actions = ActionChains(driver)
actions.key_down(ctrl)
#ウィンドウサイズ設定
driver.set_window_size(800, 600)

########################################################
###                  　　　関数　　　                   ###
########################################################

#取得したボタンを別タブで全て開き、全て閉じる
def click_newtab(btn):
    for i in btn:
      i.click()
    for window, i in zip(driver.window_handles, range(len(driver.window_handles))):
      driver.switch_to.window(window)
      if i == 0:
        continue
      driver.close()
    else:
      driver.switch_to.window(driver.window_handles[0])
########################################################
###                 クリック募金サイト                  ###
########################################################

#スポクリ
driver.implicitly_wait(10)
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
btn = driver.find_elements(By.XPATH, "//*[@class='bokin clearfix']/ul/li")
click_newtab(btn)

#東日本大震災クリック募金
driver.get("https://www.dff.jp/click/view/83/loading.html?t=1531050396146")
time.sleep(1)
btn = driver.find_element(By.XPATH, "//img[@alt='東北の学生を応援する']")
time.sleep(2)
btn.click()

#アンダ・クリック募金
driver.get("https://www.andaresort.jp/eco/flash/")
btn = driver.find_element(By.XPATH, "//embed[@src='click120530.swf']")
btn.click()

#やまがた被害者支援センター
driver.get("http://yvsc.jp/")
driver.execute_script("window.scrollTo(0, 3500);")
btn = driver.find_elements(By.XPATH, "//img[@class='bnr-img']")
click_newtab(btn)

#いわて被害者支援センター
driver.get("https://www.iwate-vsc.jp/")
btn = driver.find_elements(By.XPATH, "//div[@class='campaignbnr']/ul/li/a")
click_newtab(btn)

#大阪市市民活動総合ポータルサイト
driver.get("http://kyodo-portal.city.osaka.jp/click/")
btn = driver.find_elements(By.XPATH, "//ul[@class='bnr']/li/a/img")
click_newtab(btn)

#ひょうご被害者支援センター
driver.get("http://www.supporthyogo.org/")
btn = driver.find_elements(By.XPATH, "//div[@id='oneclick']/a/img")
click_newtab(btn)

#被害者支援センターやまなし
driver.implicitly_wait(10)
driver.get("http://www.sien-yamanashi.com/")
btn = driver.find_elements(By.XPATH, "//p[@class='bar img_in md']/a/img")
driver.execute_script("window.scrollTo(0, 3500);")
click_newtab(btn)

#ツイタもん
driver.get("https://tsuitamon.jp/")
btn = driver.find_element(By.XPATH, "//div[@id='charity']/p[@class='btn']/a/img")
btn.click()
time.sleep(2)

#ウェブベルマーク
driver.get("https://www.webbellmark.jp/")
btn = driver.find_element(By.XPATH, "//li[@class='top-btn-1click']/a/img")
btn.click()
time.sleep(3)

#スマートクリック募金
driver.implicitly_wait(10)
driver.get("http://www.ww-system.com/wws/service/smartclickbokin/#")
time.sleep(5)
btn = driver.find_element(By.XPATH, "//li[@id='btns0']/a/img")
btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#飢餓救済ウェブ
driver.get("http://www.jp.seicho-no-ie.org/kiga/fund_a.html")
btn = driver.find_elements(By.XPATH, "//ul[@class='cols-5']/li/div/a/img")
click_newtab(btn)

#CtoCグループ
driver.get("https://www.ctocgroup.co.jp/click/index.php")
btn = driver.find_element(By.XPATH, "//div[@class='soushin']/input[@class='idxclick']")
btn.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#最終画面
driver.get("http://goldstacks.xyz/click_donate/")
time.sleep(10)

driver.quit()
