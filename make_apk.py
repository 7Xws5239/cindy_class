import os
import subprocess
import shutil
import time

# 指定Python脚本的路径
python_script_path = 'caculator.py'

# 获取Python脚本的名称和目录
script_dir, script_name = os.path.split(python_script_path)
script_name_without_ext = os.path.splitext(script_name)[0]

# 创建与Python脚本名称相同的目录来保存APK
apk_dir = os.path.join(script_dir, script_name_without_ext)
os.makedirs(apk_dir, exist_ok=True)

# 运行Buildozer命令来生成APK
command = f'cd {script_dir} && buildozer -v android debug'
subprocess.run(command, shell=True)

# 等待APK文件生成
apk_path_src = os.path.join(script_dir, '.buildozer', 'android', 'platform', 'build-armeabi-v7a', 'dists', script_name_without_ext, 'bin', f'{script_name_without_ext}-release-signed.apk')
while not os.path.exists(apk_path_src):
    print(f'Waiting for APK to be generated at {apk_path_src}...')
    time.sleep(10)

# 将生成的APK移动到新的目录
apk_path_dst = os.path.join(apk_dir, f'{script_name_without_ext}.apk')
shutil.move(apk_path_src, apk_path_dst)
