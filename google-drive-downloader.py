from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import argparse

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--folderId', help="フォルダーID")
args = parser.parse_args()

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % args.folderId}).GetList()

for drive_file in file_list:
    if drive_file['title'] == 'tepco-hourly.csv':
        file_local = drive.CreateFile({'id': drive_file['id']})
        file_local.GetContentFile('tepco-hourly.csv')
        print('Download `tepco-hourly.csv` to local has been successed.')
        # drive_file.Delete()
        print('Remove `tepco-hourly.csv` in remote.')
        break
