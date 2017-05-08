# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json
def query_music_info(word):
    baseurl = r'http://s.music.163.com/search/get/?type=1&s='
    qword = urllib2.quote(word)
    url = baseurl + qword + r'&limit=20&offset=0'
    # limit=1的时候 有时候返回无数据
    resp = urllib2.urlopen(url)
    try:
        music = json.loads(resp.read())
        data = music['result']['songs']
        result=[]
        print "共找到如下的歌手演唱:"
        for i in data:
            for j in i['artists']:
                author = j['name']
                print author
            result.append(str(i['id']) + "---" + i['name'] + "---" + author)
        input_author= raw_input("Enter your singer_name: ")
        for i in result:
            if str(i).split("---")[2] == input_author:
                return i
        #print result[0]
        # return result[0]
    except:
        print "查无结果"
from selenium import webdriver
import subprocess
import time
p = None
def get_wailianurl(song_id):
    #得到歌曲id
    wailian_url="http://music.163.com/api/song/detail/?id="+song_id+"&ids=["+song_id+"]&csrf_token="
    data=urllib2.urlopen(wailian_url).read()
    result=json.loads(data)
    for i in result['songs']:
        # print "外链地址为："+i['mp3Url']
        return i['mp3Url'],i['hMusic']['playTime']
def play(filename):
    global p
    stop()
    p = subprocess.Popen(["mpg123", filename]) #mpg123

def stop():
    global p
    if p:
        p.terminate()
        p = None

if __name__ == '__main__':
    song_name = raw_input("Enter your song_name: ")
    try:
        info = query_music_info(song_name)
        if info:
            # print info
            link_url=get_wailianurl(info.split("---")[0])
            # driver = webdriver.Firefox()
            # driver.get(link_url[0])
            #apt - get install mpg123
            play(link_url[0])
            time.sleep(200)
            operate = raw_input("Enter your operate: 2 stop ")
            if operate == "2":
                print "××××××× stop ××××××××"
                stop()
            else:
                time.sleep(link_url[1] / 1000 + 20)
                stop()
            # time.sleep(link_url[1]/1000+20)
            # driver.quit()
            # urllib2.urlopen(link_url)
    except:
        print "查无结果"