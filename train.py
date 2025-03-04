## Model ที่ดีที่สุด
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn_genetic import GAFeatureSelectionCV

data = pd.read_csv("diabetes2.csv")
#data.head()
X = data[['Glucose','Insulin','BMI']]
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the GAFeatureSelectionCV with ........... estimator
ga_feature_selection = GAFeatureSelectionCV(estimator=DecisionTreeClassifier(),cv=5)
ga_feature_selection.fit(X_train, y_train)
selected_features = X_train.columns[ga_feature_selection.best_features_]
final_estimator = LogisticRegression()
final_estimator.fit(X_train[selected_features], y_train)

models = [
 ('LoR', LogisticRegression(penalty='l2', C=1.0, solver='lbfgs')),
 ('kNN', KNeighborsClassifier(n_neighbors=5, weights='uniform', metric='minkowski')),
 ('DT', DecisionTreeClassifier(criterion='gini', max_depth=None)),
 ('GB', GradientBoostingClassifier(n_estimators=100, learning_rate=0.5, loss='log_loss', max_depth=2)),
 ('RF', RandomForestClassifier(criterion='log_loss', max_depth=3, n_estimators=141)),
 ('GA', final_estimator),
 ('Adaboost', AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=50, learning_rate=1.0, algorithm='SAMME'))
]

final_estimator.fit(X_train[selected_features], y_train)
VOTE_model = VotingClassifier(estimators=models, voting='hard')
VOTE_model.fit(X_train, y_train)
y_pred = VOTE_model.predict(X_test)
print(accuracy_score(y_test, y_pred))

import pickle
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# 1. ประเมินประสิทธิภาพของแต่ละโมเดล
best_model = None
best_score = 0
best_model_name = ""

results = {}

for name, model in models:
    # ทำการ fit โมเดล
    model.fit(X_train, y_train)

    # ทำนายผลลัพธ์
    y_pred = model.predict(X_test)

    # คำนวณ metrics
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    results[name] = {
        'accuracy': acc,
        'f1_score': f1,
        'precision': precision,
        'recall': recall,
        'model': model
    }

    print(f"Model: {name}, Accuracy: {acc:.4f}, F1 Score: {f1:.4f}")

    # เก็บโมเดลที่ดีที่สุดตาม accuracy (หรือเปลี่ยนเป็น f1 ก็ได้)
    if acc > best_score:
        best_score = acc
        best_model = model
        best_model_name = name

print(f"\nBest model: {best_model_name} with accuracy {best_score:.4f}")

# 2. บันทึกโมเดลที่ดีที่สุดด้วย pickle
with open('best_diabetes_model.pkl', 'wb') as file:
    pickle.dump(best_model, file)

# 3. สำหรับ voting model
with open('voting_diabetes_model.pkl', 'wb') as file:
    pickle.dump(VOTE_model, file)

print("Models saved successfully!")
