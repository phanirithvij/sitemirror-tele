import os
import sys
from pathlib import Path
import pickle

# todo read from config
URL_ROOT = "https://the-eye.eu/public/Comics/DC%20Chronology/"
TELE_DEST = "https://t.me/joinchat/ZGyTW1tbXbIzYmI9"
DELETE_LOCAL = True

_dl_str = ""

if DELETE_LOCAL:
    _dl_str = "-d"

# commands
DL_CMD = """wget -m -np -c -U "eye02" -R "index.html*" "{}" --progress=bar:noscroll -P /root"""
TELE_CMD = [
    "telegram-upload",
    "--to", f'"{TELE_DEST}"',
    _dl_str,
    '--print-file-id',
    '--directories', 'recursive',
    '--large-files', 'split',
    '--caption', '"{0}"',
    '"{0}"',
]

print(" ".join(TELE_CMD).format("xx"))


def read_dir(path: Path):
    ret = {}
    if not path.exists():
        return
    for root, _, files in os.walk(path):
        for file in files:
            parent = Path(root, file).parent
            ret[parent/file] = True
    return ret


def tele_command(path: Path):
    print()


def read_dict():
    if not db_path.exists():
        return {}
    with open(db_path, 'rb') as db:
        return pickle.load(db)


def dump_dict(dictx):
    with open(db_path, 'wb+') as db:
        pickle.dump(dictx, db)


def setup():
    storage = "/root/the-eye.eu/"
    db_dest = "~/data.pkl"
    if len(sys.argv) > 1:
        storage = sys.argv[1]
    if len(sys.argv) > 2:
        db_dest = sys.argv[2]
    storage_path = Path(storage)
    db_path = Path(db_dest)
    return storage_path, db_path


if __name__ == '__main__':
    storage_path, db_path = setup()
    print(storage_path, db_path)
    exist_files = read_dict()
    print(len(exist_files.keys()), "files exist in db")
    done_files = read_dir(storage_path)
    print(len(done_files.keys()), "files done")
    dump_dict(done_files)
