default:
	@echo "> Please refer to README for instructions for running the programs"

k-mer:
	@python './standard-implementations/k-mer.py' --source $(source) --kval $(kval) --output $(output)

hadoop-k-mer:
	@bash './utils/check-dependencies.sh'
	rm -rf './temp'
	mkdir './temp'
	python './utils/delegate.py' --source $(source) --kval $(kval) --jobcount $(jobcount) --output './temp'
	echo "kval=$(kval)" > temp_env.sh
	docker cp ./temp namenode:files
	docker cp ./temp_env.sh namenode:temp_env.sh
	docker cp ./map-reduce-python/mapper.py namenode:mapper.py
	docker cp ./map-reduce-python/reducer.py namenode:reducer.py
	docker exec -i namenode bash < './utils/docker-commands.sh'