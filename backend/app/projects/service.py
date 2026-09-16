from .models import ProjectCreate, ProjectUpdate

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

def update_project(project_id: int, update_data: ProjectUpdate):

    for project in projects:
        if project["id"] == project_id:
            if update_data.name is not None:
                project["name"] = update_data.name
            if update_data.repo_url is not None:
                project["repo_url"] = str(update_data.repo_url)
            if update_data.status is not None:
                project["status"] = update_data.status
            return project

    return None

def delete_project(project_id: int):

    for project in projects:

        if project["id"] == project_id:
            projects.remove(project)
            return True

    return False