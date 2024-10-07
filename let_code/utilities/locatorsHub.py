from let_code.library.lib import Base


class Text_locators(Base):

    text_link=("xpath","//a[.='Edit']")
    first_name=("id","fullName")
    text=("id","join")
    text2=("id","getMe")
    text3=("id","clearMe")
    text4=("xpath","//input[@placeholder='Enter']")
    dont_write=("id","dontwrite")

    link_2=("xpath","//a[.='Click']")
    button1=("id","home")
    disbaled=("id","isDisabled")
    location=("id","position")
    property=("id","property")

    dropdown_link=("xpath","//a[.='Drop-Down']")
    select=("id","fruits")
    option=("xpath","//option[.='Apple']")
    option1=("xpath","//option[.='Mango']")
    option2=("xpath","//option[.='Orange']")
    option3=("xpath","//option[.='Banana']")
    option4=("xpath","//option[.='Pine Apple']")

    select2=("id","superheros")
    option5=("xpath","//option[@value='am']")
    option6=("xpath", "//option[@value='aq']")
    option7=("xpath", "//option[@value='ta']")
    option8=("xpath", "//option[@value='am']")
    option9=("xpath", "//option[@value='bt']")
    option10=("xpath", "//option[@value='bw']")

    select3=("id","lang")
    option11=("xpath", "//option[@value='java']")
    option12 =("xpath", "//option[@value='py']")
    option13 =("xpath", "//option[@value='swift']")
    option14=("xpath", "//option[@value='js']")
    option15=("xpath", "//option[@value='sharp']")

    select4=("id","country")
    option16 = ("xpath","//option[@value='Argentina']")
    option17 = ("xpath","//option[@value='Venezuela']")
    option18 = ("xpath","//option[@value='Paraguay']")
    option19 = ("xpath","//option[@value='Peru']")
    option20 = ("xpath","//option[@value='Ecuador']")
    option21 = ("xpath","//option[@value='Colombia']")
    option22 = ("xpath","//option[@value='Brazil']")
    option23 = ("xpath","//option[@value='India']")
    option24 = ("xpath","//option[@value='Chile']")
    option25 = ("xpath","//option[@value='Bolivia']")
    option26=("xpath","//option[@value='Suriname']")
    option27=("xpath","//option[@value='Uruguay']")

    alert_link=("xpath","//a[.='Dialog']")
    alert1=("id","accept")
    alert2=("id","confirm")
    alert3=("id","prompt")
    alert4=("id","modern")
    close_btn=("xpath","//button[@aria-label='close']")

    scroll=("xpath","//p[.=' Drag ']")
    drag_link=("xpath","//a[.='AUI - 1']")
    dragable1=("id","sample-box")


    drag_link2 = ("xpath", "//a[.='AUI - 2']")
    dragable = ("id", "draggable")
    dropable = ("id", "droppable")


    radio_btn=("xpath","//a[.='Toggle']")
    yes=("id","yes")
    no=("id","no")
    yes2=("id","one")
    no2=("id","two")
    yes3=("id","nobug")
    no3=("id","bug")
    going=("id","going")
    notgoing=("id","notG")
    maYBE=("id","maybe")
    check_box=("xpath","//label[.='Find if the checkbox is selected?']/..//input")
    check_box2=("xpath","//label[.='Accept the T&C']/..//input")


    slider=("xpath","//a[@href='/slider']")
    generate=("id","generate")
    button=("xpath","//button[.='Get Countries']")

    waits = ("xpath", "//a[@href='/waits']")
    accept = ("id", "accept")

    file=("xpath","//a[@href='/file']")
    upload=("xpath","//span[@class='file-icon']")
    exel=("xpath","//a[.='Download Excel']")
    pdf=("xpath","//a[.='Download Pdf']")
    text5=("xpath","//a[.='Download Text']")

