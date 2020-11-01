# put current date as yyyy-mm-dd in $date and $date_filename
date=$(date '+%Y-%m-%d')
date_filename=$(date '+%Y%m%d')

pip install requests
python3 tepco-watt-stats.py $date -u $USER -p $PASSWORD > $date_filename.csv

cat $date_filename.csv
# sed 's/\"//g' $date_filename.csv | awk 'NF' | cut -f5- -d, | sed '1d' >> tepco-hourly.csv
