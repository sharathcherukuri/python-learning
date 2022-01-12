import sys
import collections
import math

Statistics = collections.namedtuple("Statistics","mean,mode,median,std_dev")

def main():
    if len(sys.argv) ==1 or sys.argv[1] in {'-h','--help'}:
        print("usage: {0} file1[file2...[filen]]".format(sys.argv[0]))
        sys.exit()
    numbers=[]
    frequncies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename,numbers,frequncies)
    if numbers:
        statistics=cal_stats(numbers,frequncies)
        print_results(len(numbers),statistics)
    else:
        print("no numbers are found")

def read_data(filename,numbers,frequncies):
    for lino,line in enumerate(open(filename),start=1):
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                frequncies[number]+=1
            except ValueError as err:
                print("{0}:{1}: skipping{2}:{3}".format(filename, lino ,x ,err))

def cal_stats(numbers,frequncies):
    mean= sum(numbers)/len(numbers)
    mode = cal_mode(frequncies,3)
    median = cal_median(numbers)
    std_dev = cal_stddev(mean, numbers)
    return Statistics(mean,mode,median,std_dev)

def cal_mode(frequncies, maximum_modes):
    highest_freq = max(frequncies.values())
    mode = [number for number,frequncy in frequncies.items()
            if math.fabs(frequncy - highest_freq) <= sys.float_info.epsilon]
    if not (1<= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode

def cal_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[middle -1])/2
    return median

def cal_stddev(mean, numbers):
    total = 0
    for number in numbers:
        total+= (number- mean)**2
    variance = total / (len(numbers)-1)
    return math.sqrt(variance)

def print_results(count, statistics):
    real = '9.2f'

    if statistics.mode is None:
        modeline= ''
    elif len(statistics.mode) ==1:
        modeline ="mode   = {0:{fmt}}\n".format(statistics.mode[0], fmt =real)
    else:
        modeline = ("mode   = [" +
                    ', '.join(["{0:.2f}".format(m)
                               for m in statistics.mode]) + "]\n")
    print("""\
count   ={0:6}
mean    ={1.mean:{fmt}}
median  ={1.median:{fmt}}
{2}\
std.dev ={1.std_dev:{fmt}}""".format(count, statistics, modeline, fmt =real))
    
    
 
