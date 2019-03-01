import os
import wfdb
import pandas as pd
import matplotlib.pyplot as plt


"""downloading 3 databases online"""


def download_dbs():
    cwd = os.getcwd()
    dl_dir = os.path.join(cwd, 'mitdb')
    wfdb.dl_database('mitdb', dl_dir=dl_dir)
    dl_dir = os.path.join(cwd, 'vfdb')
    wfdb.dl_database('vfdb', dl_dir=dl_dir)
    dl_dir = os.path.join(cwd, 'cudb')
    wfdb.dl_database('cudb', dl_dir=dl_dir)


"""converting to csv in the directories"""


def convert_to_csv(path, extension):
    files1 = sorted([os.path.splitext(filename)[0] for filename in os.listdir(path) if filename.endswith(extension)])
    # print(files1)  # show name of files in each database without extension
    os.chdir(path)
    for i in files1:
        record1 = wfdb.rdsamp("{}".format(i))
        # print(record1[0].shape[1])
        # print(record1[0].ndim)
        if record1[0].shape[1] == 2:
            columns = ['ECG_1', 'ECG_2']
        else:
            columns = ['ECG_1']
        x = pd.DataFrame(record1[0], columns=columns)
        x.to_csv(os.path.join(path, '{}'.format(i)),
                 columns=['ECG_1'])  # saving one column of data, ignoring second channel
        # print(x.head())
    return files1


"""reading number of annotation """


def read_annotations(path, extension):
    db = input('enter database name: ')
    files1 = sorted([os.path.splitext(filename)[0] for filename in os.listdir(path) if filename.endswith(extension)])
    ann_list: list = []
    os.chdir(path)
    for i in files1:
        ann = wfdb.rdann("{}".format(i), extension)
        ann_list.append(ann.ann_len)
    # print('ann_{}:'.format(db), ann_list)
    # print(sum(ann_list))
    return ann_list, sum(ann_list),ann.sample #  return 3 parameter


"""visualize one ecg record"""


def plotting(path, filename):
    os.chdir(path)
    ecg = pd.read_csv(filename, index_col=0)
    # print(ecg.head())
    plt.plot(ecg)
    plt.xlabel('samples')
    plt.ylabel('ecg_signal')
    plt.title('plotting ecg of one record')
    plt.show()


def preprocessing_ecg(path,extension):
    preprocessed = []
    for i in convert_to_csv(path, extension):
        os.chdir(path)
        ecg = pd.read_csv(i, index_col=0)
        # print(ecg.ndim)
        ecg = ecg.values.reshape(len(ecg)) # reshaping to 1 dimension for further processing
        preprocessed.append(ecg)
        # print(type(ecg))
        # print(ecg.shape)
        # print(ecg.ndim)
    # print(preprocessed[0].shape)
    # print(len(preprocessed))
    # print(type(preprocessed))