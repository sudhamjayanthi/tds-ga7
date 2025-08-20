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
sns.set_style("white")
plt.rcParams.update({'font.size': 9})

# Create figure with exact 512x512 pixels
fig, ax = plt.subplots(figsize=(5.12, 5.12))

# Create heatmap with better formatting
heatmap = sns.heatmap(corr_matrix, 
                      annot=True, 
                      cmap="coolwarm", 
                      fmt=".2f",
                      square=True,
                      cbar_kws={"shrink": 0.7, "aspect": 20},
                      linewidths=0.5,
                      ax=ax)

# Improve title positioning
plt.title("Customer Engagement Correlation Matrix", 
          fontsize=12, fontweight='bold', pad=15)

# Fix label positioning and rotation
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(rotation=0, fontsize=8)

# Adjust layout to prevent cutoff
plt.subplots_adjust(top=0.9, bottom=0.2, left=0.2, right=0.9)

# Save chart as exactly 512x512 pixels
plt.savefig("q5/chart.png", dpi=100, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()
