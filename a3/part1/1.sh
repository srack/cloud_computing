hadoop fs -rm -r /users/srack/wordcount_output
hadoop fs -rm -r /users/srack/tmp
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input /public/www/* \
	-output /users/srack/tmp \
	-mapper wordcount_m0.py \
	-file wordcount_m0.py \
	-reducer wordcount_r0.py \
	-file wordcount_r0.py 
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.text.key.comparator.options=-nr \
	-input /users/srack/tmp/part-00000 \
	-output /users/srack/wordcount_output \
	-mapper wordcount_m1.py \
	-file wordcount_m1.py \
	-reducer wordcount_r1.py \
	-file wordcount_r1.py
hadoop fs -rm -r /users/srack/tmp
