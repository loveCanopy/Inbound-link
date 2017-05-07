# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json
def query_music_info(word):
    baseurl = r'http://s.music.163.com/search/get/?type=1&s='
    qword = urllib2.quote(word)
    url = baseurl + qword + r'&limit=1&offset=0'
    resp = urllib2.urlopen(url)
    try:
        music = json.loads(resp.read())
        data = music['result']['songs']
        for i in data:
            for j in i['artists']:
                author = j['name']
            result=str(i['id']) + "---" + i['name'] + "---" + author
        return result
    except:
        print "查无结果"

def get_wailianurl(song_id):
    #得到歌曲id
    wailian_url="http://music.163.com/api/song/detail/?id="+song_id+"&ids=["+song_id+"]&csrf_token="
    data=urllib2.urlopen(wailian_url).read()
    result=json.loads(data)
    for i in result['songs']:
        print "外链地址为："+i['mp3Url']
if __name__ == '__main__':
    song_name = raw_input("Enter your song_name: ");
    try:
        info = query_music_info(song_name)
        if info:
            print info
            get_wailianurl(info.split("---")[0])
    except:
        print "查无结果"