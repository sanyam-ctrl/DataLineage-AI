def analyze_project(project_name: str):

    return {
        "project": project_name,
        "health": "HEALTHY",
        "score": 87,
        "branches": 4,
        "commits": 17,
        "open_prs": 2,
        "dependencies": 24,
        "environment": "development",
        "recommendation": (
            "Project is ready for code review."
        )
    }