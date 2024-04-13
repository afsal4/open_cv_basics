import cv2 as cv
import mediapipe as mp 
import time



class HandDetection:

    # hands instance in mediapipe 
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # drawing utility in media pipe 
    mp_draw = mp.solutions.drawing_utils

    tmp_img_shape = None
    tmp_multi_land_mark = None




    def find_hands(self, frame, hand_points=[], no_hands = 2, draw=True):
        self.tmp_img_shape = frame.shape
        self.tmp_land_mark = []

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        res = self.hands.process(rgb_frame)

        if res.multi_hand_landmarks:

            for hand in res.multi_hand_landmarks:
                    
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)
                
            self.tmp_land_mark = res.multi_hand_landmarks

        return frame


    def get_hand_pos(self):
        h, w, c = self.tmp_img_shape
        position = []

        for hand in self.tmp_land_mark:
            for id, lm in enumerate(hand.landmark):
                point = (int(lm.x*w), int(lm.y*h))
                position.append(point)

        return position

        
        
if __name__ == '__main__':
    video = cv.VideoCapture(-1)

    prev_time = time.time()

    hand_detection = HandDetection()

    while True:

        ret, frame = video.read()

        frame = hand_detection.find_hands(frame)
        hand_positions = hand_detection.get_hand_pos()
        if len(hand_positions) > 0:

            frame = cv.circle(frame, hand_positions[0], 25, (255, 255, 255), -1)
    
        # calculating time per frames
        cur_time = time.time()
        fps = cur_time - prev_time
        prev_time = cur_time

        # printing time taken per frame on screen 
        cv.putText(frame, f'{fps:.2f}', (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1, 255, 3)
        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xff == ord('a'):
            break

    video.release()
    cv.destroyAllWindows()
