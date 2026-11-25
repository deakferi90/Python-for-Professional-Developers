from dataclasses import dataclass


@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False
