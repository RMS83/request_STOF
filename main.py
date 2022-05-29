from pprint import pprint
import requests as requests
import time

class StackOverflow:
    def __two_days_ago(self):
        time_ = time.localtime()
        time_erl = (time_.tm_year, time_.tm_mon, time_.tm_mday, time_.tm_hour - 48,
                    time_.tm_min, time_.tm_sec, time_.tm_wday, time_.tm_yday, time_.tm_isdst)
        earlier_time_unix = int(time.mktime(time_erl))
        return earlier_time_unix

    def get_title_questions_dict(self, tag_):
        page_number = 0
        count = 0
        while True:
            time.sleep(2)
            url_ = f'https://api.stackexchange.com/2.3/questions'
            page_number += 1
            params = {'page': page_number,
                      'pagesize': '100',
                      'fromdate': self.__two_days_ago(),
                      'todate': int(time.time()),
                      'tagged': tag_,
                      'site': 'stackoverflow',
                      'filter': '!bBWAN5DQm(mJin'}
            resp = requests.get(url_, params=params)
            if resp.json():
                for list_ in resp.json()['items']:
                    dict_ = {k: v for k, v in list_.items() if k == 'title'}
                    count += 1
                    pprint(dict_)
            else:
                break
        print(f'{count} вопросов с тегом {tag_}')

if __name__ == '__main__':
    rez = StackOverflow()
    pprint(rez.get_title_questions_dict('python'))




