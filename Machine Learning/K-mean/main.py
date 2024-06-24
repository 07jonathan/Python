import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data points
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))

# Calculate inertia for different values of K
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# Plotting the elbow curve
plt.plot(K_range, inertias, marker='o')
plt.title('Elbow Method For Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.xticks(K_range)
plt.grid(True)
plt.show()

# Based on the elbow curve, choose the optimal K and perform clustering
optimal_k = 2  # Adjust this based on the elbow plot
kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(data)
cluster_labels = kmeans.labels_

# Plotting the clusters
plt.scatter(x, y, c=cluster_labels, cmap='viridis')
plt.title(f'K-means Clustering with K={optimal_k}')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
