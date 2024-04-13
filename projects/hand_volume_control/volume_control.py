from hand_detection import HandDetection
import cv2 as cv, glob
import math
import alsaaudio

mixer = alsaaudio.Mixer()
# mixer.setvolume(70)  # Set volume to 70%
# mixer.setmute(0)    # Unmute the speaker


print(glob.glob("/dev/video?"))

def main():
    
    video = cv.VideoCapture(-1)
    hand_detection = HandDetection()

    while True:

        ret, frame = video.read()
        
        if ret:
            # flipping the frame 
            frame = cv.flip(frame, 1)


            frame = hand_detection.find_hands(frame)
            positions = hand_detection.get_hand_pos()
            
            if len(positions) > 22:
                # thumb, index -> left hand 
                # thumb2, index2 -> right hand 

                thumb, index = positions[21+4], positions[21+8]
                thumb2, index2 = positions[4], positions[8] 

                if thumb[0] < thumb2[0]:
                    thumb2, index2, thumb, index = thumb, index, thumb2, index2


                cv.circle(frame, thumb, 7, (255, 255, 255), -1)
                cv.circle(frame, index, 7, (255, 255, 255), -1)
                cv.line(frame, thumb, index, (255, 255, 255), 1)

                # cv.circle(frame, thumb2, 7, (0, 255, 255), -1)
                # cv.circle(frame, index2, 7, (0, 255, 255), -1)

                (x1, y1), (x2, y2) = thumb, index 
                (x3, y3), (x4, y4) = thumb2, index2 

                
                line_length = math.hypot((x1 - x2), (y1 - y2))
                line_length2 = math.hypot((x3 - x4), (y3 - y4))


                if line_length2 < 17:

                    cv.circle(frame, ((x4+x3) // 2, (y4+y3) //2), 7, (0, 255, 255), -1)

                    if line_length < 17:
                        cv.circle(frame, ((x1+x2)//2, (y1+y2)//2), 7, (0, 255, 255), -1)
                    elif line_length > 214:
                        cv.circle(frame, ((x1+x2)//2, (y1+y2)//2), 7, (0, 255, 255), -1)

                    min_vol_length = 20
                    max_vol_length = 120

                    percent = (line_length - min_vol_length) * 100 / max_vol_length
                    percent = 100 if percent >=100 else 0 if percent <= 0 else round(percent)

                    # print(f'Percentage: {percent}, line_length {line_length}')
                    mixer.setvolume(percent)


            cv.imshow('Hand Detection Video', frame)

            if cv.waitKey(1) & 0xFF == ord('a'):
                break 

    video.release()
    cv.destroyAllWindows()

main()