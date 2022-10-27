from bs4 import BeautifulSoup

def parse(html_string):
    bsobj = BeautifulSoup(html_string, "html.parser")
    timelineItembody = bsobj.find("div", {"class":"TimelineItem-body"})
    h2 = timelineItembody.find("h2")
    msg = f'{h2.text}'
    return msg

if __name__ == '__main__':
    file = open("gitcommit.html", encoding="utf-8")
    parse(file.read())