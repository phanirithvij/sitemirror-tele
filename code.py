import os
from pathlib import Path


def read_dir(path: Path):
    ret = []
    if not path.exists():
        return
    for root, _, files in os.walk(path):
        for file in files:
            parent = Path(root, file).parent
            ret.append(parent/file)
    return ret

if __name__ == '__main__':
    storage = Path("/root/")
    db_path = Path("~/data.db")
    print(read_dir(storage))
