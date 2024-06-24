import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# Generate random binary classification data
np.random.seed(42)
actual = np.random.binomial(1, 0.5, size=100)  # Actual data (binary)
predicted = np.random.binomial(1, 0.6, size=100)  # Predicted data (binary)

# Create confusion matrix
confusion_matrix = metrics.confusion_matrix(actual, predicted)

# Display confusion matrix
print("Confusion Matrix:")
print(confusion_matrix)

# Plot confusion matrix
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0, 1])
cm_display.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

# Calculate and print evaluation metrics
accuracy = metrics.accuracy_score(actual, predicted)
precision = metrics.precision_score(actual, predicted)
recall = metrics.recall_score(actual, predicted)
specificity = metrics.recall_score(actual, predicted, pos_label=0)
f1_score = metrics.f1_score(actual, predicted)

print("\nEvaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall (Sensitivity): {recall:.2f}")
print(f"Specificity: {specificity:.2f}")
print(f"F1 Score: {f1_score:.2f}")
