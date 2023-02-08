from fabric.api import *

env.hosts = ['docker.me']

@task
def all():
    local("echo 'make image'")
    local("echo 'upload image'")
    run("echo 'reload image'")


from fabric.api import *

env.run = local
env.hosts = ["docker.me"] # change this!

@task
def remote():
    env.run = run

@task
def build_file():
    env.run("echo 'make image'")
    env.run("echo 'upload image'")

@task
def deploy_file():
    env.run("echo 'reload image'")

@task
def do_all():
    build_file()
    remote()
    deploy_file()




#Source: https://stackoverflow.com/questions/33273142


