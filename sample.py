import argparse

if __name__ == '__main__':
	event_list_x86_amd = ['']

	parser = argparse.ArgumentParser(description='sample hardware counters')

	parser.add_argument(
		'--program', 
		'-p', 
		type=str, 
		required=True, 
		help="the program to run when couting"
	)

	parser.add_argument(
		'--time', 
		'-t', 
		type=int, 
		required=False,
		default=3, 
		help="time to take samples"
	)

	parser.add_argument(
		'--sample_freq', 
		'-f', 
		type=int, 
		required=False,
		default=1600, 
		help="sample frequency, should be multiple of 400?"
	)

	parser.add_argument(
		'--event', 
		'-e', 
		type=str,
		nargs='+',
		required=True,
		help="list of event to be sampled"
	)

	args = parser.parse_args()

	event_str = ""
	event_list = args.event
	for e in event_list:
		event_str += e
		event_str += ' '

	record_cmd = "perf script record -F {sample_freq} -e {event_list} {program}".format(
			sample_freq=str(args.sample_freq),
			event_list=event_str,
			program=args.program
		).strip()
	print(record_cmd)


