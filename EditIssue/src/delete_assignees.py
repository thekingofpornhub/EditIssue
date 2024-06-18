"""
删除指定issue中指定的assignees

"""
import requests
import ast
import log_message
def delete_assignees(repo, delete_info, token):
    # 创建一个字典来存储删除结果
    delete_result = {}
    people_list = []
    success = 0
    fail = 0
    result_path = "./result/delete_assignees_result.txt"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    proxies = {
        "http": None,
        "https": None,
    }

    # 删除指定issue number中的指定assign人员
    for issue in delete_info:
        url = f"https://api.github.com/repos/{repo}/issues/{issue['number']}/assignees"

        peoples = ast.literal_eval(issue['peoples'])
        for people in peoples:
            response = requests.delete(url, headers=headers, json={'assignees': people}, proxies=proxies)
            try:
                assert response.status_code == 200
            except AssertionError as err:
                print("location:delete_assigness-33")##############
                log_message.log(url,response.status_code)###########
            else:
                people_list.append(people)
                delete_result[issue['number']] = people_list
                success += 1
        people_list = []

    # 保存最终的delete assignees信息
    with open(result_path, 'w') as file:
        for issue_number, infos in delete_result.items():
            for info in infos:
                    file.write(f'Deleted peoples {info} in Issue {issue_number} successfully\n')

    # 汇总
    print('='*78)
    print(f'Total: {success + fail}    success: {success}    fail: {fail}\nPlease check the delete results from delete_result.txt in the result directory')
    print('='*78)