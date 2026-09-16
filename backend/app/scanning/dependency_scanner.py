import os


DEPENDENCY_FILES = [
    "requirements.txt",
    "package.json",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
]


def find_dependency_files(repository_path: str):

    found = []

    for root, directories, files in os.walk(repository_path):

        directories[:] = [
            d for d in directories
            if d not in {
                ".git",
                "node_modules",
                "__pycache__",
                ".venv"
            }
        ]

        for filename in files:

            if filename in DEPENDENCY_FILES:

                found.append(
                    os.path.join(root, filename)
                )

    return found