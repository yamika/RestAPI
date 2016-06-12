# coding utf-8
import pprint
import requests
import json

def main():
    #GETパラメータはparams引数に辞書で指定する

    response = requests.get(
        'http://qiita.com/api/v2/items/3eb6d860e115c7e44086/comments')
    pprint.pprint(response.json())

    obj = response.json()

    for i in range(len(obj)):
       id = obj[i]['user']['id']
       print (id)


if __name__== '__main__':
    main()
