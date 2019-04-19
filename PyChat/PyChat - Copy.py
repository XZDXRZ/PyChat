import os
from FUNCDEF import *

#主程序开始
os.system('color 0a')
print('Test Mode')
print('Hello！我是 兄主的仙人掌 创作的机器人 PyChat ，我们现在可以聊天了！（输入.exit或.quit退出）')
#主循环开始
while True:
    data['info'] = str(input('> '))
    if '运行' in data['info'] or '.run' in data['info']:
        run_programme()
    elif '.kw' in data['info'] or '抓关键词' in data['info']:
        catch_key_word()
    elif data['info'].split(' ')[0] == '.cf' or data['info'].split(' ')[0] == '温度转换':
        temp_change()
    elif data['info'] == '.pd' or data['info'] == '.pathdir':
        print_path_table()
    elif data['info'] == '.exit' or data['info'] == '.quit' or data['info'] == '拜拜' or data['info'] == '再见':
        say_bye()
        break
    else:
        chat()