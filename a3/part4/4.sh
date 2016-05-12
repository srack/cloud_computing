hadoop fs -rm -r /users/srack/outlinks_output
echo ''
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input /public/www/* \
	-output /users/srack/outlinks_output \
	-mapper out_m0.py \
	-file out_m0.py \
	-reducer out_r0.py \
	-file out_r0.py
