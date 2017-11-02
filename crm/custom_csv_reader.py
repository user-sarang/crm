import csv
import os


def read_csv(file):
	print(file)
	for line in open(file,'r'):
		print(line)