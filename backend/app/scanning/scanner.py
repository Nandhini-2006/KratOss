import os
import subprocess
import shutil


def clone_repository(repo_url: str, destination: str):

    if os.path.exists(destination):
        shutil.rmtree(destination)

    subprocess.run(
        ["git", "clone", repo_url, destination],
        check=True
    )

    return destination