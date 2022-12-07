source './temp_env.sh'
hdfs dfs -rm -r input # Remove input from hdfs
hadoop fs -mkdir -p input
hdfs dfs -put ./files/* input
rm -rf './files'
hdfs dfs -rm -r output # Remove output from hdfs
echo $kval
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-file mapper.py -mapper "python3 mapper.py $kval" \
-file reducer.py -reducer "python3 reducer.py" \
-input input -output output
clear
hadoop fs -cat "./output/*"