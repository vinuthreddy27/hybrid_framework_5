from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import alert_is_present


class Base():

    def __init__(self,driver):
        self.driver=driver
        self.actions=ActionChains((self.driver))

    def search_for_an_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def click_on_an_element(self,locator):
        element=self.search_for_an_element(locator)
        element.click()

    def send_text_to_an_element(self, locator,text):
        element = self.search_for_an_element(locator)
        element.send_keys(text)

    def clear_a_text(self, locator):
        element = self.search_for_an_element(locator)
        element.clear()

    def Get_attribute(self, locator, attribute_name):
        element = self.search_for_an_element(locator)
        print(element.get_attribute(attribute_name))

    def Get_both_size_and_location(self, locator):
        element = self.search_for_an_element(locator)
        print(element.rect)

    def Get_tagname(self, locator):
        element = self.search_for_an_element(locator)
        print(element.tag_name)

    def Get_text(self, locator):
        element = self.search_for_an_element(locator)
        print(element.text)

    def Get_size(self, locator):
        element = self.search_for_an_element(locator)
        print(element.size)

    def Get_location(self, locator):
        element = self.search_for_an_element(locator)
        print(element.location)

    def element_dispalyed(self,locator):
        element=self.search_for_an_element(locator)
        print(element.is_displayed())

    def element_enabled(self,locator):
        element=self.search_for_an_element(locator)
        print(element.is_enabled())

    def element_selected(self, locator):
        element=self.search_for_an_element(locator)
        print(element.is_selected())

    def navigational_command_back(self):
        self.driver.back()

    def navigational_command_forward(self):
        self.driver.forward()

    def navigational_command_refresh(self):
        self.driver.refresh()

    def select_an_option(self,locator1,locator2):
        select_class=self.search_for_an_element(locator1)
        s1=Select(select_class)
        option_locator=self.search_for_an_element(locator2)
        s1.select_by_visible_text(option_locator.text)

    def select_an_option_by_value(self, locator1, locator2):
        select_class = self.search_for_an_element(locator1)
        s1 = Select(select_class)
        option_locator = self.search_for_an_element(locator2)
        s1.select_by_value(option_locator.text)

    def deselect_an_option(self, locator1):
        select_class = self.search_for_an_element(locator1)
        s1 = Select(select_class)
        s1.deselect_all()

    def deselect_an_option_by_value(self, locator1,locator2):
        select_class = self.search_for_an_element(locator1)
        s1 = Select(select_class)
        option_locator = self.search_for_an_element(locator2)
        s1.deselect_by_value(option_locator.text)

    def deselect_an_option_by_visisble_text(self, locator1,locator2):
        select_class = self.search_for_an_element(locator1)
        s1 = Select(select_class)
        option_locator = self.search_for_an_element(locator2)
        s1.deselect_by_visible_text(option_locator.text)

    def double_click(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.double_click(element).perform()

    def actionchain_click(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.click(element).perform()

    def context_click(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.context_click(element).perform()

    def hovering(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.move_to_element(element).perform()

    def drag_and_drop(self, locator,locator2):
        source_element = self.search_for_an_element(locator)
        target_element = self.search_for_an_element(locator2)
        self.actions.drag_and_drop(source_element,target_element).perform()

    def drag_and_drop_by_offset(self, locator,x,y):
        source_element = self.search_for_an_element(locator)
        self.actions.drag_and_drop_by_offset(source_element,x,y).perform()

    def Scroll_by_amount(self,x,y):
        self.actions.scroll_by_amount(x,y).perform()

    def Scroll_by_element(self, locator):
        source_element = self.search_for_an_element(locator)
        self.actions.scroll_to_element(source_element).perform()

    def Switch_to_frame(self):
        self.driver.swith_to_frame()

    def Swtich_to_default_frame(self):
        self.driver.swith_to.default_frame()

    def Switch_to_parent_frame(self):
        self.driver.swith_to.parent_frame()

    def accept_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def sendtxt_to_an_alert(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)

    def explicit_wait(self):
        wait=WebDriverWait(self.driver,12)
        element=wait.until(alert_is_present())
        element.accept()

    def select_A_Date(self,month,year):
        self.driver.find_element("xpath","//a[.='Date & Time']").click()
        current_month=self.driver.find_element("class name","datepicker-nav-month").text
        current_year=self.driver.find_element("class name","datepicker-nav-year").text

        while not (current_month.__eq__(month) and current_year.__eq__(year)):
            nextbtn=self.driver.find_element("xpath","//button[@class='datepicker-nav-next button is-small is-text']")
            nextbtn.click()
            current_month = self.driver.find_element("class name", "datepicker-nav-month").text
            current_year = self.driver.find_element("class name", "datepicker-nav-year").text
        self.driver.find_element("xpath", "//button[.='3']").click()




