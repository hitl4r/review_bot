import pyautogui as pg
import time
import random as rd
import clipboard as clp

gmail_acc_link = "https://accounts.google.com/signup/v2/"
verify_link = "sms-activate.ru/ru/stat"
move_time = 1
l_sleep_time = 10
s_sleep_time = 1

def clear_cookies():
    try:    
        x = pg.locateCenterOnScreen('img/cookies.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(s_sleep_time)
        pg.locateCenterOnScreen('img/cookies_2.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        print('Cookies cleared succesfully!')
    except:
        pg.alert(text='Could not clear cookies.', title='error', button='OK')

def new_card():
    try:
        x = pg.locateCenterOnScreen('img/new_card.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(s_sleep_time)
    except:
        pg.alert(text='Could not open a new tab.', title='error', button='OK')

def change_profile_picture():
    pass

#gmail account creator

def gmail(adress, password, f_name, l_name, born_y, born_d):
    clear_cookies()
    new_card()
    pg.write(gmail_acc_link)
    pg.press('enter')
    time.sleep(l_sleep_time)
    try:
        x = pg.locateCenterOnScreen('img/middle.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/first_name.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()

        #filling 1st form
        pg.write(f_name)
        time.sleep(s_sleep_time)
        pg.press('tab')
        pg.write(l_name)
        time.sleep(s_sleep_time)
        pg.press('tab')
        pg.write(adress)
        time.sleep(s_sleep_time)
        pg.press('tab')
        pg.press('tab')
        pg.write(password)
        time.sleep(s_sleep_time)
        pg.press('tab')
        pg.write(password)
        pg.press('tab')
        pg.press('tab')
        pg.press('enter')
        print('1st form filled succesfully!')
    except:
        pg.alert(text='Could not fill the first form.', title='error', button='OK')

    try:
        x = pg.locateCenterOnScreen('img/look_for.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.write('chrome')
        time.sleep(l_sleep_time)
        pg.write(verify_link)
        pg.click('enter')
        time.sleep(s_sleep_time)
        x = pg.locateCenterOnScreen('img/gyg_btn.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(s_sleep_time)
        x = pg.locateCenterOnScreen('img/act_b1.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(s_sleep_time)
        x = pg.locateCenterOnScreen('img/act_b2.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
    except:
        pg.alert(text='Could not open verification site.', title='error', button='OK')

    try:
        x = pg.locateCenterOnScreen('img/copy_number.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.hotkey('alt', 'tab')
        pg.write('+52')
        pg.write(clp.get())
        x = pg.locateCenterOnScreen('img/next.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
        pg.hotkey('alt', 'tab')
    except:
        pg.alert(text='Could not fill phone number into a form.', title='error', button='OK')

    while True:
        try:
            x = pg.locateCenterOnScreen('img/kod_na_sms.png')
            pg.moveTo(x[0], x[1], move_time)
            pg.move(0, 40)
            pg.doubleclick()
            pg.hotkey('ctrl', 'c')
            break
        except:
            time.sleep(l_sleep_time)
    try:
        pg.hotkey('alt', 'tab')
        time.sleep(s_sleep_time)
        pg.hotkey('ctrl', 'v')
        x = pg.locateCenterOnScreen('img/verify.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
    except:
        pg.alert(text='Could not fill verification code into a form.', title='error', button='OK')

    try:
        x = pg.locateCenterOnScreen('img/month.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.move(0, 40, move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/day.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.write(born_d)
        x = pg.locateCenterOnScreen('img/year.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.write(born_y)
        x = pg.locateCenterOnScreen('img/gender.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.move(0, 40, move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/next.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
    except:
        pg.alert(text='Could not fill personal info.', title='error', button='OK')


    try:
        x = pg.locateCenterOnScreen('img/im_in.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
        pg.scroll(-3000)
        x = pg.locateCenterOnScreen('img/agree.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(l_sleep_time)
        time.sleep(l_sleep_time)
        print('Account created succesfully.')
    except:
        pg.alert(text='Could not agree to additional info.', title='error', button='OK')

    try:
        change_profile_picture()
    except:
        pg.alert(text='Could not change the profile picture.', title='error', button='OK')

#google maps reviewer

def review(link, text):
    new_card()
    pg.write(link1)
    pg.press('enter')
    time.sleep(l_sleep_time)
    try:
        x = pg.locateCenterOnScreen('img/directions.png')
        pg.moveTo(x[0], x[1], move_time)
    except:
        pg.alert(text='Could not find the review button.', title='error', button='OK')
    
    for i in range(20):
        try:
            x = pg.locateCenterOnScreen('img/write.png')
            pg.moveTo(x[0], x[1], move_time)
            pg.click()
            time.sleep(l_sleep_time)
            break
        except:
            pg.alert(text='Could not find the review button.', title='error', button='OK')
    try:
        x = pg.locateCenterOnScreen('img/stars.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/yes.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/quality.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        x = pg.locateCenterOnScreen('img/share.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        pg.write(text)
        x = pg.locateCenterOnScreen('img/post.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
        time.sleep(s_sleep_time)
        x = pg.locateCenterOnScreen('img/done.png')
        pg.moveTo(x[0], x[1], move_time)
        pg.click()
    except:
        pg.alert(text='Could not write the review.', title='error', button='OK')

def change_text(text, name):
    return text.replace('<name>', name)

def gmaps(link1, link2, link3, main_link, text1, text2, text3, main_text):
    review(link1, text1)
    print('First review written succesfully.')
    time.sleep(s_sleep_time)
    review(link2, text2)
    print('Second review written succesfully.')
    time.sleep(s_sleep_time)
    review(link3, text3)
    print('Third review written succesfully.')
    time.sleep(s_sleep_time)
    review(main_link, main_text)
    print('Main review written succesfully!')

#inputs and random data
adress = input('Enter email adress: ')
password = input('Enter password: ')
f_name = input('Enter first name: ')
l_name = input('Enter last name: ')
born_y = rd.randint(1970, 2000)
born_d = rd.randint(1, 28)

link1 = input('Enter first place link: ')
name1 = input('Enter first place name: ')
text1 = input('Enter first place review text: ')
link2 = input('Enter second place link: ')
name2 = input('Enter second place name: ')
text2 = input('Enter second place review text: ')
link3 = input('Enter third place link: ')
name3 = input('Enter third place name: ')
text3 = input('Enter third place review text: ')

main_link = input('Enter main place link: ')
main_name = input('Enter main place name: ')
main_text = input('Enter main place review text: ')

text1 = change_text(text1, name1)
text2 = change_text(text2, name2)
text3 = change_text(text3, name3)
main_text = change_text(main_text, main_name)

#main part
gmail(adress, password, f_name, l_name, born_y, born_d)
gmaps(link1, link2, link3, main_link, text1, text2, text3, main_text)

print('Job done!')
