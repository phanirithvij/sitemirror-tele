import os
import sys
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
    storage_path = "/root/the-eye.eu/"
    if len(sys.argv) > 1:
        storage_path = sys.argv[1]
    storage = Path(storage_path)
    db_path = Path("~/data.db")
    print(read_dir(storage))
