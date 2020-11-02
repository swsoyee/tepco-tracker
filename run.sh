# put current date as yyyy-mm-dd in $date and $date_filename
date=$(date '+%Y-%m-%d')
date_filename=$(date '+%Y%m%d')

pip3 install setuptools
pip3 install pydrive
pip3 install requests

python3 tepco-watt-stats.py $date -u $USER -p $PASSWORD > $date_filename.csv

echo client_config:'\n  'client_id: $CLIENT_ID'\n  'client_secret: $CLIENT_SECRET >> settings.yaml
python3 google-drive-downloader.py -i $RESULT_FOLDER_ID
# sed 's/\"//g' $date_filename.csv | awk 'NF' | cut -f5- -d, | sed '1d' >> tepco-hourly.csv
