from libs.ProgressChecker import GoogleSpreadsheet
from Parser import parse
from threading import Thread


def run(idx, repo_addr):
    # todo multi thread로 변경
    html_text = gs.crawl(repo_addr, {"since": "2022-10-27T10:50:50Z"})
    print(idx, parse(html_text))


if __name__ == '__main__':
    sheet_url = "https://docs.google.com/spreadsheets/d/1cJ9XQDISo3B6UHzcDmWtG9ucDRDg_YgJPkkW9atCFjk"
    sheet_name = "repositories"
    gs = GoogleSpreadsheet(sheet_url)
    student_list = gs.read_saved_student_repo_list()
    repo_sheet_target_columnNo = 2
    gs.update_student_list()
    # r = gs.crawl_and_parse(student_list[0][repo_sheet_target_columnNo])
    # html_text = open('github_commit_page2.html', encoding='utf-8').read()
    # print(parse(html_text))
    for arr in student_list:
        try:
            # Thread(target=run, args=(arr[0], arr[repo_sheet_target_columnNo])).start()
            run(arr[0], arr[repo_sheet_target_columnNo])
        except Exception as e:
            print(e)

