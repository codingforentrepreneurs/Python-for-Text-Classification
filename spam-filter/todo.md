# Text Classification with Python
How to improve our training and prediction model after "23 - Scoring Classifier Accuracy"


### Done
1. Binary Classification = spam vs not-spam


### Todo
1. Choose Vectors over One Hot Encoding
2. Use a neural network w/ Keras
3. Category Classification = good vs bad vs neutral vs hated vs loved


### Results
One Hot Encoding with SVM   = 88.25%
Vectors with SVM/Sklearn    = 54.96% - 63.89%, 89.34%
Support Vector Machine with SKLearn:
    - SVC Clasifier:
        With 20 cross validations.
        - All text
            Accuracy Score: 0.8679
            Avg Score: 0.8817
            Standard Deviation : 0.0119
            Range: 0.8710 - 0.9016
        - All text with extra line cleaning
            Accuracy Score: 0.8679
            Avg Score: 0.8817
            Standard Deviation : 0.0119 
            Range: 0.8710 - 0.9016
        - Equal Texts
            Accuracy Score: 0.5648
            Avg Score: 0.5362
            Standard Deviation : 0.0324
            Range: 0.5000 - 0.5882
        - Equal Texts with extra line cleaning
            Accuracy Score: 0.5648
            Avg Score: 0.5362
            Standard Deviation : 0.0324
            Range: 0.5000 - 0.5882

Vectors with Neural Network = 