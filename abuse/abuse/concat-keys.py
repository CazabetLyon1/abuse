import pandas as pd

link = "https://www.bitcoinabuse.com/reports/"


def extend_text(value):
    value2 = link + value
    return value2


keys = pd.read_csv('keys_reduced.csv', delimiter=',')
tab_keys = keys.as_matrix()

for i in range(len(tab_keys)):
    tab_keys[i] = extend_text(tab_keys[i])
