import os


def rename_files(dir_path, log_file="rename.log"):
    """重命名文件名称 记录在日志中"""
    files = os.listdir(dir_path)
    file_count = len(files)

    with open(log_file, "a") as log:
        for i, file in enumerate(files):
            old_file_path = os.path.join(dir_path, file)
            new_file_path = os.path.join(dir_path, f"{i}")
            os.rename(old_file_path, new_file_path)
            log.write(f"{old_file_path} </|\> {new_file_path}\n")

    print(f"Total files: {file_count}")
    print(f"Rename log saved to {log_file}")


def rename_files_back(dir_path, log_file="rename.log"):
    """从日志中恢复文件名称"""
    with open(log_file, "r") as log:
        lines = log.readlines()

    for line in lines:
        old_file_path, new_file_path = line.strip().split(" </|\> ")
        new_file_path = os.path.join(dir_path, new_file_path)
        os.rename(new_file_path, old_file_path)
        print(f"Renamed {new_file_path} back to {old_file_path}")


if __name__ == "__main__":
    dir_path = "/home/mifen/Documents/LCEDA-Pro/"
    rename_files(dir_path)
    # rename_files_back(dir_path)
