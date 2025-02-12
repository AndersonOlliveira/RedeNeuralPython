import pandas as pd 
import plotly.express as px
import numpy as np
from sklearn.cluster import KMeans



X = np.random.randint(100, size=(100,2))

kMeans = KMeans(n_clusters=3, random_state=0).fit(X)

xdf = pd.DataFrame(X)

xdf['class'] = kMeans.labels_

xdf['class'] = xdf['class'].astype('string')

px.scatter(xdf,x=0,y=1,color='class', title='k-Means')

kMeans.predict([[0,0], [12,3]])

kMeans.cluster_centers_
