from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

plength = features[:,2]
is_setosa = (data['target'] == 0)
print plength[is_setosa].max()
print plength[~is_setosa].min()

for t,marker,c in zip(xrange(3),">ox","rgb"):	#marker: > is triangle, o and x are circle and cross respectively
  plt.scatter(features[target == t,1],
	      features[target == t,2], 
	      marker = marker, 
	      c = c)			#the arguments to scatter are (x,y,marker,color) 
plt.autoscale(tight=True)
plt.grid()
plt.show()
