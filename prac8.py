import matplotlib.pyplot as plt

from matplotlib import style

from sklearn.cluster import KMeans

from sklearn.datasets.samples_generator import make_blobs

style.use("fivethirtyeight")

# make_blobs() is used to generate sample points
# around c centers (randomly chosen)

X, y = make_blobs(n_samples = 100, centers = 4,

cluster_std = 1, n_features = 2)

plt.scatter(X[:, 0], X[:, 1], s = 30, color ='b')

# label the axes

plt.xlabel('X')

plt.ylabel('Y')

plt.show()

plt.clf() # clear the figure
