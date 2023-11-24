import os
import shutil
import ctypes
import winshell


def delete_files(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error deleting {file_path}. Reason: {e}')


# 1. Delete temporary files
temp_path = os.getenv('TEMP')
delete_files(temp_path)

# 2. Delete files from the download folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
delete_files(downloads_path)

# 3. Delete files from the recycle bin


def empty_recycle_bin():
    # Empty the recycle bin
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

    print("The recycle bin has been emptied.")


if __name__ == "__main__":
    empty_recycle_bin()
