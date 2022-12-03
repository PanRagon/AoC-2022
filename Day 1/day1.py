import re;
from input import input;

newVal = re.sub(r',{2}', "][", input)

arr = newVal.split('][');

def splitFun(item):
	return item.split(',')

arr = list(map(splitFun, arr))

sumArr = [];
for item in arr:
	sumArr.append(sum(list(map(int, item))))

sumArr.sort(reverse=True);

print(sumArr[0])

print(sum(sumArr[0:3]))