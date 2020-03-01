FROM homeassistant/home-assistant

RUN apk --update add fuse alpine-sdk automake autoconf libxml2-dev fuse-dev curl-dev git bash;
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git; \
	 cd s3fs-fuse; \
	 git checkout tags/${S3FS_VERSION}; \
	 ./autogen.sh; \
	 ./configure --prefix=/usr; \
	 make; \
	 make install; \
	 rm -rf /var/cache/apk/*;
 
ADD run.sh /
CMD ["/run.sh"]