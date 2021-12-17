import os

def toPath(rel_path: str) -> str:
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, rel_path)
    