
import telebot
from selenium import webdriver
from time import sleep
from telebot import  types

driver= webdriver.Chrome()

bot=telebot.TeleBot('Tokken')

@bot.message_handler(commands=['start'])
def start(message):
    markup= types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/vacancy')
    #markup.row('/gut')
    bot.send_message(message.chat.id, 'Привет,что тебе интересно?', reply_markup=markup)



@bot.message_handler(commands=['vacancy'])
def vacancy(message):
    msg=bot.send_message(message.chat.id, "Введите название вакансии")
    bot.register_next_step_handler(msg, search)
'''
@bot.message_handler(commands=['gut'])
def gut(message):
    bot.send_message(message.chat.id, 'Загружаю последние новости')
    naz='https://www.sut.ru/bonchevents'
    driver.get(naz)
    sleep(2)
    try:
        for i in range(1,6):
            if i !=3:
                gutn=driver.find_elements_by_class_name('vt287')
                bot.send_message(message.chat.id, gutn[0].get_attribute('href'))
                
            else:
                print('lol')
    except:
        bot.send_message(message.chat.id, 'Новостей нет') 

'''
@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Ты что то хотел?')


def search(message):
    bot.send_message(message.chat.id, 'Начинаю поиск')   
    nazvaniy='https://spb.hh.ru/search/vacancy?clusters=true&area=2&ored_clusters=true&experience=noExperience&enable_snippets=true&salary=&text='+ message.text 
    driver.get(nazvaniy)
    sleep(2)
    try:
        for i in range(1,6):
            if i != 3:
                vacan = driver.find_elements_by_xpath(
                    f'/html/body/div[6]/div/div[1]/div[3]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div[{i}]/div[2]/div/span/span/span/a')
                print(vacan)
                print(type(vacan))
                print(len(vacan))
                #bot.send_message(message.chat.id, vacan[0].get_attribute('href'))
                bot.send_message(message.chat.id, vacan[0].get_attribute('href'))
            else:
                print('lol')
    except:
        bot.send_message(message.chat.id, 'Такой вакансии нет')


    
    for i in range(len(vacan)):
        bot.send_message(message.chat.id, vacan[i].get_attribute('href'))
        print( vacan[i].get_attribute('href'))
        
    
    
    


bot.polling()
