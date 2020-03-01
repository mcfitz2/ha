FROM homeassistant/home-assistant

RUN apk add automake git autotools-dev fuse g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config \
	&& git clone https://github.com/s3fs-fuse/s3fs-fuse.git \
	&& cd s3fs-fuse \
	&& ./autogen.sh \
	&& ./configure \
	&& make \
&& make install 
ADD run.sh /
CMD ["/run.sh"]