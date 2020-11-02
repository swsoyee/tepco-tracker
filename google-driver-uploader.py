from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import argparse

print('Begin authentication')
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--folderId', help="フォルダーID")
parser.add_argument('-s', '--sourceFolderId', help="ソースデータを保存するフォルダーID")
parser.add_argument('-d', '--date', help="日付")
args = parser.parse_args()

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % args.folderId}).GetList()

for drive_file in file_list:
    if drive_file['title'] == 'tepco-hourly.csv':
        file_local = drive.CreateFile({'id': drive_file['id']})
        file_local.SetContentFile('tepco-hourly.csv')
        file_local.Upload()
        print('Upload new `tepco-hourly.csv` to drive has been successed.')
        break

tepco_source_file = drive.CreateFile({"mimeType": "text/csv", "parents": [{"id": args.sourceFolderId}]})
tepco_source_file.SetContentFile(args.date + ".csv")
tepco_source_file.Upload() # Upload the file.
print('Created file %s with mimeType %s' % (tepco_source_file['title'], tepco_source_file['mimeType'])) 
