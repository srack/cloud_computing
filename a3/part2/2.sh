hadoop fs -rm-r /users/srack/bigrams_output
hadoop fs -rm -r /users/srack/tmp2
echo ''
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input /public/www/* \
	-output /users/srack/tmp2 \
	-mapper bigrams_m0.py \
	-file bigrams_m0.py \
	-reducer bigrams_r0.py \
	-file bigrams_r0.py
echo ''
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.text.key.comparator.options=-nr \
	-input /users/srack/tmp2/part-00000 \
	-output /users/srack/bigrams_output \
	-mapper bigrams_m1.py \
	-file ./bigrams_m1.py \
	-reducer bigrams_r1.py \
	-file ./bigrams_r1.py
echo ''
hadoop fs -rm -r /users/srack/tmp2
