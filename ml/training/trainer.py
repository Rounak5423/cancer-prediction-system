from sklearn.model_selection import train_test_split

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