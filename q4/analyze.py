import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create the q4 directory if it doesn't exist
if not os.path.exists('q4'):
    os.makedirs('q4')

# 1. Generate a synthetic dataset
np.random.seed(42)
data = {
    'Supplier_Lead_Time': np.random.randint(10, 60, 77),
    'Inventory_Levels': np.random.randint(50, 500, 77),
    'Order_Frequency': np.random.randint(1, 15, 77),
    'Delivery_Performance': np.random.uniform(85, 100, 77).round(2),
    'Cost_Per_Unit': np.random.uniform(5, 25, 77).round(2)
}
df = pd.DataFrame(data)
df.to_csv('q4/supply_chain_data.csv', index=False)

# 2. Calculate the correlation matrix
correlation_matrix = df.corr()

# 3. Save the correlation matrix
correlation_matrix.to_csv('q4/correlation.csv')

# 4. Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Matrix of Supply Chain Metrics')
plt.savefig('q4/heatmap.png', dpi=100, bbox_inches='tight') # Saving with 100 DPI and tight bounding box

# 5. Create README.md
with open('q4/README.md', 'w') as f:
    f.write('23f3003060@ds.study.iitm.ac.in\n')

print("Analysis complete. Files are in the 'q4' directory.")
