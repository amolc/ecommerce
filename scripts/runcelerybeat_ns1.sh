
mydir=$(dirname $0)
ps -ef | grep "celery -A restserver worker" | grep -v runcelery | awk '{print $2}' | xargs kill -9

repodir=$(dirname $mydir)
echo $repodir
conffile=/home/ubuntu/quantengine/scripts/configs/quantengine.sh
source /home/ubuntu/quantengine/scripts/configs/quantengine.sh
cd /home/ubuntu/quantengine/restserver
source /home/ubuntu/quantengine/venv/bin/activate
celery -A restserver beat --loglevel=debug
#checking if only warning can work

