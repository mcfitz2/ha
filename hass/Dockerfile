FROM homeassistant/home-assistant

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3 python && \
    pip3 install --no-cache --upgrade pip setuptools wheel

RUN pip install yas3fs \
 	&& sed -i'' 's/^# *user_allow_other/user_allow_other/' /etc/fuse.conf \
 	&& chmod a+r /etc/fuse.conf

ADD run.sh /
CMD ["/run.sh"]