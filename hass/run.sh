#mount s3 here
echo ${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY} >  ${HOME}/.passwd-s3fs
mkdir /config-aws
s3fs $S3_PATH /config-aws -o passwd_file=${HOME}/.passwd-s3fs,url=https://s3.fr-par.scw.cloud
/bin/entry.sh python3 -m homeassistant --config /config-aws