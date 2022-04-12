make clean
make
perf record -F 1200 -e '{branch-misses, bp_l1_tlb_fetch_hit}' ./wtf
perf script > ./script.log
