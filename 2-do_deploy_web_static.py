#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to web servers
"""

from fabric.api import local, env, put, run
from os.path import exists, basename
from datetime import datetime

# Set the environment to use both web servers
env.hosts = ['54.237.115.5', '54.242.190.120']


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
        filename = basename(archive_path)[:-4]

        # Uncompress the archive to /data/web_static/releases/<filename> on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            basename(archive_path), filename))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(basename(archive_path)))

        # Move files to the correct location
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
            filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))

        # Delete the symbolic link /data/web_static/current
        run("rm -f /data/web_static/current")

        # Create a new symbolic link /data/web_static/current linked to the new version
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename))

        return True
    except Exception as e:
        return False
