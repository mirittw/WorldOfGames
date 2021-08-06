from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

def test_scores_service(url):
    # "http://127.0.0.1:5001/scores"
    my_driver.get(url)
    actual = my_driver.find_element_by_id("score").text
    my_driver.close()
    if int(actual) is None or not 0 <= int(actual) <= 1000:
        return False
    else:
        return True

def main_function():
