hadoop fs -rm -r /users/srack/inlinks_output
echo ''
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input /public/www/* \
	-output /users/srack/inlinks_output \
	-mapper in_m0.py \
	-file in_m0.py \
	-reducer in_r0.py \
	-file in_r0.py
