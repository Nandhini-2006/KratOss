import os
import shutil


def create_directory(
    path: str
):

    os.makedirs(
        path,
        exist_ok=True
    )


def delete_directory(
    path: str
):

    if os.path.exists(path):

        shutil.rmtree(path)


def file_exists(
    path: str
) -> bool:

    return os.path.isfile(
        path
    )


def directory_exists(
    path: str
) -> bool:

    return os.path.isdir(
        path
    )