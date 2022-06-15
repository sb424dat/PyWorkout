#ch1_ex3_RunTiming.py

def run_timing(*args):

	user_run1 = int(input('10 km run time: '))
	user_run2 = int(input('10 km run time: '))	
	user_run3 = int(input('10 km run time: '))

	print("Average run time =", (user_run3+user_run1+user_run2)/3, "over 3 runs")

run_timing()	


def run2_timing(*args):
	try:
		n = float(input('Enter a number: '))
		print(f'n = {n}')
	except ValueError as e:
		print("Hey! That's not a valid number! ")


def run2_timing():
	inital_runs = 0
	total_time = 0
	while True:
		one_run = input('Enter 10km run time: ')

		if not one_run:
			break

		inital_runs += 1
		total_time += float(one_run)

	average_time = total_time / inital_runs

	print(f'Average of {average_time}, over {inital_runs} runs')

run2_timing()