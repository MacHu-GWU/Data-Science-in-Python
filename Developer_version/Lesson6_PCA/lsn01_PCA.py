import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print X
pca = PCA(n_components=2)
pca.fit(X)
print pca.explained_variance_ratio_
X1 = pca.transform(X)


plt.plot(X.transpose()[0], X.transpose()[1], 'ro')
plt.plot(X1.transpose()[0], X1.transpose()[1], 'bo')
plt.show()