import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    train_data = pd.read_csv('data/training.csv')
    X_train = train_data.iloc[:,0].values
    y_train = train_data.iloc[:,-1].values    
    sc = MinMaxScaler()
    sct = MinMaxScaler()
    X_train=sc.fit_transform(X_train.reshape(-1,1))
    y_train =sct.fit_transform(y_train.reshape(-1,1))

    n_samples = X_train.shape[0]
    n_val = int(0.2 * n_samples)
    X_train = X_train[:-n_val]
    y_train = y_train[:-n_val]

    X_val = X_train[-n_val:]
    y_val = y_train[-n_val:]

    train = np.c_[X_train, y_train]
    validation = np.c_[X_val, y_val]
    np.savetxt("partitions/train.csv", train, delimiter=",")
    np.savetxt("partitions/validation.csv", validation, delimiter=",")

if __name__ == '__main__':
    main()