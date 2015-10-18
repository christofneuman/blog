#coding: utf-8

from fabric.colors import yellow
from fabric.api import env, run, sudo, local, put


# Settings
env.hosts = ['159.203.243.25']
env.user = 'christof'
env.forward_agent = True

project = 'kylliki'


def deploy():
    print(yellow('Pull in changes from Github'))
    run('cd /srv/%s/app/ && git pull' % project)
    pip()
    migrate()
    print(yellow('Collectstatic'))
    run('cd /srv/%s/app/ && . /srv/%s/env/bin/activate && python manage.py collectstatic' % (project, project))
    #messages()
    restart()

def pip():
    print(yellow('PIP install requirements'))
    run('source /srv/%s/env/bin/activate && pip install -r /srv/%s/app/requirements.txt --upgrade' % (project, project))

def migrate():
    print(yellow('Run migrations'))
    run('cd /srv/%s/app/ && source /srv/%s/env/bin/activate && python manage.py migrate' % (project, project))

def messages():
    print(yellow('Compilemessages'))
    run('cd /srv/%s/app/%s && source /srv/%s/env/bin/activate && django-admin.py compilemessages -l et' % (project, project, project))

def restart():
    print(yellow('Restart uWSGI'))
    sudo('restart %s' % project)
