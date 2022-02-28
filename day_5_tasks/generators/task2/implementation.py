f = open('log.txt', 'r')
result = (line for line in f if 'ERROR' in line)
f.close()
