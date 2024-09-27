from time import sleep

from let_code.library.lib import Base
from let_code.utilities.locatorsHub import Text_locators

class Text(Base):

    def text_(self,text,text1,text2,text3,text4,value):

        self.click_on_an_element(Text_locators.text_link)
        self.send_text_to_an_element(Text_locators.first_name,text)
        self.Get_size(Text_locators.first_name)
        self.Get_tagname(Text_locators.first_name)
        self.Get_location(Text_locators.first_name)
        self.Get_both_size_and_location(Text_locators.first_name)
        self.Get_attribute(Text_locators.first_name,value)

        self.clear_a_text(Text_locators.text)
        self.send_text_to_an_element(Text_locators.text,text1)
        self.clear_a_text(Text_locators.text2)
        self.send_text_to_an_element(Text_locators.text2,text2)
        self.clear_a_text(Text_locators.text3)
        self.send_text_to_an_element(Text_locators.text3,text3)

        self.navigational_command_back()

        self.click_on_an_element(Text_locators.link_2)
        sleep(1)
        self.click_on_an_element(Text_locators.button1)
        sleep(1)
        self.navigational_command_back()

        self.navigational_command_back()
        self.click_on_an_element(Text_locators.dropdown_link)
        self.select_an_option(Text_locators.select,Text_locators.option)
        self.select_an_option(Text_locators.select, Text_locators.option1)
        self.select_an_option(Text_locators.select, Text_locators.option2)
        self.select_an_option(Text_locators.select, Text_locators.option3)
        self.select_an_option(Text_locators.select, Text_locators.option4)

        self.select_an_option(Text_locators.select2, Text_locators.option5)
        self.select_an_option(Text_locators.select2, Text_locators.option6)
        self.select_an_option(Text_locators.select2, Text_locators.option7)
        self.select_an_option(Text_locators.select2, Text_locators.option8)
        self.select_an_option(Text_locators.select2, Text_locators.option9)
        self.select_an_option(Text_locators.select2, Text_locators.option10)


        self.select_an_option(Text_locators.select3, Text_locators.option11)
        self.select_an_option(Text_locators.select3, Text_locators.option12)
        self.select_an_option(Text_locators.select3, Text_locators.option13)
        self.select_an_option(Text_locators.select3, Text_locators.option14)
        self.select_an_option(Text_locators.select3, Text_locators.option15)

        self.select_an_option(Text_locators.select4, Text_locators.option16)
        self.select_an_option(Text_locators.select4, Text_locators.option17)
        self.select_an_option(Text_locators.select4, Text_locators.option18)
        self.select_an_option(Text_locators.select4, Text_locators.option19)
        self.select_an_option(Text_locators.select4, Text_locators.option20)
        self.select_an_option(Text_locators.select4, Text_locators.option21)
        self.select_an_option(Text_locators.select4, Text_locators.option22)
        self.select_an_option(Text_locators.select4, Text_locators.option23)
        self.select_an_option(Text_locators.select4, Text_locators.option24)
        self.select_an_option(Text_locators.select4, Text_locators.option25)
        self.select_an_option(Text_locators.select4, Text_locators.option26)
        self.select_an_option(Text_locators.select4, Text_locators.option27)


        self.navigational_command_back()

        self.click_on_an_element(Text_locators.alert_link)
        self.click_on_an_element(Text_locators.alert1)
        self.dismiss_alert()

        self.click_on_an_element(Text_locators.alert2)
        self.accept_alert()

        self.click_on_an_element(Text_locators.alert3)
        self.sendtxt_to_an_alert(text4)
        self.dismiss_alert()

        self.click_on_an_element(Text_locators.alert4)
        self.click_on_an_element(Text_locators.close_btn)

        self.click_on_an_element(Text_locators.drag_link)
        sleep(2)
        self.drag_and_drop_by_offset(Text_locators.drag,10,0)

        self.click_on_an_element(Text_locators.radio_btn)
        self.click_on_an_element(Text_locators.yes)
        self.click_on_an_element(Text_locators.no3)
        self.click_on_an_element(Text_locators.yes3)
        self.click_on_an_element(Text_locators.yes2)
        self.click_on_an_element(Text_locators.no2)
        self.click_on_an_element(Text_locators.no)


