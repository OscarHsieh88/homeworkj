from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://24h.pchome.com.tw/")

imput_field = "//*[@id=\'root\']/div/header/div[2]/div[1]/div/div/div/div/div[3]/input"
driver.find_element("xpath", imput_field).send_keys("whoscall")
time.sleep(2)
search_btn = "//*[@id=\'root\']/div/header/div[2]/div[1]/div/div/div/div/div[2]/button"
driver.find_element("xpath", search_btn).click()
time.sleep(2)
product = "//*[@id=\'DMAE7S-A900B3RYW\']/dd[2]/h5/a"
driver.find_element("xpath", product).click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

price_xpath = "//*[@id=\"ProdBriefing\"]/div/div/div[2]/div[3]/div/div[1]/div/div"
price = driver.find_element("xpath", price_xpath).text
assert price[:4] == "$999"

time.sleep(5)
spec = "//*[@id=\"ProdDesc\"]"
spec = driver.find_element("xpath", spec)

actions = ActionChains(driver)
actions.move_to_element(spec).perform()

location = spec.location
size = spec.size
png = spec.get_screenshot_as_png() # saves screenshot of entire page
im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image

driver.quit()


