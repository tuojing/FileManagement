import argparse

parser = argparse.ArgumentParser()
parser.add_argument('src', help='來源檔案路徑')
parser.add_argument('dest', help='目標檔案路徑')

args = parser.parse_args()
print('來源路徑:', args.src)
print('目標路徑:', args.dest)
