from resourse import RegistrationPage


def test_submit():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Smith')
    registration_page.fill_email('example@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_phone_number('5555555555')
    registration_page.fill_date_of_birth(15,5,1995)
    registration_page.fill_subject('Hist')
    registration_page.fill_hobby('Sports')
    registration_page.send_file('my_file.png')
    registration_page.fill_adress('test street address')
    registration_page.fill_state_city('NCR','Delhi')
    registration_page.submit()
    registration_page.should_have_registered('John Smith','example@mail.ru','Male','5555555555','15 May,1995','History','Sports','my_file.png','test street address','NCR Delhi')









