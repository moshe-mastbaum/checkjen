import time

from selenium.webdriver.common.keys import Keys

from conf.initdriver import driver, action


class ToDosMethods:

    def create_item(self, name):
        driver.find_element_by_class_name("new-todo").send_keys(name)
        driver.find_element_by_class_name("new-todo").send_keys(Keys.RETURN)

    def filter_all(self):
        driver.find_element_by_css_selector("li[data-reactid='.0.2.1.0']").click()

    def list_items(self):
        return driver.find_elements_by_xpath("//ul[@class='todo-list']/li")

    def delete_item(self, index):
        item_delete = driver.find_element_by_tag_name("button")
        action.move_to_element(self.list_items()[index]).move_to_element(item_delete).click().perform()

    def get_item_number(self):
        return len(self.list_items())

    def delete_all_items(self):
        count = self.get_item_number()
        for i in range(0, count):
            self.delete_item(0)

    def toggle_item(self, index):
        self.list_items()[index].find_element_by_class_name("toggle").click()

    def filter_completed(self):
        driver.find_element_by_link_text("Completed").click()

    def filter_active(self):
        driver.find_element_by_link_text("Active").click()

    def clear_completed(self):
        driver.find_element_by_class_name("clear-completed").click()

    def get_items_left(self):
        return int(driver.find_element_by_xpath("//span[@class='todo-count']/strong").text)

    def get_item_name(self, index):
        return self.list_items()[index].find_element_by_tag_name("label").text

    def rename_item(self, index, new_name):
        char_count = len(self.get_item_name(index))
        item_name = self.list_items()[index].find_element_by_tag_name("label")
        action.double_click(item_name).perform()
        for i in range(0, char_count):
            self.list_items()[index].find_element_by_class_name("edit").send_keys(Keys.BACK_SPACE)
        self.list_items()[index].find_element_by_class_name("edit").send_keys(new_name)
        self.list_items()[index].find_element_by_class_name("edit").send_keys(Keys.RETURN)


class Test_ToDos(ToDosMethods):

    def setup_class(cls):
        # global driver, action
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://todomvc.com/examples/react/")
        time.sleep(3)
        driver.implicitly_wait(5)
        # action = ActionChains(driver)

    def teardown_class(cls):
        driver.quit()

    def setup_method(self):
        self.create_item("AAA")
        self.create_item("BBB")
        self.create_item("CCC")

    def teardown_method(self):
        self.filter_all()
        self.delete_all_items()

    def test_01_create_items(self):
        assert self.get_item_number() == 3

    def test_02_filter_completed(self):
        self.toggle_item(2)
        self.filter_completed()
        assert self.get_item_number() == 1

    # def test_03_filter_active(self):
    #     self.toggle_item(2)
    #     self.filter_active()
    #     assert self.get_item_number() == 2
    #
    # def test_04_clear_completed(self):
    #     self.toggle_item(2)
    #     self.clear_completed()
    #     assert self.get_item_number() == 2
    #
    # def test_05_items_left(self):
    #     assert self.get_items_left() == 3
    #
    # def test_06_rename_item(self):
    #     self.rename_item(2, 'DDD')
    #     assert self.get_item_name(2) == 'DDD'
    #
    # def test_07_delete_item(self):
    #     self.delete_item(0)
    #     assert self.get_item_number() == 2