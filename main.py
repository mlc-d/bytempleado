# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# imports
import requests
from getpass import getpass
from random import seed
from jobs import get_users
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


baseUrl = 'http://localhost:1998'
ref_token = ''
acc_token = ''

credentials = {
        'name': 'dev',
        'password': 'test'
}


def

# login sending credentials
def login():
    credentials['name'] = input("Please enter your username: ")
    credentials['password'] = getpass()
    response = requests.post(baseUrl + '/login', json=credentials)
    print('login status code: ', response.status_code)
    global ref_token
    ref_token = response.cookies.values()[0]
    global acc_token
    acc_token = response.json()['accToken']


def refresh():
    response = requests.post(baseUrl + '/refresh', cookies=dict(refToken=ref_token))
    print('refresh status code: ', response.status_code)


def test():
    login()
    auth = {
        'accessToken': acc_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(baseUrl + '/api/v1/users', headers=auth)
    print('test status code: ', response.status_code)
    users = response.json()
    get_users(baseUrl + '/api/v1/users')
    for user in users:
        print(user)


def worker():
    # auth = {
    #     'accessToken': acc_token,
    #     'Content-Type': 'application/json'
    # }
    seed(1)
    # response = requests.get(baseUrl + '/api/v1/roles', headers=auth)
    # print('test 2 status code: ', response.status_code)
    # roles = response.json()
    # for role in roles:
    #    print(role['role'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test()
    worker()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
