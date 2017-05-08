# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json
import random
# 百度music web版全接口
# http://tingapi.ting.baidu.com/v1/restserver/ting

# 搜索歌曲
# http://tingapi.ting.baidu.com/v1/restserver/ting?size=2&_t=1468380543284
# &format=json&method=baidu.ting.search.catalogSug&query=%E6%88%90%E9%83%BD
url="http://tingapi.ting.baidu.com/v1/restserver/ting?size=1&_t=1468380543284&format=json" \
    "&method=baidu.ting.search.catalogSug&query=%E6%88%90%E9%83%BD"
data=urllib2.urlopen(url).read()
song= json.loads(data)['song']
# for i in song:
#     print i['artistname'],i['songid'],i['songname']

# //LRC歌词
# baidu.ting.song.lry {songid: id}
# lrcurl="http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.lry&songid=274841326"
# print urllib2.urlopen(lrcurl).read().decode("unicode-escape")

# 通过songid 找到ting_uid 和试听地址 ，图片地址
play_url="http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&songid=274841326"
songinfo=urllib2.urlopen(play_url).read()
song_info=json.loads(songinfo)
# 图片地址
pic_url=song_info['songinfo']['pic_big']
# 专辑id
ting_uid=song_info['songinfo']['ting_uid']
# 专辑名
album_title=song_info['songinfo']['album_title']
# 歌曲名
title=song_info['songinfo']['title']
# print  pic_url,ting_uid,album_title ,title
# 试听地址
show_url=song_info['bitrate']['show_link']
print    show_url
# 歌单中的歌曲
songlist_url="http://tingapi.ting.baidu.com/v1/restserver/ting?" \
             "method=baidu.ting.artist.getSongList&tinguid=90654808&limits=6&use_cluster=1"
songlist= urllib2.urlopen(songlist_url).read()
song_list=json.loads(songlist)
# for i in  song_list['songlist']:
#     print i['author'],i['song_id'],i['title']
#
# 获取歌手信息
# baidu.ting.artist.getInfo { tinguid: id }
# tinguid: //歌手ting id
author_url="http://tingapi.ting.baidu.com/v1/restserver/ting?" \
"method=baidu.ting.artist.getInfo&tinguid=90654808"
author_info=json.loads( urllib2.urlopen(author_url).read())
# print author_info['name'],author_info['intro']

# 获取榜单数据
bang_url="http://tingapi.ting.baidu.com/v1/restserver/ting?size=20&type=2" \
         "&_t=1468380543284&format=json&method=baidu.ting.billboard.billList "
# type: //1、新歌榜，2、热歌榜，
# 11、摇滚榜，12、爵士，16、流行
# 21、欧美金曲榜，22、经典老歌榜，23、情歌对唱榜，24、影视金曲榜，25、网络歌曲榜