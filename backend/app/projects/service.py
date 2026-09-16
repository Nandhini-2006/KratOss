from .models import ProjectCreate

projects = []

def create_project(project: ProjectCreate):

    new_project = {
        "id": len(projects) + 1,
        "name": project.name,
        "repo_url": str(project.repo_url),
        "status": "Not Scanned"
    }

    projects.append(new_project)

    return new_project

def get_projects():

    return projects


def get_project(project_id: int):

    for project in projects:
        if project["id"] == project_id:
            return project

    return None

def delete_project(project_id: int):

    for project in projects:

        if project["id"] == project_id:
            projects.remove(project)
            return True

    return False