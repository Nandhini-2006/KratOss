import subprocess


def get_git_commits(repository_path: str, limit: int = 20):

    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                repository_path,
                "log",
                f"-{limit}",
                "--pretty=format:%H|%an|%ad|%s",
                "--date=iso"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        commits = []

        for line in result.stdout.splitlines():

            parts = line.split("|", 3)

            if len(parts) != 4:
                continue

            commit_hash, author, date, message = parts

            commits.append({
                "commit_hash": commit_hash,
                "author": author,
                "date": date,
                "message": message
            })

        return commits

    except subprocess.CalledProcessError:

        return []