# Tool Name :- IP-Tracer
# Author :- Rajkumar Dusad
# Date :- 5/8/2018

if [ -e  /usr/lib/sudo ];then
  if [ ! -e /usr/bin/php ];then
     sudo apt-get update
     sudo apt-get upgrade -y
     sudo apt-get install php -y
     sudo apt-get install php5 -y
   fi
else
  if [ -d /usr/bin ];then
    if [ ! -e /usr/bin/php ];then
     apt-get update
     apt -get upgrade -y
     apt-get install php -y
     apt-get install php5 -y
    fi
  fi
fi
if [ ! -d /usr/bin ];then
  if [ ! -e /data/data/com.termux/files/usr/bin/php ];then
    pkg update
    pkg upgrade -y
    pkg install php -y
    pkg install php5 -y
  fi
fi
php .setup.php
exit
