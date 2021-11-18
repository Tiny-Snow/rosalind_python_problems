import sys

max_gc = 0
max_ID = ''
last_seq = ''
last_ID = ''

while True:
    line = sys.stdin.readline().rstrip()
    if line == '':
        break
    
    if line[0] == '>':
        if last_seq != '':
            num_gc = (last_seq.count('G') + last_seq.count('C')) / len(last_seq)
            
            if num_gc > max_gc:
                max_gc = num_gc
                max_ID = last_ID
            
        last_ID = line[1: ]
        last_seq = ''

    else:
        last_seq += line

# 处理最后的序列
if last_seq != '':
    num_gc = (last_seq.count('G') + last_seq.count('C')) / len(last_seq)
    
    if num_gc > max_gc:
        max_gc = num_gc
        max_ID = last_ID

print(max_ID)
print(max_gc * 100)