#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to web servers
"""

from fabric.api import local, env, put, run
from os.path import exists
from datetime import datetime

# Set the environment to use both web servers
env.hosts = ['54.242.190.120', '54.237.115.5']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive path
        time_format = "%Y%m%d%H%M%S"
        archive_name = "web_static_{}.tgz".format(
            datetime.utcnow().strftime(time_format))
        archive_path = "versions/{}".format(archive_name)

        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Get the filename without extension
        filename = archive_path.split('/')[-1].split('.')[0]

        # Uncompress the archive to /data/web_static/releases/<filename> on the web server
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_path.split('/')[-1], filename))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_path.split('/')[-1]))

        # Delete the symbolic link /data/web_static/current
        run("rm -f /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename))

        return True
    except Exception as e:
        return False
