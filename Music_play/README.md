为了实现linux播放mp3 这里使用mpg123
apt - get install mpg123
```
def play(filename):
    global p
    stop()
    p = subprocess.Popen(["mpg123", filename]) #mpg123

def stop():
    global p
    if p:
        p.terminate()
        p = None

```
filename可以直接为url

