import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

# Creating the DataFrame from the given image data
data = {
    'Unit': list(range(1, 17)),
    'Kaffe': [90, 82, 88, 96, 94, 27, 30, 50, 95, 73, 97, 94, 12, 70, 23, 30],
    'Pulverkaffe': [49, 10, 42, 62, 38, 27, 26, 31, 51, 72, 13, 52, 17, 12, 40, 52],
    'Te': [88, 68, 63, 98, 48, 36, 99, 77, 61, 85, 21, 38, 13, 84, 40, 99],
    'Soedemiddel': [19, 2, 4, 32, 11, 2, 22, 22, 15, 29, 5, 35, 14, 62, 11, 80],
    'Kiks': [57, 55, 76, 62, 74, 9, 91, 72, 29, 51, 6, 66, 62, 18, 23, 80],
    'Frossen': [27, 4, 11, 14, 13, 20, 26, 22, 15, 54, 35, 51, 18, 64, 57, 5],
    'Aebler': [81, 67, 87, 83, 76, 85, 68, 51, 49, 79, 56, 81, 78, 67, 77, 57],
    'Appelsin': [75, 71, 84, 89, 76, 68, 92, 61, 42, 70, 78, 72, 64, 37, 57, 52],
    'Marmelade': [71, 46, 45, 81, 57, 91, 91, 48, 41, 61, 75, 64, 51, 57, 38, 89],
    'Hvidloeg': [22, 80, 88, 15, 29, 20, 11, 16, 51, 64, 9, 11, 7, 11, 16, 5],
    'Smoer': [91, 66, 94, 84, 94, 65, 95, 22, 51, 82, 68, 92, 51, 44, 84, 97],
    'Margarine': [85, 24, 47, 80, 57, 78, 94, 68, 72, 48, 32, 91, 51, 51, 25, 25],
    'Olivenoile': [74, 94, 36, 83, 29, 84, 57, 16, 28, 61, 48, 30, 37, 31, 31, 3],
    'Yoghurt': [30, 5, 57, 53, 20, 31, 11, 6, 13, 48, 3, 11, 11, 16, 3, 3],
    'Knaeckbroed': [26, 18, 3, 15, 5, 24, 28, 9, 6, 30, 93, 34, 62, 64, 16, 9]
}

df = pd.DataFrame(data)

# Calculating the ranges
ranges = df.describe().loc[['min', 'max']].transpose()

ranges

# Pairplot of variables
sns.pairplot(df.drop(columns=['Unit']))
plt.show()

# PCA plot
from sklearn.decomposition import PCA
import numpy as np

# Standardizing the data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop(columns=['Unit']))

# Applying PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(scaled_data)

# Creating a DataFrame for PCA components
pca_df = pd.DataFrame(data=pca_components, columns=['PC1', 'PC2'])
pca_df['Unit'] = df['Unit']

# Plotting the first two components
plt.figure(figsize=(10, 7))
sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Unit', palette='viridis', s=100)
plt.title('PCA of the dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()

# Given Points
points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])

# Applying DBSCAN
dbscan = DBSCAN(eps=4, min_samples=4)
clusters = dbscan.fit_predict(points)

# Plotting clusters
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], c=clusters, cmap='viridis', s=100)
plt.title('DBScan Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# If Epsilon is increased to √10
dbscan_eps_sqrt10 = DBSCAN(eps=np.sqrt(10), min_samples=4)
clusters_eps_sqrt10 = dbscan_eps_sqrt10.fit_predict(points)

# Plotting clusters for eps=√10
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], c=clusters_eps_sqrt10, cmap='viridis', s=100)
plt.title('DBScan Clustering with Epsilon = √10')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Applying K-means clustering with an initial guess of 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(pca_components)

# Adding cluster information to the PCA DataFrame
pca_df['Cluster'] = clusters

# Plotting the clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Cluster', palette='viridis', s=100)
plt.title('PCA of the dataset with K-means Clusters')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()

# Displaying the units and their corresponding clusters
cluster_assignments = pca_df[['Unit', 'Cluster']].sort_values(by='Cluster')
cluster_assignments