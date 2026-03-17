import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv("data/raw/sf_data.csv")

# Step 2: Keep only neighborhood column
df = df[['analysis_neighborhood']].dropna()

# Step 3: Count incidents per neighborhood
counts = df['analysis_neighborhood'].value_counts()
counts_df = counts.reset_index()
counts_df.columns = ['Neighborhood', 'Incident_Count']

# Step 4: Sort neighborhoods (ranking)
counts_df = counts_df.sort_values(by='Incident_Count', ascending=False)

# Step 5: Clustering (data mining part)
X = counts_df[['Incident_Count']]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
counts_df['Cluster'] = kmeans.fit_predict(X)

# Step 6: Cluster summary (for explanation)
cluster_summary = counts_df.groupby('Cluster')['Incident_Count'].mean().sort_values()

print("\nNeighborhood Results:")
print(counts_df)

print("\nCluster Summary:")
print(cluster_summary)

# Step 7: Save results
counts_df.to_csv("output/neighborhood_safety.csv", index=False)
cluster_summary.to_csv("output/cluster_summary.csv")

# Step 8: Graph (top 10)
counts_df.head(10).plot(
    kind='bar',
    x='Neighborhood',
    y='Incident_Count'
)

plt.title("Top 10 Neighborhoods by Incidents")
plt.tight_layout()
plt.show()