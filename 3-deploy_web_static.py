#!/usr/bin/python3
from fabric.api import put, run, local, env
from time import strftime
from datetime import date
from os import path

env.hosts = ["54.167.24.215", "54.82.159.235"]


def do_pack():
    """ this script generates archive contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None


def do_deploy(archive_path):
    """a fabric script  distributing an
    archive to the web server"""

    if not path.exists(archive_path):
        return False
    try:
        tgzfile = archive_path.split("/")[-1]
        print(tgzfile)
        filename = tgzfile.split(".")[0]
        print(filename)
        pathname = "/data/web_static/releases/" + filename
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgzfile, filename))
        run("rm /tmp/{}".format(tgzfile))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except Exception as e:
        return False


def deploy():
    """running these functions"""

    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
