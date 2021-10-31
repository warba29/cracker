import sys, os, subprocess, platform

if sys.version_info.major != 3:
 exit('\x1b[1;94m   /\x1b[1;91m_!_\x1b[1;94m\ \x1b[1;93msilahkan menggunakan python 3 ')

#if not struct.calcsize("P")*8==64:
	#exit('(¡) script tidak bisa digunakan di perangkat anda')

if not '3.10.0' in platform.python_version():
	exit('(¡) perbarui python anda ke versi 3.10.0')

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","mpg123"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
	os.system('pkg install mpg123 -y &> /dev/null')
	
try:
	import requests
except:
	os.system('pip install requests')
 
try:
	import sty
except:
	os.system('pip install sty')
	
try:
	import bs4
except:
	os.system('pip install bs4')
	
try:
	import deep_translator
except:
	os.system('pip install deep_translator')

os.system('chmod 777 running && ./running')
