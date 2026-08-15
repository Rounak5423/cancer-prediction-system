from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
class ModelTrainer:
    def __init__(self):
        pass
    def split_dataset(self,x,y):
        x_train,x_test,y_train,y_test=train_test_split(
            x,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y,
        
        )
        return x_train,x_test,y_train,y_test

    def train_logistic_regression(self,x_train,_y_train):
        model=Pipeline([("scaler",StandardScaler()),
                        ("classifier",LogisticRegression(max_iter=1000))]
            
        )
        model.fit(x_train,_y_train)
        return model
    