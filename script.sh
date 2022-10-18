while true
do
	## simulate the 3 clients with a for loop
	for i in {1..3}
	do
		number=$(( $RANDOM % 10 + 1 ))
		## sent the random number to the server
		curl -i http://127.0.0.1:5000/addNumber -X POST -H 'Content-Type: application/json' -d '{"random":"'$number'"}'
		## sleep 1 second to make it more realistic
		sleep 1
	done
	sleep 5
done
