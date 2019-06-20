import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def make_data(file_name):
    total_data = pd.DataFrame(columns=('a', 'b', 'c', 'd'))
    for i in range(1, 6):
        xy = pd.read_csv(f'./data/{file_name}_{i}.csv', header=None, names=[0, 1, 'a', 'b', 'c', 'd', 2, 3])
        data = xy.drop([0, 1, 2, 3], axis=1)
        bool_index = xy[1].str.contains('/eeg')
        data = data[bool_index]
        data = data[:data.shape[0] % 128 * -1]
        total_data = total_data.append(data, sort=False)
    total_data.to_csv(file_name + '.csv', index=False, header=None)
def combine_data(*filename):
    category_len=[]
    for i in filename:
        total_data = pd.DataFrame(columns=('a', 'b', 'c', 'd'))
        xy = pd.read_csv(f'{i}.csv', header=None, names=['a', 'b', 'c', 'd'])
        category_len.append(xy.shape[0])
        total_data=total_data.append(xy)

    return total_data, category_len

for i in ['blink','chewing','clench','nod','nothing']:
    make_data(i)

total_data , category_len= combine_data('blink', 'chewing', 'clench', 'nod', 'nothing')

normalized_data=MinMaxScaler().fit_transform(total_data.values)
category_num=[]
for i,j in zip(range(0,5),category_len):

    data_len=int(j/128)
    vector3_data = normalized_data.reshape([int(normalized_data.shape[0]/128),128,4])
    zer=np.ones(data_len,dtype='int32')*i
    category_num.extend(zer)
    print(len(category_num))

# total_data = pd.DataFrame(columns=('a','b','c','d'))
# for i in range(1,6):
#     file_name = f'blink'
#     xy = pd.read_csv(f'./data/{file_name}_{i}.csv', header=None, names=[0, 1,'a','b','c','d',2,3])
#     data = xy.drop([0, 1, 2, 3], axis=1)
#     bool_index = xy[1].str.contains('/eeg')
#     data = data[bool_index]
#     data = data[:data.shape[0]%128*-1]
#     total_data = total_data.append(data, sort=False)
#
# total_data.to_csv('modified'+file_name+'.csv', index=False, header=None)
#
# normalized_data=MinMaxScaler().fit_transform(total_data.values)
# print(normalized_data)
# np.savetxt("normalized.csv", normalized_data , delimiter=",")
# print(pd.DataFrame(normalized_data))
# data_num=int(normalized_data.shape[0]/128)
# vector3_data= normalized_data.reshape([data_num,128,4])
# zer=np.ones(data_num,dtype='int32')*2
# print(zer)
# print(len(vector3_data[0]))
#
# print(vector3_data)