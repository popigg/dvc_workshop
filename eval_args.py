from argparse import ArgumentParser
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from model import linearRegression

def main(epochs, lr):

    model = linearRegression(1, 1)
    model.load_state_dict(torch.load(f'models/linear_regression_args.pt'))
    model.eval()

    validation_data = pd.read_csv('partitions/validation.csv')
    X_val = validation_data.iloc[:,0].values
    y_val = validation_data.iloc[:,-1].values

    X_val = torch.from_numpy(X_val.astype(np.float32)).view(-1,1)
    y_val = torch.from_numpy(y_val.astype(np.float32)).view(-1,1)

    predicted = model(X_val).detach().numpy()

    plt.scatter(X_val.detach().numpy()[:150] , y_val.detach().numpy()[:150])
    plt.plot(X_val.detach().numpy()[:150] , predicted[:150] , "red")
    plt.xlabel("Celcius")
    plt.ylabel("Farenhite")
    plt.savefig(f'evaluations/chart_args.png')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-e", "--epochs", help="write report to FILE", metavar="FILE")
    parser.add_argument("-lr", "--learning_rate", help="don't print status messages to stdout")
    args = parser.parse_args()
    main(args.epochs, args.learning_rate)