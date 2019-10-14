import pandas as pd
import seaborn as sns
import pylab as pl
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
dataset = pd.read_csv('winequality-red.csv')
x0 = dataset.iloc[:, 0:10]
x = x0.apply(lambda x0: x0.fillna(x0.mean()),axis=0)

wcss = []  ##Within Cluster Sum of Squares
##elbow method to know the number of clusters
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,max_iter=300,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
##building the model
nclusters = 3 # this is the k in kmeans based on the elbow method
km = KMeans(n_clusters=nclusters)
km.fit(x)
# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)
##scaling the data
import pandas as pd
from sklearn.decomposition import PCA

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)
x_scaler = scaler.transform(x)
##check the scale effect on the score
km = KMeans(n_clusters=nclusters)
km.fit(x_scaler)

# predict the cluster for each data point
y2_cluster_kmeans = km.predict(x_scaler)
from sklearn import metrics
score2 = metrics.silhouette_score(x_scaler, y2_cluster_kmeans)
print(score2)
##
pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
scaler.fit(x_pca)
x_scaler = scaler.transform(x_pca)
##check the scale effect on the score
km = KMeans(n_clusters=nclusters)
km.fit(x_pca)
#visualization
pl.figure('K-means with 6 clusters')
pl.scatter(x_pca[:, 0], x_pca[:, 1], c=kmeans.labels_)
pl.show()
# predict the cluster for each data point
y3_cluster_kmeans = km.predict(x_pca)
score3 = metrics.silhouette_score(x_pca, y3_cluster_kmeans)
print(score3)