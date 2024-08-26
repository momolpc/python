
'''
File I/O
'''
from pathlib import Path 

#文件路径
path = Path("foldername/filename.txt") 

# 读取文件，并去掉末尾空行
contents = path.read_text().rstrip() 

#按行读取
lines = contents.splitlines() 
for line in lines:
    print(line)

# 连接文件每行内容
lines = contents.splitlines()
string = ''
for line in lines:
    string += line 

print(string)

# 打印某些位数
print(f'{string[:50]}...') 

# 写入文件 *只能写入字符串，数字需要先str()
path.write_text('text')

# 写入多行
contents = 'text 1\n'
contents += 'text 2\n'
contents += 'text 3\n'

path.write_text('contents')






'''
Try-Except
'''
# try - except
try:
    print(5/0)
except ZeroDivisionError:
    print('You can't divide by Zero')


# 一直提示到用户输入其他答案
while True:
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You can't divide by 0!')
    else:
        print(answer)

# FileNotFoundError
path = Path('filename.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'Sorry, the file {path} does not exist.')

# 分析文本单词 split()
path = Path('filename.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'Sorry, the file {path} does not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {path} has about {num_words} words')

# 定义函数
from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'Sorry, the file {path} does not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words')

path = Path('filename.txt')
count_words(path)

# 静默失败
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # 继续运行，什么都不要做
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words')

path = Path('filename.txt')
count_words(path)


# 存储数据 json.dumps(), json.loads()

# 存储数据
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('number.json')
contents = json.dumps(numbers) 
path.write_text(contents)


# 读取数据
path = Path('number.json')
contents = json.dumps(numbers) 
numbers = json.loads(contents)
print(numbers)

