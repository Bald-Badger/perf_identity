perf record -F 12000 -e '{cache-misses}' -a sleep 3
perf script --header > ./temp.log
# perf script --header > ./script.log
