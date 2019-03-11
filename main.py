# 1.import modules

import ECG_module

# 2.downloading data
# ECG_module.download_dbs()
# 3.convert to csv for 3 dbs , dont forgot to change path for each of them
path = '/home/mohadese/PycharmProjects/ECG/vfdb'
# ECG_module.convert_to_csv(path, 'hea')
# 4.reading number of annotation of a db
extension = 'atr'
a, b, c = ECG_module.read_annotations(path, extension)
# print(a)
# 5.plot one signal with defining path and file name
ECG_module.plotting(path, '418')
# 6.data preprocessing
mn,uulvgyu
