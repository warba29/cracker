import sys, os, subprocess, platform, struct

if sys.version_info.major != 3:
  exit('\x1b[1;94m   /\x1b[1;91m_!_\x1b[1;94m\ \x1b[1;93msilahkan menggunakan python 3 ')

if struct.calcsize("P")*8==64:
  Exe = "running"

if struct.calcsize("P")*8==32:
  Exe = "running32"

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
  os.system('pkg install play-audio -y &> /dev/null')

while True :
  try :
    import pwinput, requests, bs4, beautifultable, termcolor
  except ImportError as e:
    os.system('python -m pip install '+e.name)
  else:
    break

os.system(f'chmod 777 {Exe} && ./{Exe}')
