hadoop fs -rm -r /users/srack/inverted_output
echo ''
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input /public/www/* \
	-output /users/srack/inverted_output \
	-mapper inverted_m0.py \
	-file inverted_m0.py \
	-reducer inverted_r0.py \
	-file inverted_r0.py
