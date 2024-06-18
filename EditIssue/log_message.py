
def log(url, response):
    if response.status_code %100== 4:
        print(f"{url} Not Found {response.status_code}")
    elif response.status_code %100== 3:
        print(f"{url} Redirect {response.status_code}")
    elif response.status_code %100== 5:
        print(f"{url} Internal Server Error {response.status_code}")

def httperror(http_err,response):
    print(f"HTTP error occurred: {http_err}")
    print(f"Response: {response.json()}")
def elseerror(err):
    print(f"Other error occurred: {err}")

def signment(issue,err):
    print(f"An error occurred when assign issue {issue['number']}. The error message is: {err}")
