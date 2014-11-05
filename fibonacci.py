#! /usr/bin/env python

nums = [1, 1]
print 1, 1, 
while True:
	nums.append(nums[-2] + nums[-1])
	print nums[-1], 