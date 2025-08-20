import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Patient Satisfaction Score': [1.35, 0.77, 3.41, 5.17]
}
df = pd.DataFrame(data)

# --- Analysis ---
average_score = df['Patient Satisfaction Score'].mean()
industry_target = 4.5

# --- Verification ---
# This print statement will confirm the calculated average.
# The user-provided average is 2.68, and the calculated average is 2.675.
# This is a good place to confirm the value.
print(f"Calculated Average Patient Satisfaction Score: {average_score:.2f}")

# --- Visualization ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the quarterly scores
bars = ax.bar(df['Quarter'], df['Patient Satisfaction Score'], color=['#d9534f', '#d9534f', '#f0ad4e', '#5cb85c'], label='Quarterly Score')

# Adding the industry target and average score lines
ax.axhline(y=industry_target, color='r', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target})')
ax.axhline(y=average_score, color='b', linestyle='-', linewidth=2, label=f'Average Score ({average_score:.2f})')

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom')

# --- Formatting ---
ax.set_title('Quarterly Patient Satisfaction Scores vs. Industry Target', fontsize=16, weight='bold')
ax.set_xlabel('2024 Quarters', fontsize=12)
ax.set_ylabel('Satisfaction Score (out of 5)', fontsize=12)
ax.set_ylim(0, 6)
ax.legend()
ax.grid(axis='y', linestyle='-', alpha=0.7)

# --- Save the Chart ---
plt.savefig('patient_satisfaction_analysis.png', dpi=300)
print("Chart 'patient_satisfaction_analysis.png' saved successfully.")
