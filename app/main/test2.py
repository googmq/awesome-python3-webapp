import requests, re, json, time


def alla():
    n = 1000010000
    while n < 1439189657:
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
            key = a['file']['key']

            realurl = 'http://img.hb.aicdn.com/' + key
            print(realurl)

            with open(key[:5] + '' + str(int(time.time())) + '.jpg', 'wb') as f:
                f.write(requests.get(realurl).content)

        except Exception as e:
            print(e)
            time.sleep(1)
            n = n + 1
            continue
        n = n + 1


if __name__ == '__main__':
    alla()
