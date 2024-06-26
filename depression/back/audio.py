import os
from re import A
import pandas as pd
import numpy as np
from sklearn import preprocessing
import tensorflow as tf
from tcn import TCN

#通过openSmile提取音频特征
def audio_Feature(audio_path,audio_feature_txt):
    path = 'cd /d H:/opensmile-3.0-win-x64/bin && SMILExtract.exe -C H:/opensmile-3.0-win-x64/config/is09-13/IS09_emotion.conf -I '+audio_path + ' -O '+ audio_feature_txt
    os.system(path)

#将openSmile提取出txt文件转换成csv文件
def Feature(audio_feature_txt,audio_feature_csv):
    with open(audio_feature_txt, "r", encoding="utf8") as f:
        lines = f.readlines()
        s = lines[391].split(',')
        s = s[1:-1] 
        s = np.array(s).reshape((1,len(s)))
        df = pd.DataFrame(s)
        for i in range(392,len(lines)):
            # print(i)
            t = lines[i].split(',')
            t = t[1:-1]
            t = np.array(t).reshape((1,len(t)))
            t = pd.DataFrame(t)
            df = pd.concat([df,t],ignore_index=True)
        df.to_csv(audio_feature_csv)

#将音频特征送入模型，得出结果
def audio_Model(audio_feature_csv):
    tcn = tf.keras.models.load_model('audio_1.h5',custom_objects={'TCN':TCN})

    df = pd.read_csv(audio_feature_csv,index_col=0)
    time_step = 50
    x_Test=[]
    j = 0
    while(j+time_step<df.shape[0]):
        x_Test.append(df.iloc[j:j+time_step,:])
        j = j+time_step

    X_TEST = [x.values for x in x_Test]
    X_TEST = np.array(X_TEST)

    a,b,c = X_TEST.shape[0],X_TEST.shape[1],X_TEST.shape[2]
    x_test_normal = X_TEST.reshape(-1,c)
    min_max_scaler = preprocessing.MinMaxScaler(feature_range = (-1,1))
    x_test_minmax=min_max_scaler.fit_transform(x_test_normal)
    x_test = x_test_minmax.reshape(a,b,c)

    predict = tcn.predict(x_test)
    x = np.min(predict)
    print("音频预测的结果")
    print(x)
    return x


if __name__ == '__main__':
    audio_path = 'H:/data/audio_feature/female_train_ND_feature/303_1.csv'
    
    # audio_Feature(audio_path)
    # Feature()
    # predict = audio_Model(audio_path)
