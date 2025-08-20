import matplotlib.pyplot as plt
import numpy as np

def analyze_satisfaction_data():
    """
    Analyzes patient satisfaction data and generates a trend plot.
    """
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    scores = [1.35, 0.77, 3.41, 5.17]
    average_score = np.mean(scores)
    industry_target = 4.5

    plt.figure(figsize=(10, 6))
    plt.plot(quarters, scores, marker='o', linestyle='-', color='b', label='Quarterly Score')
    plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
    plt.axhline(y=average_score, color='g', linestyle=':', label=f'Average Score ({average_score:.2f})')

    plt.title('Quarterly Patient Satisfaction Scores vs. Industry Target')
    plt.xlabel('Quarter')
    plt.ylabel('Satisfaction Score')
    plt.legend()
    plt.grid(True)

    # Adding the data labels
    for i, score in enumerate(scores):
        plt.text(i, score + 0.1, str(score), ha='center')

    plt.savefig('q8/satisfaction_trend.png')
    print("Analysis complete. Plot saved to q8/satisfaction_trend.png")

if __name__ == '__main__':
    analyze_satisfaction_data()
