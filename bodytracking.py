'''
Bodytracking uses OpenCV and the Mediapipe ML pipeline to identify 33
points on the body through the webcam camera.
'''
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

class Body:
    '''
    Body will be used to generate and store the body landmarks.
    '''
    def __init__(self) -> None:
        pass
    # For webcam input:
    def tracking():
        '''
        Tracking returns a list of all of the body landmarks from webcam input.
        The location of a body landmark resembles the following:
        x: 0.410572350025177
        y: 3.420576333999634
        z: -0.6242696642875671
        visibility: 7.143011316657066e-05'
        '''
        cap = cv2.VideoCapture(0)
        with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                    continue
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)

                # Draw the pose annotation on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=
                    mp_drawing_styles.get_default_pose_landmarks_style())

                #Preallocate a list with default point values
                landmark_list = 32 * ['x: 0.410572350025177\
                                        y: 3.420576333999634 \
                                        z: -0.6242696642875671\
                                        visibility: 7.143011316657066e-05']
                for i in range(32):
                    if results.pose_landmarks:
                        landmark_list[i] = results.pose_landmarks.landmark
                    continue

            # Flip the image horizontally for a selfie-view display.
            #cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
            #if cv2.waitKey(5) & 0xFF == 27:
            #  break
                return landmark_list
        cap.release()

# 0 - nose
# 1 - left eye (inner)
# 2 - left eye
# 3 - left eye (outer)
# 4 - right eye (inner)
# 5 - right eye
# 6 - right eye (outer)
# 7 - left ear
# 8 - right ear
# 9 - mouth (left)
# 10 - mouth (right)
# 11 - left shoulder
# 12 - right shoulder
# 13 - left elbow
# 14 - right elbow
# 15 - left wrist
# 16 - right wrist
# 17 - left pinky
# 18 - right pinky
# 19 - left index
# 20 - right index
# 21 - left thumb
# 22 - right thumb
# 23 - left hip
# 24 - right hip
# 25 - left knee
# 26 - right knee
# 27 - left ankle
# 28 - right ankle
# 29 - left heel
# 30 - right heel
# 31 - left foot index
# 32 - right foot index
