import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve

# Generate example data
n = 10000
y = np.array([0] * n + [1] * n)

# Example model probabilities
y_prob_1 = np.array(
    np.random.uniform(0.25, 0.5, n//2).tolist() +
    np.random.uniform(0.3, 0.7, n).tolist() +
    np.random.uniform(0.5, 0.75, n//2).tolist()
)

y_prob_2 = np.array(
    np.random.uniform(0, 0.4, n//2).tolist() +
    np.random.uniform(0.3, 0.7, n).tolist() +
    np.random.uniform(0.6, 1, n//2).tolist()
)

# Calculate accuracy scores
accuracy_model_1 = accuracy_score(y, y_prob_1 > 0.5)
accuracy_model_2 = accuracy_score(y, y_prob_2 > 0.5)

print(f'Model 1 accuracy score: {accuracy_model_1}')
print(f'Model 2 accuracy score: {accuracy_model_2}')

# Calculate AUC-ROC scores
auc_model_1 = roc_auc_score(y, y_prob_1)
auc_model_2 = roc_auc_score(y, y_prob_2)

print(f'Model 1 AUC score: {auc_model_1}')
print(f'Model 2 AUC score: {auc_model_2}')

# Plot ROC curves
def plot_roc_curve(true_y, y_prob, model_name=''):
    fpr, tpr, thresholds = roc_curve(true_y, y_prob)
    auc = roc_auc_score(true_y, y_prob)
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {auc:.2f})')
    plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random Guessing')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()

plot_roc_curve(y, y_prob_1, model_name='Model 1')
plot_roc_curve(y, y_prob_2, model_name='Model 2')
