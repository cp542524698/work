pids=`netstat -antp |grep :7777 |awk '{print $7}'`
kill -9 ${pids%%/*}
