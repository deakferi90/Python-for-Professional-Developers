from dataclasses import dataclass

project_names = ["Payments API", "Developer Portal", "Ops Console"]

slugs = []
for name in project_names:
    slugs.append(name.capitalize().replace(" ", "-"))

print(slugs)

tasks: list[dict[str, str | bool]] = [
    {"title": "ship docs", "done": False},
    {"title": "cut release", "done": True},
    {"title": "announce launch", "done": False},
]

open_titles = [task["title"] for task in tasks if not task["done"]]

print(f"Open titles: {open_titles}")

tasksNotDone = []

for task in tasks:
    if not task["done"]:
        title = task["title"]
        if isinstance(title, str):
            tasksNotDone.append(title.capitalize().replace(" ", "-"))

    print(tasksNotDone)


def validate_project_name(name: str) -> str:
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Project name cannot be empty.")
    return cleaned_name


@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False


if __name__ == "__main__":
    print(slugs)
    print(f"Open titles: {open_titles}")

    try:
        validate_project_name("  ")
    except ValueError as e:
        print(f"Validation error: {e}")

    payments = Project(name="Payments API", slug="payments-api")
    print(payments)
    print(payments.archived)
