from flask import Flask, Response, jsonify, request
import cv2 as cv
import mediapipe as mp
import numpy as np
from flask_cors import CORS
import threading
import time

app = Flask(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6)

CORS(app)

recording = False
out = None
selected_exercise = 'exercise1'

# variables for the actual counting of exercise
counter = 0
stage = None

def stop_recording_after_delay(delay):
    global recording, out
    time.sleep(delay)
    recording = False
    if out is not None:
        out.release()
        out = None

def generate_frames():
    
    
    
    
    
    
    
    
    def exercise1():
        global counter, stage  # Declare counter and stage as global variables
        try:
            def calculate_angle(a, b, c):
                a = np.array(a)
                b = np.array(b)
                c = np.array(c)
                
                radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
                angle = np.abs(radians * 180 / np.pi)
                
                if angle > 180:
                    angle = 360 - angle
                    
                return angle

            landmarks = results.pose_landmarks.landmark
            
            # FINDING THE COORDINATES
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            # finding the angle
            angle = calculate_angle(hip, knee, ankle)
            
            # putting it onto the opencv
            cv.putText(image, str(angle),
                       tuple(np.multiply(knee, [640, 480]).astype(int)),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, [255, 255, 255], 2, cv.LINE_AA)
            
            # counting logic
            if angle > 160:
                stage = "down"
            if angle < 120 and stage == "down":
                stage = "up"
                counter += 1
                print(counter)
                
            cv.rectangle(image, (0,0), (225, 73), (245, 117, 16), -1)
            
            cv.putText(image, 'REPS', (15,12),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                       )
            cv.putText(image, str(counter),
                       (10,60),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                       )
            
            cv.putText(image, 'STAGE', (65,12),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                       )
            cv.putText(image, stage,
                       (60,60),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                       )
        except:
            pass
        
        
        
        
        
        
        
        
    def exercise2():
        global counter, stage  # Declare counter and stage as global variables
        try:
            def calculate_angle(a, b, c):
                a = np.array(a)
                b = np.array(b)
                c = np.array(c)
                
                radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
                angle = np.abs(radians * 180 / np.pi)
                
                if angle > 180:
                    angle = 360 - angle
                    
                return angle

            landmarks = results.pose_landmarks.landmark
            
            # FINDING THE COORDINATES
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            # finding the angle
            angle = calculate_angle(hip, knee, ankle)
            
            # putting it onto the opencv
            cv.putText(image, str(angle),
                    tuple(np.multiply(knee, [640, 480]).astype(int)),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, [255, 255, 255], 2, cv.LINE_AA)
            
            # counting logic
            if angle < 100:
                stage = "down"
            if angle > 120 and stage == "down":
                stage = "up"
                counter += 1
                print(counter)
                
            cv.rectangle(image, (0,0), (225, 73), (245, 117, 16), -1)
            
            cv.putText(image, 'REPS', (15,12),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                    )
            cv.putText(image, str(counter),
                    (10,60),
                    cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                    )
            
            cv.putText(image, 'STAGE', (65,12),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                    )
            cv.putText(image, stage,
                    (60,60),
                    cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                    )
        except:
            pass
    
    
    
    
    
    
    
    
    def exercise3():
        global counter, stage  # Declare counter and stage as global variables
        try:
            def calculate_angle(a, b, c):
                a = np.array(a)
                b = np.array(b)
                c = np.array(c)
                
                radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
                angle = np.abs(radians * 180 / np.pi)
                
                if angle > 180:
                    angle = 360 - angle
                    
                return angle

            landmarks = results.pose_landmarks.landmark
            
            # FINDING THE COORDINATES
            foot = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x, landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            # finding the angle
            angle = calculate_angle(hip, knee, ankle)
            
            # putting it onto the opencv
            cv.putText(image, str(angle),
                    tuple(np.multiply(knee, [640, 480]).astype(int)),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, [255, 255, 255], 2, cv.LINE_AA)
            
            # counting logic
            if angle > 160:
                stage = "down"
            if angle < 120 and stage == "down":
                stage = "up"
                counter += 1
                print(counter)
                
            cv.rectangle(image, (0,0), (225, 73), (245, 117, 16), -1)
            
            cv.putText(image, 'REPS', (15,12),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                    )
            cv.putText(image, str(counter),
                    (10,60),
                    cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                    )
            
            cv.putText(image, 'STAGE', (65,12),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA
                    )
            cv.putText(image, stage,
                    (60,60),
                    cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA
                    )
        except:
            pass
    
    
    
    
    
    
    
    
    
    

    global recording, out, selected_exercise
    camera = cv.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Recoloring to RGB
            image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Make the detection
            results = pose.process(image)
            
            # Recoloring back into BGR
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            
            exercise3()
            
            if selected_exercise == 'exercise1':
                cv.putText(image, 'Bed Supported Knee Nend', (image.shape[1] // 2 - 200, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
                exercise1()
                
            elif selected_exercise == 'exercise2':
                cv.putText(image, 'Sitting Supported Knee Bend', (image.shape[1] // 2 - 200, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
                exercise2()
                
            elif selected_exercise == 'exercise3':
                cv.putText(image, 'Ankle Pump', (image.shape[1] // 2 - 200, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
                exercise3()
            
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    # changing colors
                                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
            
            if recording and out is not None:
                out.write(image)
                cv.putText(image, 'Recording...', (10, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)  # Moved to bottom left
            else:
                cv.putText(image, 'Not Recording', (10, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)  # Moved to bottom left
            
            ret, buffer = cv.imencode('.jpg', image)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Connected! Get ready to work out!",
    })

@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording, out, selected_exercise
    data = request.get_json()
    selected_exercise = data.get('exercise', 'exercise1')
    if not recording:
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
        recording = True
        threading.Thread(target=stop_recording_after_delay, args=(10,)).start()
    return jsonify({'message': 'Recording started', 'exercise': selected_exercise})

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, port=8080)