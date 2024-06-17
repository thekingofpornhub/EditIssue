"""
给指定issue删除labels

"""
#ok
import requests
import ast
from src.find_labels import find_labels
import log_message
def delete_labels(repo, issues, token):
    # 创建一个字典来存储delete labels的结果
    delete_labels_infos = {}
    label_list = []
    success = 0
    fail = 0
    result_path = "./result/delete_labels_result.txt"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    proxies = {
        "http": None,
        "https": None,
    }

    
    for issue in issues:
        if issue['label']:
            # Labels 的信息
            if(isinstance(issue['label'], str)):
                try:
                    labels = ast.literal_eval(issue['label'])
                except (ValueError, SyntaxError) as e:
                    print(f"Error parsing label: {e}")
                    labels = issue['label']
            else:
                labels = issue['label']
            for label in labels:
                # 构造请求 URL
                url = f"https://api.github.com/repos/{repo}/issues/{issue['number']}/labels/{label}"

                response = requests.delete(url, headers=headers, proxies=proxies)

                
                # 当返回状态码为404的时候，去查找该issue的labels，若labels已经不存在，则视为删除成功，否则删除失败
                try:
                    assert response.status_code != 200
                    label_list.append(label)
                    delete_labels_infos[issue['number']] = label_list
                    success += 1
                except:
                    print("location:delete_labels-49")#
                    log_message.log(response.status_code)#

            label_list = []
        else:
            delete_labels_infos[issue['number']] = [f"issue {issue['number']} no need to delete labels"]
    # 汇总
    print('='*92)
    print(f'Total: {success + fail}    success: {success}    fail: {fail}\nPlease check the delete labels results from delete_labels_result.txt in the result directory')
    print('='*92)
