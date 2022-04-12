make clean
make
perf script record -F 1200 -e '{branch-misses, L1-dcache-load-misses, cpu-cycles}' ./wtf
perf script --header > ./script.log
