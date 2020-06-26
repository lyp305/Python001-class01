import requests
from bs4 import BeautifulSoup as bs

import pandas as pd


def getMoviesByCnt(myurl, cnt):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'

    header = {'user-agent': user_agent}
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    iDetailList = []
    index = 1
    # bsdetail = bs_info.find_all('dd', limit=cnt)
    # print(bsdetail)
    # for movies in bsdetail:
    #     print(movies)
    #     while index > cnt:
    #         break
    for movie in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}, limit=cnt):
        iDetail = []
        iDetail.append(movie.find('span', attrs={'class': 'name'}).text)
        hover = movie.find_all('div', attrs={'class': 'movie-hover-title'})
        for hoverDiv in hover:

            itext = hoverDiv.find('span', ).text

            if itext == '上映时间:' or itext == '类型:':
                iDetail.append(hoverDiv.text.replace('\n', '').replace(' ', ''))
        iDetailList.append(iDetail)
    movieData = pd.DataFrame(data=iDetailList)


# windows需要使用gbk字符集
    movieData.to_csv('./movie.csv', encoding='utf8', index=False, header=False)

getMoviesByCnt('https://maoyan.com/films?showType=3', 10)
