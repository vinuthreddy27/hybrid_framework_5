from let_code.POM.text_page import Text


def test_text(driver):
    text_page_obj=Text(driver)
    text_page_obj.text_("vinuth",
                        "i am too  good what about you....",
                        "heyy .....",
                        "......",
                        "vinuth",
                        "id")

