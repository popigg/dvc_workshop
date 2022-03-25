from argparse import ArgumentParser
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import linearRegression

def main(epochs, lr):

    num_epochs = epochs
    learning_rate = lr
    model = linearRegression(1, 1)
    l = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr =learning_rate )

    train_data = pd.read_csv('partitions/train.csv')
    X_train = train_data.iloc[:,0].values
    y_train = train_data.iloc[:,-1].values

    X_train = torch.from_numpy(X_train.astype(np.float32)).view(-1,1)
    y_train = torch.from_numpy(y_train.astype(np.float32)).view(-1,1)

    with open(f'metrics/train_loss_{epochs}_{lr}.txt', 'w') as f:

        train_losses = []

        for epoch in range(num_epochs):
            # forward feed
            y_pred = model(X_train.requires_grad_())

            # calculate the loss
            loss= l(y_pred, y_train)

            # backward propagation: calculate gradients
            loss.backward()

            # update the weights
            optimizer.step()

            # clear out the gradients from the last step loss.backward()
            optimizer.zero_grad()

            train_losses.append(loss.item())
            # print(f'epoch {epoch}, loss {loss.item()}')
            f.write(f'epoch {epoch}, loss {loss.item()} \n')
    
    torch.save(model.state_dict(), f'models/linear_regression_{epochs}_{lr}.pt')
    
    plt.plot(range(0,num_epochs), train_losses, 'g', label='Training loss')
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.savefig(f'metrics/train_loss_{epochs}_{lr}.png')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-e", "--epochs", help="write report to FILE", metavar="FILE")
    parser.add_argument("-lr", "--learning_rate", help="don't print status messages to stdout")
    args = parser.parse_args()
    main(int(args.epochs), float(args.learning_rate))    