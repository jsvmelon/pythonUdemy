import os
import fnmatch

import generators


def scan(root: str, pattern: str = "*.emp3", full_path: bool = True) -> generators:
    for path, directories, files in os.walk(root):
        for file in fnmatch.filter(files, pattern):
            if full_path:
                yield os.getcwd() + "/" + os.path.join(path, file)
            else:
                yield os.path.join(path, file)


if __name__ == "__main__":
    scanner = scan("/", full_path=False)
    for music_file in scanner:
        print(music_file)
