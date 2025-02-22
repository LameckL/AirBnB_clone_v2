#!/usr/bin/python3
from fabric.api import put, run, local, env
from os import path


env.hosts = ["54.167.24.215", "54.82.159.235"]


def do_deploy(archive_path):
    """this fabric script distributes an
    archive to the web server"""

    if not path.exists(archive_path):
        return False
    try:
        tgz_file = archive_path.split("/")[-1]
        print(tgz_file)
        filename = tgz_file.split(".")[0]
        print(filename)
        pathname = "/data/web_static/releases/" + filename
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_file, filename))
        run("rm /tmp/{}".format(tgz_file))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except Exception as e:
        return False
