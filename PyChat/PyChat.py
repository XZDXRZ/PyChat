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

#主程序开始
os.system('color 0a')
print('Hello！我是 兄主的仙人掌 创作的机器人 PyChat ，我们现在可以聊天了！（输入.exit或.quit退出）')
#主循环开始
while True:
    data['info'] = str(input('> '))
    if '运行' in data['info'] or '.run' in data['info']:
        if data['info'].split(' ')[2] == '-s':
            exe = data['info'].split(' ')[1]
            os.system(exe)
        else:
            exe = data['info'].split(' ')[1]
            pn = int(data['info'].split(' ')[2])
            os.system(path[pn]+'/'+exe)
    elif '.kw' in data['info'] or '抓关键词' in data['info']:
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
    elif data['info'].split(' ')[0] == '.cf' or data['info'].split(' ')[0] == '温度转换':
        mode = data['info'].split(' ')[1]
        test = int(data['info'].split(' ')[2])
        if mode == '-c':
            print((test - 32)/1.8)
        elif mode == '-f':
            print(test*1.8+32)
        else:
            print('没有找到 '+mode+' 这种模式')
    elif data['info'] == '.pd' or data['info'] == '.pathdir':
        i = 0
        print('Num\tPath')
        print('-------------------------------------------------------------------------------')
        for p in path:
            print(str(i)+'\t'+str(p))
            i+=1
        print('-------------------------------------------------------------------------------')
    elif data['info'] == '.exit' or data['info'] == '.quit' or data['info'] == '拜拜' or data['info'] == '再见':
        #当用户输入.exit或.quit时退出程序
        print('PyChat: "'+random.choice(bye)+'"')
        time.sleep(1)
        break
    else:
        reponse = requests.post(url,headers=headers,data=data)
        rep = json.loads(reponse.text)
        print('PyChat: "'+rep['text']+'"')