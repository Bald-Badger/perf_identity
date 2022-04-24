import argparse
import csv
import os


def init_parser():
	parser = argparse.ArgumentParser(description='sample hardware counters')

	parser.add_argument(
		'--program', 
		'-p', 
		type=str, 
		default='sleep',
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
		default=10000, 
		help="sample frequency, should be multiple of 400?"
	)

	parser.add_argument(
		'--event', 
		'-e', 
		type=str,
		nargs='+',
		default=['uops_dispatched'],
		help="list of event to be sampled"
	)

	parser.add_argument(
		'--output_name', 
		'-o', 
		type=str,
		default='temp.csv',
		help="output csv file name"
	)

	return parser


def clean():
	os.system('make clean')


def get_data (args):
	event_str = ""
	event_list = args.event
	for e in event_list:
		event_str += e
		event_str += ','
	event_str = event_str[:-1] # remove last comma

	record_cmd = "sudo perf script record -a -F {sample_freq} -e {event_list} -- {program} {time}".format(
			sample_freq=str(args.sample_freq),
			event_list=event_str,
			program=args.program,
			time=args.time
		).strip()
	print(record_cmd)
	os.system(record_cmd)
	os.system("sudo perf script > ./temp.log")


def get_line_list(filename:str):
	with open(filename) as file:
		lines_raw = [line.rstrip() for line in file]
	lines_raw = list(lines_raw)
	lines = []
	for l in lines_raw:
		l = l.split()
		if len(l) == 9: # get rid of wired lines that I'm too lazy to sanitize
			lines.append(l)
	del lines[:1000] # delete first 1000 rows
	return lines


def write_csv(lines:list, filename:str):
	fields = [
		'process_name',
		'pid',
		'idk',
		'time',
		'counter',
		'event_name',
		'pc',
		'pc_tag',
		'path'
	]

	with open(filename, 'w') as csvfile: 
		csvwriter = csv.writer(csvfile) 
		csvwriter.writerow(fields)  
		csvwriter.writerows(lines)


if __name__ == '__main__':
	clean()
	p = init_parser()
	args = p.parse_args()
	get_data(args)
	lines = get_line_list('./temp.log')
	write_csv(lines,args.output_name)

