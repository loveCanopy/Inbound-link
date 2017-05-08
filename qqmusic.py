# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json
import random
# 搜索歌曲API：
# http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0&n={2}\
# &aggr=1&cr=1&loginUin={3}&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json\
# &needNewCode=0&p={1}&catZhida=0&remoteplace=sizer.newclient.next_song&w={0}
# {0}=需要搜索的歌曲或歌手
# {1}=查询的页码数
# {2}=当前页的返回数量
# {3}=默认为0,是登录的QQ号ID
song_name = raw_input("Enter your song_name: ")
#将n设为1  默认只返回一条
url="http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0&n=1&aggr=1&cr=1&loginUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json&needNewCode=0" \
    "&p=1&catZhida=0&remoteplace=sizer.newclient.next_song&w="+song_name
# print url
try:
    data=urllib2.urlopen(url).read()
    if data:
        for i in  json.loads(str(data))['data']['song']['list']:
            # print str(i['f']).split("|")[0]+" "+str(i['f']).split("|")[1]
            song_id=str(i['f']).split("|")[0]
            song_name=str(i['f']).split("|")[1]
            qq_wailianurl = "http://ws.stream.qqmusic.qq.com/"+song_id+".m4a?fromtag="+random.randint(1,50)
            # print str(i['f'])
            print song_id,song_name,qq_wailianurl
except:
    print "无外链"