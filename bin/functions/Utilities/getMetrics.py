# This script provides a report of the output with different metrics by comparing the true values and the estimated ones




from sklearn.metrics import classification_report
y_true = [0, 1, 1, 0, 0]
y_pred = [0, 0, 1, 1, 0]
target_names = ['class 0 (buried)', 'class 1 (exposed)']


print(classification_report(y_true, y_pred, target_names=target_names))



