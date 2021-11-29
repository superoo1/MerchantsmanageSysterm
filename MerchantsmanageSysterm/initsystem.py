import subprocess
import sys

bind = "127.0.0.1:8080"
WORKERS = 4
log_format = '%(h)s %(t)s "%(r)s" %(s)s %(b)s '

def start_gunicorn():
    cmd = [
        'gunicorn', 'MerchantsmanageSysterm.wsgi',
        '-b', bind,
        '-w', str(WORKERS),
        '--access-logformat', log_format,

    ]
    p = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr)
    return p

def start_nginx():

    cmd2 = "'cp ./business.conf'  '/etc/nginx/sites-enabled/business.conf'"
    cmd1 = "'nginx -s reload'"
    cmd = cmd1 +"&&"+cmd2
    p = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr,shell=True)
    return p




if __name__ == '__main__':

    start_gunicorn()
    start_nginx()







