from bs4 import BeautifulSoup
from datetime import datetime
import pytz



def li_parse(li):
    details = li.find("div", {"class":"Details"})
    a_tag = details.find("a")
    p_mb1_a = details.find("p", {"class":"mb-1"}).find("a")
    relative_time = details.find("relative-time")
    # hh시 mm분
    dt = datetime.strptime(relative_time['datetime'], "%Y-%m-%dT%H:%M:%SZ")
    tz = pytz.timezone("Asia/Seoul")
    aware_dt = tz.localize(dt)
    commit_datetime = aware_dt.strftime("%d일%H:%M")
    commit_message = p_mb1_a.text
    return {"commit_message":commit_message, "commit_datetime":commit_datetime}

def parse(html_string):
    bsobj = BeautifulSoup(html_string, "html.parser")
    timeline_itembody = None
    try:
        timeline_itembody = bsobj.find("div", {"class":"TimelineItem-body"})
    except:
        print("parsing error")
        return "지정한 날짜 이후의 commit이 없습니다."

    if timeline_itembody != None:
        h2 = timeline_itembody.find("h2")
        msg = f'{h2.text}'
        ol = timeline_itembody.find("ol")
        lis = ol.find_all()
        try:
            r_li_parse = li_parse(lis[0])
            msg += f'|{r_li_parse["commit_message"]} {r_li_parse["commit_datetime"]}'
        except:
            print('파싱 에러')
            pass
        return msg
