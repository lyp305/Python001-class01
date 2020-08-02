from selenium import webdriver
import traceback

import os
import pandas
import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'lyp'
}

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {'User-Agent': user_agent}
errors = []
browser = webdriver.Chrome()

conn = pymysql.connect(
    host=dbInfo['host'],
    port=dbInfo['port'],
    user=dbInfo['user'],
    password=dbInfo['password'],
    db=dbInfo['db'],
    charset='utf8mb4'
)

try:

    # url_base = 'https://movie.douban.com/subject/1292052/comments?status=P'
    url_base = 'https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=new_score&status=P&percent_type=l'

    browser.get(url_base)

    sql = 'INSERT INTO comments(mcomments, mrank, metime) VALUES (%s, %s, %s)'


    cur = conn.cursor()

    for index in range(1, 15):
        xpath1 = f'//*[@id="comments"]/div[{index}]/div[2]/p/span'
        xpath2 = f'//*[@id="comments"]/div[{index}]/div[2]/h3/span[2]/span[2]'
        xpath3 = f'//*[@id="comments"]/div[{index}]/div[2]/h3/span[2]/span[3]'

        ele1 = browser.find_element_by_xpath(xpath1)
        ele2 = browser.find_element_by_xpath(xpath2)
        ele3 = browser.find_element_by_xpath(xpath3)

        metime = ele3.text
        mrank = str(ele2.get_attribute('class')).replace('allstar', '').replace(' rating', '')
        print(mrank)
        mcomments = ele1.text

        cur.execute(sql, (mcomments, mrank, metime))

    cur.close()

except Exception as e:
    traceback.print_exc()
    print(e)
finally:
    # print('errors')
    # print(errors)
    browser.close()
    conn.commit()
    conn.close()

