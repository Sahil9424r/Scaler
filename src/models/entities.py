from dataclasses import dataclass

@dataclass
class TaskEntry:
    tid: str
    pid: str
    title: str
    status: str