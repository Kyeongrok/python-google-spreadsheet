import gspread, os
import requests, json
from Parser import parse


class GoogleSpreadsheet:
    gc = gspread.service_account(filename=os.getenv("GS_KEY_PATH"))
    sheet_url = ''
    workbook = None

    def __init__(self, sheet_url):
        self.sheet_url = sheet_url

    def read(self, sheet_name, range):
        '''
        구글스프레드시트에서 불러오기
        '''
        if self.workbook == None:
            self.workbook = self.gc.open_by_url(self.sheet_url)

        sh = self.workbook.worksheet(sheet_name)
        # sh = gc.open("명렬표").worksheet("repositories")
        return sh.get(range)

    def read_saved_student_repo_list(self, filename="student_list.csv"):
        f = open(filename, encoding="utf-8")
        r = []
        for line in f.readlines():
            r.append(line.split(","))
        return r

    def crawl(self, base_url, params={"since": "2022-10-27T10:50:50Z"}):
        # git repo주소로 crawl해서
        url = base_url + "/commits"
        res = requests.get(url, params=params)
        print(res, url)
        return res.text

    def crawl_and_parse(self, giturl):
        html_str = self.crawl(giturl)
        r = parse(html_str)
        print(r)
        return r

    def save_to_csv(self, arr):
        # todo
        # google spreadsheet에서 받은 arr을 csv로 convert한 후 파일로 저장
        # gs api call을 줄이기 위함
        file = open("student_list.csv", "w+", encoding="utf-8")
        for row in arr:
            s = ""
            for item in row:
                item = item.replace(".git","")
                s += f'{item},'

            file.write(f'{s}\n')

    def update_student_list(self, sheet_name='repositories'):
        repositories_arr = self.read(sheet_name, 'A2:D88')
        self.save_to_csv(repositories_arr)
        print(f"google spreadsheet {sheet_name} 을 참조하여 student_list.csv를 업데이트 했습니다.")

    def writeRange(self, sheet_name, range):
        sh = self.workbook.worksheet(sheet_name)

        for row_num in range(4, 90 + 1):
            sh.update_cell(row_num, 7, 'test')
