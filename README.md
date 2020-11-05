# FraudDetectionConcur
Fraud Detection Framework Expenses Auditing 

The project focuses on Fraud detection and Expense Prediction problems for the given dataset

1. Fraud Detection:
    Tracking anomalies in the relatively small dataset was challenging with data imbalance. 
    Tackling the data imbalance has been done with SOMGEN library. It uses Synthetic Minority Oversampling Technique (SMOTE) for regression purpose.
    Based on the K-NN clustering the undersampled observations in the data distribution are bootstrapped and added back in the dataset
    For details please check https://github.com/nickkunz/smogn/blob/master/examples/smogn_example_2_int.ipynb

2. Expense Prediction:
    Using L2 regression, (for maintaining features in the model and avoid sparsity) the travel expenses of the employee can be given based on 
    'Stay', 'expense_num','air_fare', 'hotel', 'car_rental', 'per_diem','per_diem_based_on_rate','total_expense'
