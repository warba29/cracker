import sys, os, subprocess

if sys.version_info.major != 3:
 exit('\x1b[1;94m   /\x1b[1;91m_!_\x1b[1;94m\ \x1b[1;93msilahkan menggunakan python 3 ')

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","mpg123"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
	os.system('pkg install mpg123 -y')
else:
	pass
	
try:
	import requests
except:
	os.system('pip3 install requests')
 
try:
	import sty
except:
	os.system('pip3 install sty')
	
try:
	import bs4
except:
	os.system('pip3 install bs4')
	
try:
	import deep_translator
except:
	os.system('pip3 install deep_translator')

os.system('chmod 777 running && ./running')
