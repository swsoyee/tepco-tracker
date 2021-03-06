# put current date as yyyy-mm-dd in $date and $date_filename
date=$(date -d '-1 day' '+%Y-%m-%d')
date_filename=$(date -d '-1 day' '+%Y%m%d')

pip3 install setuptools
pip3 install pydrive
pip3 install requests

python3 tepco-watt-stats.py $date -u $USER -p $PASSWORD > $date_filename.csv

echo $CREDENTIALS >> credentials.json
echo client_config:'\n  'client_id: $CLIENT_ID'\n  'client_secret: $CLIENT_SECRET >> settings.yaml

python3 google-drive-downloader.py -i $RESULT_FOLDER_ID
sed 's/\"//g' $date_filename.csv | awk 'NF' | cut -f5- -d, | sed '1d' >> tepco-hourly.csv
python3 google-driver-uploader.py -i $RESULT_FOLDER_ID -s $SOURCE_FOLDER_ID -d $date_filename
