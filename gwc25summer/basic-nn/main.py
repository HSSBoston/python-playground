import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import  confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from collections import defaultdict

# Load the training dataset
train_data = pd.read_csv('sign_mnist_13bal_train.csv')

# Separate the data (features) and the  classes
X_train = train_data.drop('class', axis=1)  # Features (all columns except the first one)
X_train = X_train / 255.0
y_train = train_data['class']   # Target (first column)

# Load the testing dataset
test_data = pd.read_csv('sign_mnist_13bal_test.csv')

# Separate the data (features) and the  classes
X_test = test_data.drop('class', axis=1)  # Features (all columns except the first one)
X_test = X_test / 255.0
y_test = test_data['class']   # Target (first column)

# Use this line to get you started on adding a validation dataset
X_train, X_validate, y_train, y_validate = train_test_split(X_train, y_train, test_size = 20, random_state = 0, stratify = y_train)

neural_net_model = MLPClassifier(hidden_layer_sizes=(40,30),random_state=30,tol=0.005)

neural_net_model.fit(X_train, y_train)
# Determine model architecture 
layer_sizes = [neural_net_model.coefs_[0].shape[0]]  # Start with the input layer size
layer_sizes += [coef.shape[1] for coef in neural_net_model.coefs_]  # Add sizes of subsequent layers
layer_size_str = " x ".join(map(str, layer_sizes))
print(f"Training set size: {len(y_train)}")
print(f"Layer sizes: {layer_size_str}")


# predict the classes from the training and test sets
y_pred_train = neural_net_model.predict(X_train)
y_pred_validate = neural_net_model.predict(X_validate)
y_pred_test = neural_net_model.predict(X_test)

# Create dictionaries to hold total and correct counts for each class
correct_counts = defaultdict(int)
total_counts = defaultdict(int)
overall_correct = 0

# Count correct test predictions for each class
for true, pred in zip(y_test, y_pred_test):
    total_counts[true] += 1
    if true == pred:
        correct_counts[true] += 1
        overall_correct += 1

 # Count correct validation predictions for each class   
total_counts_validate = 0
correct_counts_validate = 0
for true, pred in zip(y_validate, y_pred_validate):
    total_counts_validate += 1
    if true == pred:
        correct_counts_validate += 1

# For comparison, count correct _training_ set predictions
total_counts_training = 0
correct_counts_training = 0
for true, pred in zip(y_train, y_pred_train):
    total_counts_training += 1
    if true == pred:
        correct_counts_training += 1

# Calculate and print accuracy for each class and overall test accuracy
for class_id in sorted(total_counts.keys()):
    accuracy = correct_counts[class_id] / total_counts[class_id] *100
    print(f"Accuracy for class {class_id}: {accuracy:3.0f}%")
print(f"----------")
overall_accuracy = overall_correct / len(y_test)*100
print(f"Overall Test Accuracy: {overall_accuracy:3.1f}%")
overall_training_accuracy = correct_counts_training / total_counts_training*100
print(f"Overall Training Accuracy: {overall_training_accuracy:3.1f}%")
overall_validation_accuracy = correct_counts_validate / total_counts_validate*100
print(f"Overall Validation Accuracy: {overall_validation_accuracy:3.1f}%")

#print evaluation of the model
print("\nThe model misidentifies the letter F as letter K and the letter G as letter H the most. This makes sense because the sign for each pair are quite similar looking. F and K both have the palm facing away from the signer with more than 1 finger up, and G and H have either 1 or 2 fingers pointing the right of the signer in the same way.\n")

#create and print confusion matrix (to determine which letters are most often misidentified)
conf_matrix = confusion_matrix(y_test, y_pred_test)
class_ids = sorted(total_counts.keys())

# For better formatting
print("Confusion Matrix:")
print(f"{'':9s}", end='')
for label in class_ids:
    print(f"Class {label:2d} ", end='')
print()  # Newline for next row

for i, row in enumerate(conf_matrix):
    print(f"Class {class_ids[i]}:", " ".join(f"{num:8d}" for num in row))