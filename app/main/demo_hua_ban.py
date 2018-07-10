import requests, re, json, time, pymongo


def alla():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb = myclient["test"]
    mycol = mydb["sites"]
    n = 1000100000
    while n < 1439189659:
        try:
            url = 'http://huaban.com/pins/' + str(n) + '/'
            response = requests.get(url).content
            res = str(response, 'utf-8')
            prog = re.compile(r'app\.page\["pin"\].*')
            appPins = prog.findall(res)

            pin0 = appPins[0]

            pin1 = pin0.replace('app.page["pin"] = ', '')
            pin2 = pin1.replace(';', '')
            a = json.loads(pin2)
            # url 的 key
            key = a['file']['key']
            # 来源
            rawtext = a['raw_text']
            # 描述
            title = a['board']['title']
            # 分类
            category = a['board']['category_id']

            realurl = 'http://img.hb.aicdn.com/' + key

            mydict = {'raw_text': rawtext, 'url': realurl, 'desc': title, 'category': category}

            x = mycol.insert_one(mydict)

            print(title)
        except Exception as e:
            print(e)
            time.sleep(1)
            n = n + 1
            continue
        n = n + 1


if __name__ == '__main__':
    alla()
