# interesting event for amd x86:
# 
# paper's event
# all_l2_cache_hits
# all_l2_cache_misses
# uops_retired
# l3_misses
# 
# 
#
# i find interesting
# ls_int_taken		[Number of interrupts taken]
# ex_ret_mmx_fp_instr.sse_instr	[SSE instructions]
# l1_itlb_misses
# branch-misses
# branch-instructions
# 

perf record -F 10000 -a -e l2_cache_hits_from_dc_misses,l2_cache_hits_from_ic_misses,uops_retired,ex_ret_brn_ind_misp -- sleep 3
perf script > ./temp.log
# perf script --header > ./script.log
# perf record -e L1-dcache-load-misses -c 10000 -ag -- sleep 5
# perf record -e L1-dcache-load-misses -F 10000 -ag -- sleep 5

branch-misses dtlb_load_misses.stlb_hit lsd.uops l2_rqsts.code_rd_miss