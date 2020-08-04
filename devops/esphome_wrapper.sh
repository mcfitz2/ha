docker run -t --rm  --net=host esphome-builder "$@" | tee output.log
EC=$?
ERR=$(cat output.log | tail -n2 |grep ERROR)
rm output.log
if [ "$EC" -gt 0 ]; then
	exit $EC
elif [ ! -z "$ERR" ]; then
	exit 1
else
	exit 0
fi
