from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


#NOTA: Para poder probar el código cambiar el driver al que ustedes utilicen
# solo pongan el que está abajo en un comentario y vuelvan a escribir la variable driver 
# con el driver que utilizan
driver = webdriver.Firefox(executable_path='D:/Selenium/WebDriver/geckodriver.exe')

#Éstos 2 de abajo dejenlos tal y como están
driver.get('https://magento.pwa-commerce.com/')
action = AC(driver=driver)

# PARTE 1 (Rovira)

#Click en opción de cuenta
user = driver.find_element(By.ID, 'my-account')
user.click()
sleep(2)


#Ir a formulario de creación de cuenta
user = driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/div/form/div[4]/button[2]')
user.click()
sleep(2)


#Llenado de formulario
# NOTA: Cada que prueben el código tendrán que cambiar el nombre de usuario y el email
# Solo cambien el número que está al último de cada cadena de texto
user = driver.find_element(By.NAME, 'customer.firstname')
user.send_keys('asdf52')

user = driver.find_element(By.NAME, 'customer.lastname')
user.send_keys('asdf52')

user = driver.find_element(By.NAME, 'customer.email')
user.send_keys('zxcv52@asdf.com')

user = driver.find_element(By.NAME, 'password')
user.send_keys('Aeiou_123')

user = driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/form/div[7]/button[1]')
user.click()
sleep(10)


#Ir a página principal
user = driver.find_element(By.XPATH, '//*[@id="siminia-main-header"]/div[1]/div/div[1]/a/img')
user.click()
sleep(3)


#Seleccionar opción de chamarras para hombre
item = driver.find_element(By.XPATH, '//*[@id="menu-item-category-node-11"]')
action.move_to_element(item).perform()
sleep(3)
#item = driver.find_element(By.XPATH, '//*[@id="menu-item-container-undefined"]/ul/li[2]/div/a')
#action.move_to_element(item).perform()

driver.get('https://magento.pwa-commerce.com/men/tops-men/hoodies-and-sweatshirts-men.html')
sleep(5)


#Adición de 3 chamarras a lista de deseados
#AC.scroll_by_amount(delta_x=0, delta_y=300).perform()
driver.execute_script("window.scrollBy(horizontal_scroll=0, vertical_scroll=300 );")
item = driver.find_element(By.XPATH, '//*[@id="root-product-list"]/div/div[4]/section/div/div/div[1]/div[2]')
action.move_to_element(item).perform()

bttn = driver.find_element(By.CLASS_NAME, 'item-product-grid-wishlistbtn-2kO')
bttn.click()
sleep(2)


item = driver.find_element(By.XPATH, '//*[@id="root-product-list"]/div/div[4]/section/div/div/div[2]/div[2]')
action.move_to_element(item).perform()

bttn = driver.find_element(By.XPATH, '//*[@id="root-product-list"]/div/div[4]/section/div/div/div[2]/div[3]/div/button')
bttn.click()
sleep(2)


item = driver.find_element(By.XPATH, '//*[@id="root-product-list"]/div/div[4]/section/div/div/div[3]/div[2]/div[1]')
item.click()
sleep(2)
driver.execute_script("window.scrollBy(horizontal_scroll=0, vertical_scroll=200 );")
bttn = driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[5]/div/button')
bttn.click()
sleep(2)


# PARTE 2 (Reynaldo)

#1er Item
driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/a/div[2]/span')
driver.click()
sleep(2)

driver.execute_script("window.scrollBy(horizontal_scroll=0, vertical_scroll=200 );")

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[1]/div/button[1]')
driver.click()

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[2]/div/button[1]')
driver.click()
sleep(1)

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[4]/div[2]/section/button')
driver.click()

driver.find_element('//*[@id="wish-list"]/a')
driver.click()


#2do Item
driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/a/div[2]/span')
driver.click()
sleep(2)

driver.execute_script("window.scrollBy(horizontal_scroll=0, vertical_scroll=200 );")

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[1]/div/button[1]')
driver.click()

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[2]/div/button[1]')
driver.click()
sleep(1)

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[4]/div[2]/section/button')
driver.click()

driver.find_element('//*[@id="wish-list"]/a')
driver.click()


#3er Item
driver.find_element(By.XPATH, '//*[@id="siminia-main-page"]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/a/div[2]/span')
driver.click()
sleep(2)

driver.execute_script("window.scrollBy(horizontal_scroll=0, vertical_scroll=200 );")

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[1]/div/button[1]')
driver.click()

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[3]/section/div[2]/div[2]/div/button[1]')
driver.click()
sleep(1)

driver.find_element('//*[@id="siminia-main-page"]/div/div/div/div/div[3]/div[1]/form/div[4]/div[2]/section/button')
driver.click()

driver.find_element('//*[@id="wish-list"]/a')
driver.click()



# PARTE 3 (Migue)
driver.find_element(By.CSS_SELECTOR, ".cartTrigger-root-3ZH svg").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, ".cartTrigger-root-3ZH > .header-item-text-1Mj").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR, ".miniCart-goToCheckoutButton-36O > .button-content-WHg").click()
sleep(2)

driver.find_element(By.ID, "customer_street0").click()
sleep(2)

driver.find_element(By.ID, "customer_street0").send_keys("CALLE")
sleep(2)

driver.find_element(By.ID, "customer_city").click()
sleep(2)

driver.find_element(By.ID, "customer_city").send_keys("ATLANTA")
sleep(2)

driver.find_element(By.ID, "region-root-1Sr").click()
sleep(2)

dropdown = driver.find_element(By.ID, "region-root-1Sr")
sleep(2)

dropdown.find_element(By.XPATH, "//option[. = 'Colorado']").click()
sleep(2)

driver.find_element(By.ID, "postcode-root-26p").click()
sleep(2)

driver.find_element(By.ID, "postcode-root-26p").send_keys("56")
sleep(2)

driver.find_element(By.ID, "customer_telephone").click()
sleep(2)

driver.find_element(By.ID, "customer_telephone").send_keys("23435633")
sleep(2)

driver.find_element(By.CSS_SELECTOR, ".button-root_normalPriority-1nP").click()
sleep(2)

driver.find_element(By.ID, "paymentMethod--checkmo").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR, ".checkoutPage-review_order_button-151").click()
sleep(2)

driver.find_element(By.CSS_SELECTOR, ".checkoutPage-place_order_button-3Pk").click()
sleep(2)

driver.find_element(By.XPATH, "//img[@alt=\'SimiCart PWA\']").click()
sleep(2)

