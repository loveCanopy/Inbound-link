需求：
在做公众号的时候，由于音乐盒功能，需要找音乐的外链，但由于之前使用的http://link.hhtjim.com 由于过度消耗资源暂时无法访问，所以想自己实现一个外链工具，目前是网易云,qq音乐，输入歌名，显示外链请求
欢迎大家关注：
![天台球场的小站](qrcode_for_gh_09cc5b092659_430.jpg)
# [网易云](#page1)  [qq音乐](#page2)  [百度音乐](#page3)
# <h2 id="page1">网易云</h2>
## 网易云搜索api
```
URLhttp://s.music.163.com/search/get/
获取方式：GET
参数：
    src: lofter //可为空
    type: 1
    filterDj: true|false //可为空
    s:  //关键词
    limit: 10 //限制返回结果数
    offset: 0 //偏移
    callback:  //为空时返回json，反之返回jsonp callback
```
得到的返回json，以成都为例
```
{"result":{"songCount":4814,"songs":[{"id":436514312,"name":"成都","artists":[{"id":6731,"name":"赵雷","picUrl":null}],"album":{"id":34930257,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/34YW1QtKxJ_3YnX9ZzKhzw==/2946691234868155.jpg"},"audio":"http://m2.music.126.net/4gwWNLUdEZuPCKGUWWu_rw==/18720284975304502.mp3","djProgramId":0,"page":"http://music.163.com/m/song/436514312"},{"id":420397956,"name":"成都","artists":[{"id":12056033,"name":"文文小婧","picUrl":null}],"album":{"id":34777453,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/JIxteWQ_2Q3jlDgQGOLdaA==/18207912556364337.jpg"},"audio":"http://m2.music.126.net/_7mel0hU-aDjU8w_r3jXCw==/1367792477877615.mp3","djProgramId":0,"page":"http://music.163.com/m/song/420397956"},{"id":33920047,"name":"成都","artists":[{"id":1071076,"name":"姜贰拾","picUrl":"http://p1.music.126.net/llMYuh7fd9sJg26Tqz742g==/109951162864213798.jpg?param=25x25x1"}],"album":{"id":3265394,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/wfg2IRJcnYWGkVxSXfYwNg==/16624615812602486.jpg"},"audio":"http://m2.music.126.net/1_vmDe1qe4oYrSMjPZAv3Q==/1384285143075914.mp3","djProgramId":0,"page":"http://music.163.com/m/song/33920047"},{"id":416892377,"name":"成都","artists":[{"id":12026284,"name":"王大呵","picUrl":null}],"album":{"id":34729621,"name":"成都带不走的只有你","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/qoZHd05FpVfHNtZt8UX5Xg==/18254092044680341.jpg"},"audio":"http://m2.music.126.net/btf5bPkGwMInbi2LP-3b1Q==/3412884100254418.mp3","djProgramId":0,"page":"http://music.163.com/m/song/416892377"},{"id":468513323,"name":"成都","artists":[{"id":11988018,"name":"兴子","picUrl":null}],"album":{"id":35313352,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/pm5yMY9KL_kYIiS-nYNNcQ==/18729081069395536.jpg"},"audio":"http://m2.music.126.net/472dz4ZSBmuDw6_wH3nfew==/19045740416388129.mp3","djProgramId":0,"page":"http://music.163.com/m/song/468513323"},{"id":413188398,"name":"成都","artists":[{"id":12037090,"name":"噪音回收站","picUrl":null}],"album":{"id":34694567,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/mjGx6ZVKQcqmELf3G4B-eg==/17985811207281202.jpg"},"audio":"http://m2.music.126.net/wy7RTl959b1CIQnM15JQ6w==/17985811207281196.mp3","djProgramId":0,"page":"http://music.163.com/m/song/413188398"},{"id":415086115,"name":"成都","artists":[{"id":12055017,"name":"郑熏","picUrl":null}],"album":{"id":34723057,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/nOqqhoOtJc5FsmOW5qkL1Q==/17929736114347990.jpg"},"audio":"http://m2.music.126.net/5kmlfhpTsTOgd7GX75pogw==/18520173858862102.mp3","djProgramId":0,"page":"http://music.163.com/m/song/415086115"},{"id":420401479,"name":"成都","artists":[{"id":12039087,"name":"鹏鹏","picUrl":null}],"album":{"id":34779223,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/iIsspV1MP_ijKWp9iqzBcg==/17686744044708424.jpg"},"audio":"http://m2.music.126.net/Uz_-9g2Lc8jHh1VSc0A8GA==/2946691191763483.mp3","djProgramId":0,"page":"http://music.163.com/m/song/420401479"},{"id":447835691,"name":"成都","artists":[{"id":0,"name":"大Poon／iter","picUrl":null}],"album":{"id":35061557,"name":"成都","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/XT6Cr72e0YvsVpHamVCkww==/109951162825397217.jpg"},"audio":"http://m2.music.126.net/7WVEsmrBKzvEGH6j7PyLbA==/18780758115683479.mp3","djProgramId":0,"page":"http://music.163.com/m/song/447835691"},{"id":443205753,"name":"成都","artists":[{"id":966134,"name":"逗青","picUrl":null}],"album":{"id":35015649,"name":"成都Cover","artist":{"id":0,"name":"","picUrl":null},"picUrl":"http://p1.music.126.net/bWQiFJYQofOModSWHb7RfQ==/109951162814555356.jpg"},"audio":"http://m2.music.126.net/fil7C2B0jVup5QaG6Z8L1w==/18676304511408604.mp3","djProgramId":0,"page":"http://music.163.com/m/song/443205753"}]},"code":200}
```

## 网易云通过id得到外链地址
分享访问的api接口：id为歌曲的id
http://music.163.com/api/song/detail/?id=425137664&ids=[425137664]&csrf_token= 
返回的数据：
```
{"songs":[{"name":"成都","id":436514312,"position":1,"alias":[],"status":0,"fee":0,"copyrightId":36016,"disc":"","no":1,"artists":[{"name":"赵雷","id":6731,"picId":0,"img1v1Id":0,"briefDesc":"","picUrl":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","img1v1Url":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","albumSize":0,"alias":[],"trans":"","musicSize":0}],"album":{"name":"成都","id":34930257,"type":"EP/Single","size":1,"picId":2946691234868155,"blurPicUrl":"http://p1.music.126.net/34YW1QtKxJ_3YnX9ZzKhzw==/2946691234868155.jpg","companyId":0,"pic":2946691234868155,"picUrl":"http://p1.music.126.net/34YW1QtKxJ_3YnX9ZzKhzw==/2946691234868155.jpg","publishTime":1477238400007,"description":"","tags":"","company":"StreetVoice","briefDesc":"","artist":{"name":"","id":0,"picId":0,"img1v1Id":0,"briefDesc":"","picUrl":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","img1v1Url":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","albumSize":0,"alias":[],"trans":"","musicSize":0},"songs":[],"alias":[],"status":0,"copyrightId":36016,"commentThreadId":"R_AL_3_34930257","artists":[{"name":"赵雷","id":6731,"picId":0,"img1v1Id":0,"briefDesc":"","picUrl":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","img1v1Url":"http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg","albumSize":0,"alias":[],"trans":"","musicSize":0}],"subType":"录音室版"},"starred":false,"popularity":100.0,"score":100,"starredNum":0,"duration":328155,"playedNum":0,"dayPlays":0,"hearTime":0,"ringtone":null,"crbt":null,"audition":null,"copyFrom":"","commentThreadId":"R_SO_4_436514312","rtUrl":null,"ftype":0,"rtUrls":[],"copyright":2,"rtype":0,"rurl":null,"hMusic":{"name":null,"id":1245174539,"size":13139636,"extension":"mp3","sr":44100,"dfsId":18632324045084368,"bitrate":320000,"playTime":328155,"volumeDelta":-1.94,"dfsId_str":"18632324045084368"},"mMusic":{"name":null,"id":1245174540,"size":6569841,"extension":"mp3","sr":44100,"dfsId":18720284975304502,"bitrate":160000,"playTime":328155,"volumeDelta":-1.49,"dfsId_str":"18720284975304502"},"lMusic":{"name":null,"id":1245174541,"size":3941922,"extension":"mp3","sr":44100,"dfsId":18665309393829604,"bitrate":96000,"playTime":328155,"volumeDelta":-1.51,"dfsId_str":"18665309393829604"},"bMusic":{"name":null,"id":1245174541,"size":3941922,"extension":"mp3","sr":44100,"dfsId":18665309393829604,"bitrate":96000,"playTime":328155,"volumeDelta":-1.51,"dfsId_str":"18665309393829604"},"mvid":0,"mp3Url":"http://m2.music.126.net/7o5D4dA6271VktgawcbZFA==/18665309393829604.mp3"}],"equalizers":{},"code":200}
```
其中json字段mp3url的值就是外链地址
http://m2.music.126.net/7o5D4dA6271VktgawcbZFA==/18665309393829604.mp3

# <h2 id="page2">QQ音乐</h2>
## QQ搜索API
```
http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0&n={2}&aggr=1&cr=1&loginUin={3}
&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json&needNewCode=0&
p={1}&catZhida=0&remoteplace=sizer.newclient.next_song&w={0}
{0}=需要搜索的歌曲或歌手
{1}=查询的页码数
{2}=当前页的返回数量
{3}=默认为0,是登录的QQ号ID
```
示例：
搜索歌名成都，只返回第一行 默认你第一行为搜索匹配度最高的一行
```
{"code":0,"data":{"keyword":"","priority":0,"qc":[],"semantic":{"curnum":0,"curpage":1,"list":[],"totalnum":0},"song":{"curnum":2,"curpage":1,"list":[{"albumName_hilight":"无法长大","chinesesinger":0,"docid":"13598769090983139333","f":"108963136|成都|40449|赵雷|1666157|无法长大|2832564|328|6|1|0|13124110|5249759|1411000|0|31539642|32010277|7051417|7511341|0|001bhwUC1gE6ep|001Lr98T0yEWAk|000jE4g74VS43p|0|4009","fiurl":"","fnote":2009,"fsinger":"赵雷","fsinger2":"","fsong":"成都","grp":[{"albumName_hilight":"<span class=\"c_tx_highlight\">成都</span>","chinesesinger":0,"docid":"2416530247501575298","f":"200790315|成都|40449|赵雷|1656856|成都|2829364|328|6|1|0|13137599|5255188|1411000|0|31800452|32270434|7030541|7529931|0|003TLWoN0gQnP5|001Lr98T0yEWAk|003ltiMR4RSrgo|31|0","fiurl":"","fnote":0,"fsinger":"赵雷","fsinger2":"","fsong":"成都","isupload":0,"isweiyun":0,"lyric":"","lyric_hilight":"","mv":"","nt":10000,"only":0,"pubTime":1477238400,"pure":0,"singerMID":"001Lr98T0yEWAk","singerMID2":"","singerName2_hilight":"","singerName_hilight":"赵雷","singerid":40449,"singerid2":0,"songName_hilight":"<span class=\"c_tx_highlight\">成都</span>","t":1,"tag":0,"ver":0}],"isupload":0,"isweiyun":0,"lyric":"","lyric_hilight":"","mv":"","nt":10000,"only":0,"pubTime":1482249600,"pure":0,"singerMID":"001Lr98T0yEWAk","singerMID2":"","singerName2_hilight":"","singerName_hilight":"赵雷","singerid":40449,"singerid2":0,"songName_hilight":"<span class=\"c_tx_highlight\">成都</span>","t":1,"tag":0,"ver":0}],"totalnum":338},"totaltime":5.800000000000000e-05,"zhida":{"chinesesinger":0,"type":0}},"message":"","notice":"","subcode":0,"time":1494158879,"tips":""}
```
分析json格式，歌曲名称，歌手，专辑，还有其中的f的属性
```
"f":"108963136|成都|40449|赵雷|1666157|无法长大|2832564|328|6|1|0|13124110|5249759|1411000|0|31539642|32010277|7051417|7511341|0|001bhwUC1gE6ep|001Lr98T0yEWAk|000jE4g74VS43p|0|4009"
```
```
试听id：108963136
歌名：成都
歌曲id：001bhwUC1gE6ep
歌曲页：https://y.qq.com/n/yqq/song/001bhwUC1gE6ep.html
singerMid：001Lr98T0yEWAk
歌手页：https://y.qq.com/n/yqq/singer/001Lr98T0yEWAk.html#
专辑图片：000jE4g74VS43p
专辑页：https://y.qq.com/n/yqq/album/000jE4g74VS43p.html#
singerid:40449
image_id:1666157
```
## 获取歌曲图片API
### 第一种 通过专辑图片
```
http://imgcache.qq.com/music/photo/mid_album_90/{1}/{2}/{0}.jpg
{0}=上面取到的Img
{1]=上面取到的Img的倒数第二个字符
{2}=上面取到的Img的最后一个字符
```
示例：
http://imgcache.qq.com/music/photo/mid_album_90/3/p/000jE4g74VS43p.jpg
### 第二种 通过专辑图片
```
http://y.gtimg.cn/music/photo_new/T002R300x300M000{0}.jpg?max_age=25920000
{0}=上面取到的Img
```
### 第三种 通过image_id
```
http://imgcache.qq.com/music/photo/album_${width}/${image_id%100}/${width}_albumpic_${image_id}_0.jpg
```
## 获取试听地址
```
http://ws.stream.qqmusic.qq.com/${id}.m4a?fromtag=46
```
## 获取歌词
```
http://music.qq.com/miniportal/static/lyric/{1}/{0}.xml
{0}=上面取到的试听id
{1}=上面取到的试听id%100
```
# <h2 id="page3">百度音乐</h2>
## API
## Music web全接口
```
http://tingapi.ting.baidu.com/v1/restserver/ting
```
## 搜索歌曲
```
http://tingapi.ting.baidu.com/v1/restserver/ting?size=2&_t=1468380543284 
&format=json&method=baidu.ting.search.catalogSug&query=${1}

${1}位置存放关键字
```
返回的数据格式
```
{"song":[{"bitrate_fee":"{\"0\":\"129|-1\",\"1\":\"-1|-1\"}","weight":"5420","songname":"海阔天空","songid":"268425156","has_mv":"0","yyr_artist":"0","resource_type_ext":"0","artistname":"韩红","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":"2107fffd7c409584153f0L"},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"170","songname":"海阔天空","songid":"266907369","has_mv":"0","yyr_artist":"0","resource_type_ext":"0","artistname":"T榜","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":"0307fe8aee90957e78ab8L"},{"bitrate_fee":"{\"0\":\"129|-1\",\"1\":\"-1|-1\"}","weight":"120","songname":"海阔天空","songid":"8877990","has_mv":"0","yyr_artist":"0","resource_type_ext":"0","artistname":"林育群","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":"66068777a6095848d897L"},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"110","songname":"海阔天空","songid":"73896409","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"幼稚园杀手","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"101","songname":"14.海阔天空","songid":"73888949","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"左右乐队","info":"","resource_provider":"1","control":"0100000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"90","songname":"海阔天空-电吉他版","songid":"73984962","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"MC雪殇","info":"","resource_provider":"1","control":"0100000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"40","songname":"海阔天空","songid":"74007550","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"丛浩楠","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"10","songname":"海阔天空","songid":"73996756","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"许苏峰（Bragg.Xu）","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"10","songname":"海阔天空","songid":"74043630","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"Resound_APEinT","info":"","resource_provider":"1","control":"0000000000","encrypted_songid":""},{"bitrate_fee":"{\"0\":\"0|0\",\"1\":\"0|0\"}","weight":"1","songname":"Hubei.萝卜哥《海阔天空》","songid":"74017327","has_mv":"0","yyr_artist":"1","resource_type_ext":"0","artistname":"萝卜","info":"","resource_provider":"1","control":"0100000000","encrypted_songid":""}],"error_code":22000,"order":"song"}

```
## LRC歌词
```
method=baidu.ting.song.lry {songid: id}
示例：
http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.lry&songid=274841326
``` 
## 图片地址
通过songid找到ting_uid
```
http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&songid=274841326
```
返回数据
```
{"songinfo":{"special_type":0,"pic_huge":"http:\/\/musicdata.baidu.com\/data2\/pic\/cd8dcc4f40cbb37c7dcf0e6c151fbcc6\/522916493\/522916493.jpg@s_0,w_1000","resource_type":"0","pic_premium":"http:\/\/musicdata.baidu.com\/data2\/pic\/cd8dcc4f40cbb37c7dcf0e6c151fbcc6\/522916493\/522916493.jpg@s_0,w_500","havehigh":2,"author":"赵雷","toneid":"0","has_mv":0,"song_id":"274841326","piao_id":"0","artist_id":"13874366","lrclink":"http:\/\/musicdata.baidu.com\/data2\/lrc\/cc971cffe87677aa8986f0f056d20df0\/540728422\/540728422.lrc","relate_status":"0","learn":0,"pic_big":"http:\/\/musicdata.baidu.com\/data2\/pic\/cd8dcc4f40cbb37c7dcf0e6c151fbcc6\/522916493\/522916493.jpg@s_0,w_150","play_type":0,"album_id":"275347355","album_title":"无法长大","bitrate_fee":"{\"0\":\"129|-1\",\"1\":\"-1|-1\"}","song_source":"web","all_artist_id":"13874366","all_artist_ting_uid":"90654808","all_rate":"64,128,256,320,flac","charge":0,"copy_type":"0","is_first_publish":0,"korean_bb_song":"0","pic_radio":"http:\/\/musicdata.baidu.com\/data2\/pic\/cd8dcc4f40cbb37c7dcf0e6c151fbcc6\/522916493\/522916493.jpg@s_0,w_300","has_mv_mobile":0,"title":"成都","pic_small":"http:\/\/musicdata.baidu.com\/data2\/pic\/cd8dcc4f40cbb37c7dcf0e6c151fbcc6\/522916493\/522916493.jpg@s_0,w_90","album_no":"6","resource_type_ext":"0","ting_uid":"90654808"},"error_code":22000,"bitrate":{"show_link":"http:\/\/zhangmenshiting.baidu.com\/data2\/music\/239908cd71a27d737fef95b17d18b97c\/540728460\/540728460.mp3?xcode=824826331591c01cd1fcd5f6c50b1ab0","free":0,"song_file_id":540728460,"file_size":2619789,"file_extension":"mp3","file_duration":327,"file_bitrate":64,"file_link":"http:\/\/yinyueshiting.baidu.com\/data2\/music\/239908cd71a27d737fef95b17d18b97c\/540728460\/540728460.mp3?xcode=824826331591c01cd1fcd5f6c50b1ab0","hash":"8914235b7268b28cd2bc5af56c4acfd73eb55358"}}

图片地址                                      
pic_url=song_info['songinfo']['pic_big']    
专辑id                                      
ting_uid=song_info['songinfo']['ting_uid']  
专辑名                                       
album_title=song_info['songinfo']['album_title']
歌曲名                                       
title=song_info['songinfo']['title']        
试听地址                                      
show_url=song_info['bitrate']['show_link']  

```
## 获取ting_uid中的歌曲
```
http://tingapi.ting.baidu.com/v1/restserver/ting?" \                        
method=baidu.ting.artist.getSongList&tinguid=90654808&limits=6&use_cluster=1
```
## 获取歌手信息
```
http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.artist.getInfo&tinguid=90654808
```

## 获取榜单数据
```
bang_url="http://tingapi.ting.baidu.com/v1/restserver/ting?size=20&type=2
         "&_t=1468380543284&format=json&method=baidu.ting.billboard.billList
type: //1、新歌榜，2、热歌榜，                           
11、摇滚榜，12、爵士，16、流行                             
21、欧美金曲榜，22、经典老歌榜，23、情歌对唱榜，24、影视金曲榜，25、网络歌曲榜   
```
