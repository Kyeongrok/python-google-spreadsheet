import gspread, os
import requests, json

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
        url = base_url.replace("github.com", "api.github.com/repos")+"/commits"
        # print(url)
        res = requests.get(url)
        j = res.json()
        commit0 = j[0]['commit']
        return commit0
        # print(json.dumps(j))

    def writeRange(self, sheet_name, range):
        sh = self.workbook.worksheet(sheet_name)
        cell_list = sh.range(range)

        for cell in cell_list:
            cell.value = 'test'




if __name__ == '__main__':
    sheet_url = "https://docs.google.com/spreadsheets/d/1cJ9XQDISo3B6UHzcDmWtG9ucDRDg_YgJPkkW9atCFjk/edit#gid=2033806681"
    sheet_name = "repositories"
    gs = GoogleSpreadsheet()
    r = gs.read(sheet_url, sheet_name, 'A2:D88')
    print(json.dumps(r))
    # for arr in r:
        # commit0 = gs.crawl(arr[3])
        # print(arr[0], commit0['committer']['date'], commit0['message'], commit0['committer']['name'])
