from bitarray import bitarray
import mmh3
import statistics
import math

def trailing_zeros(n):
	s = str(n)
	return len(s)-len(s.rstrip('0'))

input_file =   ['quotes_2008-08.txt','quotes_2008-09.txt','quotes_2008-10.txt','quotes_2008-11.txt','quotes_2008-12.txt',
		'quotes_2009-01.txt','quotes_2009-02.txt','quotes_2009-03.txt','quotes_2009-04.txt']

result = [ "" for i in range(10)]
result_tail = [[] for i in range(10)]
		
for i in input_file:
	fp = open(i,"r", encoding='ISO-8859-1')
	for line in fp:
		stream = line.split("\t")
		if stream[0] is 'Q':
			for seed in range(10):
				result[seed] = format(abs(mmh3.hash(stream[1], seed)), '032b')
				result_tail[seed].append(trailing_zeros(result[seed]))
	fp.close()
group1 = (2**(max(result_tail[0])) + 2**(max(result_tail[1])) + 2**(max(result_tail[2])) + 2**(max(result_tail[3])) + 2**(max(result_tail[4])))/ float(5)
group2 = (2**(max(result_tail[5])) + 2**(max(result_tail[6])) + 2**(max(result_tail[7])) + 2**(max(result_tail[8])) + 2**(max(result_tail[9])))/ float(5)
print (math.ceil(statistics.median([group1, group2])))	
