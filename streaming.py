import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", appName="ReemusStreamer")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 20)
socket_stream = ssc.socketTextStream("0.0.0.0", 5555)
lines = socket_stream.window( 20 )
    
counts = lines.flatMap(lambda line: line.split(" "))\
        .map(lambda word: (word, 1))\
        .reduceByKey(lambda a, b: a+b)

counts.pprint()
ssc.start()
ssc.awaitTermination()
