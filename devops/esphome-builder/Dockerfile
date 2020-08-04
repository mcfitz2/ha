FROM esphome/esphome:latest
ADD *.yaml /config/
ADD wrapper.sh /bin/wrapper.sh
RUN chmod +x /bin/wrapper.sh
ENTRYPOINT ["/bin/wrapper.sh"]

