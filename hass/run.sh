#mount s3 here
echo ${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY} >  ${HOME}/.passwd-s3fs

s3fs $S3_PATH /config 
/bin/entry.sh python3 -m homeassistant --config /config