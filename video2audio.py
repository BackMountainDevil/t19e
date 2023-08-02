""" 
作用：用 ffmpeg 从视频 中批量提取音频，若想提取为mp3，就把m4a换mp3
运行：安装 ffmpeg ，设置路径参数后，用 python3 运行即可
"""
import os

# 文件名称 或 文件夹路径，如果想设置为代码同级路径，可设置为 os.getcwd()
FILE_OR_DIR = "/home/mifen/Videos"
# 文件名后缀，如果上面输入是文件夹，可忽略此参数。注意此参数前面有个点
FILE_FORMAT = ".mp4"

# 设置输出结果是否保存在输入文件相同目录，False则保存在代码相同目录
SAVE_IN_SAME_DIR = False
OUTPUT_FORMAT = "m4a"  # 输出音频的文件格式

if os.path.isdir(FILE_OR_DIR):
    for dirpath, dirnames, filenames in os.walk(FILE_OR_DIR):
        for filename in filenames:
            try:
                print("debug", filename)
                # 校验文件名后缀，避免输入无关文件
                if os.path.splitext(filename)[-1] == FILE_FORMAT:
                    file_full_path = os.path.join(FILE_OR_DIR, filename)
                    output_path = os.path.join(FILE_OR_DIR, filename[:-4])
                    if not SAVE_IN_SAME_DIR:
                        output_path = os.path.join(os.getcwd(), filename[:-4])
                    cmd = 'ffmpeg -i "{}" -vn "{}.{}"'.format(
                        file_full_path, output_path, OUTPUT_FORMAT
                    )
                    os.system(cmd)
                else:
                    print(
                        "Error: The file %s is not %s, it's %s"
                        % (filename, FILE_FORMAT, os.path.splitext(filename)[-1])
                    )
            except Exception as e:
                print("Exception: ", e, ". Filename: ", filename)
elif os.path.isfile(FILE_OR_DIR):
    # 单文件 不校验文件名称后缀
    try:
        output_path = FILE_OR_DIR[:-4]
        if not SAVE_IN_SAME_DIR:
            output_path = os.path.join(os.getcwd(), os.path.basename(FILE_OR_DIR))
        cmd = 'ffmpeg -i "{}" -vn "{}.{}"'.format(
            FILE_OR_DIR, output_path, OUTPUT_FORMAT
        )
        os.system(cmd)
    except Exception as e:
        print("Exception: ", e, ". Filename: ", filename)
