#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals # this is so one can use the angstrom symbol in plot labels \u
import numpy as np # 
import matplotlib.pyplot as plt # pyplot is used for plotting
import glob # glob is used extract the names of each file for plotting uses

# append each dos to a list of its own, including the first column of energy values

# parse data from file by calling parser with the argument fname = your_filename e.g., parser('filename.data')
def parser(fname, sys): # create function parser and take in the value of filename and sys: 0=C, 1=C-H, 2=GaN, 3=GaN-H when calling the function
	en, t_up, t_down, c_sup, c_sdown, c_pup, c_pdown, ga_sup, ga_sdown, ga_pup, ga_pdown, ga_dup, ga_ddown, n_sup, n_sdown, n_pup, n_pdown, h_up, h_down = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []  # create empty lists to story values
	f = open(fname, 'r').readlines() # open and read through file
	for line in f: # loop over each line in the opened file
		values = [float(n) for n in line.split()] # split file lines into individual values
		en.append(values[0]) # add values to en list from first column of fname
		t_up.append(values[1]) # add values to t_up list from second column of fname
		t_down.append(values[2]) 
		# note: columns immeditately after t_up and t_down are total spin_up and spin_down for each element
		# note: remember to skip these lines
		if sys == 0
			c_sup.append(values[])
			c_sdown.append(values[])
			c_pup.append(values[])
			c_pdown.append(values[])
			
		elif sys == 1
			c_sup.append(values[])
			c_sdown.append(values[])
			c_pup.append(values[])
			c_pdown.append(values[])
			h_up.append(values[])
			h_down.append(values[])

		elif sys == 2
			ga_sup.append(values[])
			ga_sdown.append(values[])
			ga_pup.append(values[])
			ga_pdown..append(values[])
			ga_dup.append(values[])
			ga_ddown.append(values[])
			n_sup.append(values[])
			n_sdown.append(values[])
			n_pup.append(values[])
			n_pdown.append(values[])

		elif sys == 3
			ga_sup.append(values[])
			ga_sdown.append(values[])
			ga_pup.append(values[])
			ga_pdown..append(values[])
			ga_dup.append(values[])
			ga_ddown.append(values[])
			n_sup.append(values[])
			n_sdown.append(values[])
			n_pup.append(values[])
			n_pdown.append(values[])
			h_up.append(values[])
			h_down.append(values[])

	return en, t_up, t_down, c_sup, c_sdown, c_pup, c_pdown, ga_sup, ga_sdown, ga_pup, ga_pdown, ga_dup, ga_ddown, n_sup, n_sdown, n_pup, n_pdown, h_up, h_down # returns the values of x and y to be used further in the code

names = sorted(glob.glob('')) # obtain the name of each file

sys = [0, 1, 2, 3]
index = 0
while index < len(names):
	data = parser(name[index], index)
	en = data[0]
	# multiple y values or loop over values??
	y = 
	index += 1


# plot tdos comparison 3x3 subplot with size-dep H-dep and dip-dep across the top, and C Ga and N down the left side
# plot individual pdos plots for supllemental information
# tic marks all around the plot
# times new roman font
# no box around legend
