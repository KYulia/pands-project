import pandas as pd
import matplotlib.pyplot as plt
from os import path
import os

#outpath = ""
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Users/alexe/Desktop/programming/AAA_MishaHelp/')

# reading from the files: this gives us a "dataframe" i.e. python friendly excel sheet, for each file
df1 =  pd.read_csv('setosa.data', sep=",")
df3 =  pd.read_csv('versicolor.data', sep=",")
df2 =  pd.read_csv('virginica.data', sep=",")

#this creates a list of the three dataframes, so that I can access each in a for loop and program them all to give me the same thing (see below loop)
all_data = [df1, df2, df3]

num_bins = 20  # Change this number as you need

# Create separate histograms
count=0
for file in all_data:
	ax = file.hist(bins=num_bins)
	#ax.savefig('file_{count}.png')
	count += 1

plt.show()
plt.savefig(results_dir+'histograms_try')

#for i in range(1, len(ax)):
#	image.set_data(x,ax[i])
#	#plt.draw()
#	fig.savefig(path.join(outpath,"dataname_{0}.png".format(i))