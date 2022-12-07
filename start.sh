#!/env/bash
rm -r './map-reduce-python/input/'
mkdir './map-reduce-python/input'
python './map-reduce-python/tasker.py'
# docker cp ./map-reduce-python/input namenode:files
# docker cp ./map-reduce-python/mapper.py namenode:mapper.py
# docker cp ./map-reduce-python/reducer.py namenode:reducer.py