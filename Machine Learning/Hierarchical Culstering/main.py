import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# Generate synthetic data
X, _ = make_blobs(n_samples=10, centers=3, n_features=2, random_state=42)

# Perform hierarchical/agglomerative clustering
Z = linkage(X, method='ward')

# Plot dendrogram
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data point index')
plt.ylabel('Distance')
plt.show()

# Plot clustered data points
plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c='blue', marker='o', edgecolor='black', s=100)
plt.title('Clustered Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
