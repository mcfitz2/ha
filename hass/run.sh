#mount s3 here

yas3fs s3://$S3_PATH /config -f
/bin/entry.sh python3 -m homeassistant --config /config