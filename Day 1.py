#Day 1 code
'''The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and 
the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?'''



def get_calibration_sum(file_path):
    import re
    lines= open(file_path).readlines()
    sum=0

    for line in lines:
        digits=re.findall(r'\d',line)
        if len(digits)==0:
            num=0
        elif len(digits)==1:
            num=int(str(digits[0])+str(digits[0]))
        else:
            num=int(str(digits[0])+str(digits[-1]))
        sum+=num
    
    return sum


x= get_calibration_sum('Day 1 Input.txt')
print(x)