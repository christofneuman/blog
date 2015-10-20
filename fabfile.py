# coding: utf-8

from fabric.colors import yellow
from fabric.api import env, run, sudo, local, put


# Settings
env.hosts = ['159.203.243.25']
env.user = 'christof'
env.forward_agent = True

project = 'kylliki'


def deploy():
    print(yellow('Pull in changes from Github'))
    run('cd /srv/{project}/app/ && git pull'.format(project=project))
    pip()
    migrate()
    print(yellow('Collectstatic'))
    run('cd /srv/{project}/app/ && . /srv/{project}/env/bin/activate && python manage.py collectstatic --noinput --settings={project}.settings.production'.format(project=project))
    #messages()
    restart()

def pip():
    print(yellow('PIP install requirements'))
    run('source /srv/{project}/env/bin/activate && pip install -r /srv/{project}/app/requirements.txt --upgrade'.format(project=project))

def migrate():
    print(yellow('Run migrations'))
    run('cd /srv/{project}/app/ && source /srv/{project}/env/bin/activate && python manage.py migrate --settings={project}.settings.production'.format(project=project))

def messages():
    print(yellow('Compilemessages'))
    run('cd /srv/{project}/app/{project} && source /srv/{project}/env/bin/activate && django-admin.py compilemessages -l et --settings={project}.settings.production'.format(project=project))

def restart():
    print(yellow('Restart uWSGI'))
    sudo('restart {project}'.format(project=project))
