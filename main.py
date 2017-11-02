import urllib

import platform
import sys

def inject_custom_packets(x,z):
    try:
        import scapy
        from scapy import *
    except ImportError:
        print("cant connect,maybe you are missing a packet.Check your dependencies")        
    #test if packet can be send
    sr1(IP(dst=x)/z)
    
    
def get_current_version():
    current_version = platform.python_version()
    if '2.7' in current_version:
        print("sorry buddy you'll need to get python 3.6 to be able to run it')
              

def inject_custom_cookie():
    try:
        url = urlib.request(raw_input())
        url.add_header('Cookie',raw_input())
        info = urllib.urlopen(url)
    except URLError:
        print("cant connect to the wesite")

def main():
    
