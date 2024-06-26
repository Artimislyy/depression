import cv2

def video_capture(startTime,endTime,video_path,out_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("width:",width, "height:", height,'frames:',frames,'fps:',fps)
    out = cv2.VideoWriter(out_path, fourcc,fps, (width, height))

    video_length = frames / fps
    print(video_length)

    pos = 1*fps
    while (pos <= 40 * fps):
        print(pos)
        ret, frame = cap.read()  # 捕获一帧图像
        out.write(frame)  # 保存帧
        pos=pos+1

    cap.release()
    out.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    video_path = 'H:/depression_system/video/12022-04-29_video_capture.mp4'
    out_path = 'H:/depression_system/video/42022-04-29_video_fff.mp4'
    # video_capture(3,20,video_path,out_path)
    # path = 'H:/depression_system/video/video_cap.mp4'
    # video_capture(1,10,video_path,path)
    # HDR()
    # video_Model()