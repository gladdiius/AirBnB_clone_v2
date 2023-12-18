#!/usr/bin/python3

from fabric.api import local, env
from datetime import datetime
import os

# Set the environment to use local by default
env.hosts = ['localhost']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
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
