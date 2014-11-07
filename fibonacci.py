#! /usr/bin/env python
import pf
howMany = iinp("How many Fibonacci numbers should I create?")

nums = [1, 1]
print 1, 1, 
for i in range(2, howMany):
	nums.append(nums[-2] + nums[-1])
	print nums[-1], 