from flask import Flask,request,session
import json
from flask_cors import CORS
from config import UPDATE_PATH_AUDIO, UPDATE_PATH_VIDEO
from extract_audio import extract_Audio,audio_capture
import os
# from flask_login import LoginManager, UserMixin,login_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import datetime
from video_capture import video_capture
from audio import audio_Feature,Feature,audio_Model
from face import video_feature,HDR,video_Model

app = Flask(__name__) #创建Flask类的实例，第一个参数是模块或者包的名称

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


app.config['JSON_AS_ASCII']=False # 支持中文显示
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app, supports_credentials=True)

db = SQLAlchemy(app,use_native_unicode='utf8')


class User( db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),nullable=True)
    # historys = db.relationship("History",backref = 'user')

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class History(db.Model):
    __tablename__ = 'history'
    hid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # uid = db.Column(db.Integer,nullable=False)
    time = db.Column(db.String(200),nullable=False)
    score = db.Column(db.Integer,nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    # u = db.relationship('User', back_populates='historys')

    def __init__(self,uid,time,score):
        self.uid = uid
        self.time = time
        self.score = score


@app.route('/login', methods=['POST','GET'])
def login_post():
    username = request.form.get("username")
    print(username)
    password = request.form.get("password")
    print("password"+password)
    if username == "" or password == "":
        print('用户名和密码不能为空！！！')
        data = {'code': 401, 'data': '', 'msg': 'username or password can not null'}
        return json.dumps(data)
    user = User.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        print('用户名或密码错误！！！')
        data = {'code': 401, 'data': '', 'msg': 'username or password is wrong'}
        return json.dumps(data)
    session['user_id'] = user.id
    print('login success')
    data = {'code': 200, 'data': user.id, 'msg': 'login success'}
    return json.dumps(data)

@app.route('/register', methods=['POST','GET'])
def register_post():
    username = request.form.get("username")
    password = request.form.get("password")
    repassword = request.form.get("repassword")
    email = request.form.get("email")
    
    if username == "" or password == "":
        print('用户名和密码不能为空！！！')
        data = {'code': 401, 'data': '', 'msg': 'username or password can not null'}
        return json.dumps(data)
    if password != repassword:
        print('两次密码不一致！！！')
        data = {'code': 401, 'data': '', 'msg': 'password is not equal to repassword'}
        return json.dumps(data)
    user = User.query.filter_by(username=username).first()
    if user is not None:
        print('用户名重复！！！')
        data = {'code': 401, 'data': '', 'msg': 'user is existe'}
        return json.dumps(data)
    user = User(username=username,password=password,email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    data = {'code': 200, 'data': '', 'msg': 'register success'}
    return json.dumps(data)

@app.route('/history',methods=['POST','GET'])
def history():

    user_id = session['user_id']
    historys = History.query.filter(History.uid==user_id).all()

    if historys is None:
        data = {'code': 401, 'data': '', 'msg': 'historys is not existe'}
        return json.dumps(data)
    else:
        print('----------------------')
        print(type(historys))
        y=[]
        z=[]
        x=dict()
        j=0
        for i in historys:
            y.append(str(i.time))
            z.append(str(i.score))
        x['score']=z
        x['time']=y
        data = {'code': 200, 'data':x ,'msg': 'historys success'}
        return json.dumps(data)
    


@app.route('/Score', methods=['POST','GET']) # 使用methods参数处理不同HTTP方法
def GetScore():
      score = request.args.get('Score')
      session['score'] = score
      data = {'code': 200, 'data':'', 'msg': 'Score success'}
      return json.dumps(data)

@app.route('/video', methods=['POST','GET'])
def GetVideo():
      data = request.files
      file = data['file']
      Time = datetime.datetime.now().strftime('%Y-%m-%d')
      id = session['user_id']
      name = str(id)+Time
      video_path = UPDATE_PATH_VIDEO+name+'_'+'video.mp4'
      file.save(video_path)
    #   video_feature_path = UPDATE_PATH_VIDEO+name+'_'+'video_capture.mp4'
      timestart = session['st']
      timeend = session['et']
      
      audio_path = UPDATE_PATH_AUDIO+name+"audio.wav"
      print("现在正在分离音频...")
      extract_Audio(video_path,audio_path)
      print("分离音频结束...")
      print("现在正在截取音频...")
      audio_capture_path = UPDATE_PATH_AUDIO+name+'audio_capture.wav'
      audio_capture(audio_path,audio_capture_path,timestart,timeend)



    #   print("现在正在截取视频...")
    # #   video_capture(timestart,timeend,video_path,video_feature_path)
    #   print("截取视频结束...")


      
      #音频
      audio_feature_txt = UPDATE_PATH_AUDIO+name+'audio_feature.txt'
      print("现在正在获得音频txt文件...")
      audio_Feature(audio_capture_path,audio_feature_txt)
      print("获得音频txt文件结束...")
      audio_feature_csv = UPDATE_PATH_AUDIO+name+'audio_feature.csv'
      print("现在正在获得音频csv文件...")
      Feature(audio_feature_txt,audio_feature_csv)
      print("获得音频csv文件结束...")
      print("现在正在跑音频模型...")
      audioScore = audio_Model(audio_feature_csv)
      print("跑音频模型结束...")
      
      #面部
      print("现在正在获得面部初始文件...")
      video_feature(video_path)
      print("获得面部初始文件结束...")
      video_new_path = 'H:/OpenFace_2.2.0_win_x64/processed/'+name+'_'+'video.csv'
      HDR_path = 'H:/depression_system/video/'+ name+'_'+'video_capture.csv'
      print("现在正在获得面部HDR文件...")
      HDR(video_new_path,HDR_path)
      print("获得面部HDR文件结束...")
      print("现在正在视频频模型...")
      videoScore = video_Model(HDR_path)
      print("视频频模型结束...")
      #决策融合
      Score = session['score']
      score = (float(audioScore)+float(videoScore))/2*0.5+float(Score)*0.5
      print("最终的结果"+str(score))
      history = History(uid=id,time=Time,score = score)
      db.session.add(history)
      db.session.commit()
      data = {'code': 200, 'data':score, 'msg': 'Video success'}
      return json.dumps(data)

@app.route('/Time', methods=['POST','GET']) # 使用methods参数处理不同HTTP方法
def GetTime():

    timeBegin = request.args.get('timeBegin')
    session['st'] = int(int(timeBegin)/1000)
    print(timeBegin)
    timeEnd = request.args.get('timeEnd')
    session['et'] = int(int(timeEnd)/1000)
    print(timeEnd)
    data = {'code': 200, 'data':'', 'msg': 'Time success'}
    return json.dumps(data)


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    if os.path.exists('db/db.db'):
        pass
    else:
        db.create_all()
    app.run(host='0.0.0.0')
    