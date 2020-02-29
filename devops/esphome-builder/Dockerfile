FROM esphome/esphome:latest
RUN pip3 install awscli awscli-plugin-endpoint
RUN mkdir /root/.aws
ADD aws-config /root/.aws/config
ADD *.yaml /config/
RUN aws s3 cp s3://$S3_BUCKET_NAME/esphome-secrets.yaml /config/secrets.yaml
