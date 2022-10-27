import gspread, os
import requests, json
from Parser import parse

class GoogleSpreadsheet:
    gc = gspread.service_account(filename=os.getenv("GS_KEY_PATH"))
    workbook = None

    def __init__(self, sheet_url):
        self.workbook = self.gc.open_by_url(sheet_url)

    def read(self, sheet_name, range):
        '''
        구글스프레드시트에서 불러오기
        '''
        sh = self.workbook.worksheet(sheet_name)
        # sh = gc.open("명렬표").worksheet("repositories")
        return sh.get(range)

    def crawl(self, base_url):
        # git repo주소로 crawl해서
        url = base_url+"/commits"
        res = requests.get(url, params={"since":"2022-10-27T10:50:50Z"})
        print(res, url)
        return res.text

    def crawl_and_parse(self, giturl):
        html_str = self.crawl(giturl)
        r = parse(html_str)
        print(r)

    def save_to_csv(self, arr):
        # todo
        # google spreadsheet에서 받은 arr을 csv로 convert한 후 파일로 저장
        # gs api call을 줄이기 위함
        pass

    def writeRange(self, sheet_name, range):
        sh = self.workbook.worksheet(sheet_name)

        for row_num in range(4, 90 + 1):
            sh.update_cell(row_num, 7, 'test')

if __name__ == '__main__':
    sheet_url = "https://docs.google.com/spreadsheets/d/1cJ9XQDISo3B6UHzcDmWtG9ucDRDg_YgJPkkW9atCFjk"
    sheet_name = "repositories"
    gs = GoogleSpreadsheet(sheet_url)
    # r = gs.read(sheet_name, 'A2:D88')
    # repoSheetTargetColumnNo = 2
    # for arr in r:
    #     try:
    #         studentName = arr[0]
    #         html_text = gs.crawl(arr[repoSheetTargetColumnNo])
    #         print(html_text)
    #         parse(html_text)
    #     except Exception as e:
    #         print(e)
    # gs.writeRange('10.26', 'G4:G88')

