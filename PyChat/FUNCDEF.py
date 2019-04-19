'''Function Define'''

import requests,json,os,random,time

bye = ['拜拜','再见','回头见']
url = 'http://www.tuling123.com/openapi/api'
data = {
    'key' : 'b273a7286caa44108b8b20b6cfec1403',
    'info' : 'Hello',
    'userid' : 'PyChat Robot'
}
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
path = open('exe.path','r').read().split(';')

def FPRINT(str):
    print('PyChat: "'+str+'"')

def run_programme():
    if data['info'].split(' ')[2] == '-s':
        exe = data['info'].split(' ')[1]
        os.system(exe)
    else:
        exe = data['info'].split(' ')[1]
        pn = int(data['info'].split(' ')[2])
        os.system(path[pn]+'/'+exe)

def print_path_table():
    i = 0
    print('Num\tPath')
    print('-------------------------------------------------------------------------------')
    for p in path:
        print(str(i)+'\t'+str(p))
        i+=1
    print('-------------------------------------------------------------------------------')

def say_bye():
    FPRINT(random.choice(bye))
    time.sleep(1)

def chat():
    reponse = requests.post(url,headers=headers,data=data)
    rep = json.loads(reponse.text)
    FPRINT(rep['text'])

def catch_key_word():
    n = data['info'].split(' ')[1]
    w = {
        'type' : 'all',
        'content' : n
    }
    r  = requests.post('http://ictclas.nlpir.org/nlpir/index5/getKeyWords.do',data = w,headers=headers)
    kw = json.loads(r.text)['keywords'].split('#')
    i = 0
    for word in kw:
        if word != '':
            print(word,end = '')
            if kw[i+1] != '':
                print('，',end = '')
        i+=1
    print('')

def temp_change():
    mode = data['info'].split(' ')[1]
    test = int(data['info'].split(' ')[2])
    if mode == '-c':
        print((test - 32)/1.8)
    elif mode == '-f':
            print(test*1.8+32)
    elif mode == '--help':
        print('-c : 华氏度至摄氏度')
        print('-f : 摄氏度至华氏度')
    else:
        print('没有找到 '+mode+' 这种模式')