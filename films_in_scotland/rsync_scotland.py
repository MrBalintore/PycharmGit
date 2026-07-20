import os

from films_in_scotland.get_copies import get_rsync_copies


def rsync_scotland():
    print("hello")
    copies = get_rsync_copies()
    for copy in copies:
        src, dst= copy
        command = f"rsync -ah --info=progress2 --size-only {src} {dst}"
        print(f"command is {command}")
        os.system(command)

def main():
    rsync_scotland()


if __name__ == "__main__":
    main()


