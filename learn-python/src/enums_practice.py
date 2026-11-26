from enum import StrEnum, auto


class TaskStatus(StrEnum):
    PENDING = auto()
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
