import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Generate synthetic data
np.random.seed(0)
data = {
    "Website Visits": np.random.randint(100, 1000, 100),
    "Purchases": np.random.randint(1, 10, 100),
    "Time on Site (min)": np.random.uniform(1, 30, 100),
    "Emails Opened": np.random.randint(0, 20, 100),
    "Customer Support Interactions": np.random.randint(0, 5, 100),
}
df = pd.DataFrame(data)

# Create correlation matrix
corr_matrix = df.corr()

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create heatmap
plt.figure(figsize=(8, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Customer Engagement Correlation Matrix")

# Save chart
plt.savefig("q5/chart.png", dpi=64, bbox_inches="tight")
