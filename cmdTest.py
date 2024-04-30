import argparse
from os import path
import sys

parser = argparse.ArgumentParser()  # 建立解析命令的物件
parser.add_argument('src', help='來源檔案路徑')
parser.add_argument('dest', help='目標檔案路徑')

args = parser.parse_args()  # 解析命令參數

if not path.isdir(args.src):
    print('"{}"不是資料夾路徑'.format(args.src))
    sys.exit(2)

if not path.isdir(args.dest):
    print('"{}"不是資料夾路徑'.format(args.dest))
    sys.exit(2)
else:
    print('來源路徑:', args.src)
    print('目標路徑:', args.dest)
print('沒事~我離開了。')
sys.exit()
