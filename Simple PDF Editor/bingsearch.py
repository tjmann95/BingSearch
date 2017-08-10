from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\1117254\\Documents\\chromedriver.exe")
browser.set_window_size(1920, 1080)


def login(username, password):
    browser.get("http://www.bing.com")
    time.sleep(2)
    sign_in = browser.find_element_by_id("id_a")
    sign_in.click()
    time.sleep(2)
    connect = browser.find_element_by_id("b_idProviders")
    connect.click()
    time.sleep(2)
    actions = ActionChains(browser)
    actions.send_keys(username)
    actions.perform()
    enter = browser.find_element_by_id("idSIButton9")
    enter.click()
    time.sleep(2)
    actions = ActionChains(browser)
    actions.send_keys(password)
    actions.perform()
    enter = browser.find_element_by_id("idSIButton9")
    enter.click()


def do_search(word):
    search_box = browser.find_element_by_id("sb_form_q")
    search_box.send_keys(word)
    search_box.submit()
    search_box = browser.find_element_by_id("sb_form_q")
    search_box.clear()


def logout():
    logout_button = browser.find_element_by_id("id_l")
    logout_button.click()
    time.sleep(2)
    logout = browser.find_element_by_id("b_idProviders")
    logout.click()


def get_points():
    points_elem = browser.find_element_by_id("id_rc")
    return points_elem.text


def main():
    wordfile = open("words.txt", "r")
    words = wordfile.read().split("\n")
    loginfile = open("login.txt", "r")
    login_raw = loginfile.read().split("\n")
    usernames = login_raw[0:5]
    passwords = login_raw[5:]
    start_time = time.time()
    for each_login in range(len(usernames)):
        if usernames[each_login]:
            print(usernames[each_login] + "...")
            login(usernames[each_login], passwords[each_login])
            for i in range(40):
                if i == 1:
                    print(usernames[each_login] + " has " + get_points() + " points.")
                do_search(random.choice(words) + " " + random.choice(words))
                time.sleep(random.uniform(.5, 5.0))
            print(usernames[each_login] + " has " + get_points() + " points.")
            logout()
            print(usernames[each_login] + " is done.\n")
    duration = time.time() - start_time
    print("Search program took " + str(int(duration / 60)) + " minutes " + str(int(duration % 60)) + " seconds to complete.")
    wordfile.close()

if __name__ == "__main__":
    main()
