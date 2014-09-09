from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

plength = features[:,2]
is_setosa = (data['target'] == 0)
features = features[~is_setosa]
tar = target[~is_setosa]
is_virginica = (tar == 1)
print features.shape, is_virginica.shape
best_acc = -1
for fi in xrange(features.shape[1]):
  print features[:,fi]
  thresh = features[:,fi].copy()
  thresh.sort()
  for t in thresh:
	pred = (features[:,fi] > t)
	acc = np.mean(pred == is_virginica)
	print (pred == is_virginica)
	if acc > best_acc:
	  best_acc = acc
	  best_fi = fi
	  best_t = t
  print "============="

print best_acc, best_fi, best_t

for t,marker,c in zip(xrange(1,3),"ox","gb"):	#marker: > is triangle, o and x are circle and cross respectively
  plt.scatter(features[tar == t,0],
	      features[tar == t,2], 
	      marker = marker, 
	      c = c)			#the arguments to scatter are (x,y,marker,color) 
plt.autoscale(tight=True)
plt.grid(True)
plt.show()

