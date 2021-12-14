import sys, os, subprocess, platform, struct

if sys.version_info.major != 3:
 exit('\x1b[1;94m   /\x1b[1;91m_!_\x1b[1;94m\ \x1b[1;93msilahkan menggunakan python 3 ')

if not struct.calcsize("P")*8==64:
	exit('(¡) script tidak bisa digunakan di perangkat anda')

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
	os.system('pkg install play-audio -y &> /dev/null')
	
try:
	import requests, bs4, sty
except ImportError as e:
	os.system('pip install '+e.name)
	
os.system('chmod 777 running && ./running')
