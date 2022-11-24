from libs.ProgressChecker import GoogleSpreadsheet
from Parser import parse
from threading import Thread


def run(name, repo_addr):
    # todo multi thread로 변경
    res = gs.crawl(repo_addr, {"since": "2022-11-07T02:00:50Z"})
    # print('404인지', res.status_code == 404)
    if res.status_code == 404:
        print(f"{name}학생의 repository주소로 호출이 안되고 있습니다. 주소:{repo_addr}")
    html_text = res.text
    result = parse(html_text)
    print(name, result)


if __name__ == '__main__':
    sheet_url = "https://docs.google.com/spreadsheets/d/1cJ9XQDISo3B6UHzcDmWtG9ucDRDg_YgJPkkW9atCFjk"
    sheet_name = "repositories"
    gs = GoogleSpreadsheet(sheet_url)
    repo_sheet_target_columnNo = 1 # 1은 algorithm 2는 springboot 3은 mustache
    gs.update_student_list()
    student_list = gs.read_saved_student_repo_list()
    # r = gs.crawl_and_parse(student_list[0][repo_sheet_target_columnNo])
    # html_text = open('github_commit_page2.html', encoding='utf-8').read()
    # print(parse(html_text))
    for arr in student_list[0:]:
        try:
            # Thread(target=run, args=(arr[0], arr[repo_sheet_target_columnNo])).start()
            run(arr[0], arr[repo_sheet_target_columnNo])
        except Exception as e:
            print(e)

