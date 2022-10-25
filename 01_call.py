import gspread, os


def read(sheet_url, sheet_name, range):
    '''
    구글스프레드시트에서 불러오기
    '''
    gc = gspread.service_account(filename=os.getenv("GS_KEY_PATH"))
    sh = gc.open_by_url(sheet_url).worksheet(sheet_name)
    # sh = gc.open("명렬표").worksheet("repositories")
    return sh.get(range)


if __name__ == '__main__':
    sheet_url = "https://docs.google.com/spreadsheets/d/1cJ9XQDISo3B6UHzcDmWtG9ucDRDg_YgJPkkW9atCFjk/edit#gid=2033806681"
    sheet_name = "repositories"
    for arr in read(sheet_url, sheet_name, 'A2:D88'):
        print(arr)