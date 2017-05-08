# encoding=utf-8
from Tkinter import *
import tkMessageBox
import requests
import json
import time

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


def createWnd():
    global root
    global listBox
    global text

    root = Tk()
    root.title('-----DemoPlayer------来自网易云音乐-----')

    center_window(root, 440, 250)

    root['background'] = '#C7EDCC'

    text = Entry(font='宋体', width=36)
    text.pack()
    button = Button(root, text='搜索', width=18, fg='red', background='#CDCDC1', command=searchM).pack()

    listBox = Listbox(root, height=24, width=72, background='#C7EDCC')
    listBox.bind('<Double-Button-1>', play)
    listBox.pack()
    root.mainloop()

def searchM():
    global m_List
    itemCount =20

    if not text.get():
        tkMessageBox.showinfo('温馨提示', '您可以输入以下内容进行搜索\n1.歌曲名\n2.歌手名\n3.部分歌词')
        return

    # 获得输入的歌名
    url = 'http://s.music.163.com/search/get/?type=1&s=%s&limit=%s' % (text.get(), itemCount)

    # get请求
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    html = requests.get(url, header)
    data = json.loads(html.text)
    m_List = []

    try:
        listBox.delete(0, listBox.size())
        for MusicData in data['result']['songs']:
            listBox.insert(END, MusicData['name'] + '------' + '(' + MusicData['artists'][0]['name'] + ')')
            m_List.append(MusicData['audio'])
    except Exception as e:
        tkMessageBox.showinfo('温馨提示', '查询过程出现错误，请重试')
        # print '查询过程出现错误，请重试'
p=None
import  subprocess
def play(args):
    try:
        global p
        sy = listBox.curselection()[0]
        p = subprocess.Popen(["mpg123", m_List[int(sy)]])
        time.sleep(100)
        stop()
    except Exception as e:
        pass
def stop():
    global p
    if p:
        p.terminate()
        p = None

def main():
    createWnd()


if __name__ == '__main__':
    main()