
#later wil be update 
import urllib

def 

def inject_custom_cookie():
    try:
        url = urlib.request(raw_input())
        url.add_header('Cookie',raw_input())
        info = urllib.urlopen(url)
    except URLError:
        print("cant connect to the wesite")
