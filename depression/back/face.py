import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
import tensorflow as tf
from tcn import TCN

#通过openFace提取面部特征
def video_feature(video_path):
    path = 'cd /d H:/OpenFace_2.2.0_win_x64 && FeatureExtraction.exe -f ' + video_path + ' -2Dfp'
    os.system(path)

#提取HDR特征
def HDR(video_new_path,HDR_path):
    m=[10,20,30,40,50]
    df = pd.read_csv(video_new_path)
    x0 = 5
    y0 = 73
    l=[]
    for i in range(4080):
        l.append(i)
    l = np.array(l).reshape((1,len(l)))
    df1 = pd.DataFrame(l)
    for i in range(0,df.shape[0]-101,10):#每一帧
        lines = []
        print(i)
        for j in range(len(m)):#每一个时间间隔
            for k in range(0,68):#每一对(x,y)
                a,b = i+m[j],i
                r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12 = 0,0,0,0,0,0,0,0,0,0,0,0
                num=0
                while(a<=i+100):
                    x = float(df.iloc[a][x0+k]-df.iloc[b][x0+k])
                    y = float(df.iloc[a][y0+k]-df.iloc[b][y0+k])
                    b = b + 10
                    a = b + m[j]
                    if(x<-20):
                        r1=r1+1
                    elif(x>=-20 and x<-10):
                        r2=r2+1
                    elif(x>=-10 and x<0):
                        r3 = r3+1
                    elif(x>=0 and x<10):
                        r4 = r4+1
                    elif(x>=10 and x<20):
                        r5 = r5+1
                    else:
                        r6=r6+1
                    if(y<-20):
                        r7=r7+1
                    elif(y>=-20 and y<-10):
                        r8=r8+1
                    elif(y>=-10 and y<0):
                        r9 = r9+1
                    elif(y>=0 and y<10):
                        r10 = r10+1
                    elif(y>=10 and y<20):
                        r11 = r11+1
                    else:
                        r12=r12+1
                    num = num+1
                r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12 = r1/num,r2/num,r3/num,r4/num,r5/num,r6/num,r7/num,r8/num,r9/num,r10/num,r11/num,r12/num
                lines.append(r1)
                lines.append(r2)
                lines.append(r3)
                lines.append(r4)
                lines.append(r5)
                lines.append(r6)
                lines.append(r7)
                lines.append(r8)
                lines.append(r9)
                lines.append(r10)
                lines.append(r11)
                lines.append(r12)
        lines = np.array(lines).reshape((1,len(lines)))
        df2 = pd.DataFrame(lines)
        df1 = pd.concat([df1,df2],ignore_index=True)    
    df1 = df1[1:]
    df1.to_csv(HDR_path)

#将HDR特征送入模型中的出结果
def video_Model(HDR_path):
    tcn = tf.keras.models.load_model('H:/depression_system/vidio_1.h5',custom_objects={'TCN':TCN})
    df = pd.read_csv(HDR_path,index_col=0)
    time_step = 10

    x_Test=[]
    j = 0
    while(j+time_step<df.shape[0]):
        x_Test.append(df.iloc[j:j+time_step,:])
        j = j+time_step

    X_TEST = [x.values for x in x_Test]
    x_test = np.array(X_TEST)
    # a,b,c = X_TEST.shape[0],X_TEST.shape[1],X_TEST.shape[2]
    # x_test_normal = X_TEST.reshape(-1,c)
    # min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
    # x_test_minmax=min_max_scaler.fit_transform(x_test_normal)
    # x_test = x_test_minmax.reshape(a,b,c)

    predict = tcn.predict(x_test)
    print("面部预测结果")
    for i in range(len(predict)):
        print(predict[i])
    x = np.min(predict)
    print(x)
    return x



if __name__ == '__main__':
    # video_path ='H:\\data\\vidio_feature\\female_train_D_feature\\320_6.csv'
    out_path = 'H:/depression_system/video/32022-04-29_video.mp4'
    # print(video_path)
    video_feature(out_path)
    # print(1)
    # HDR(video_path,out_path)
    # video_Model(video_path)





