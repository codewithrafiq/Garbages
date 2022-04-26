import cv2
import datetime


capture = cv2.VideoCapture(0)
def main():
    '''
    Video Write on the file
    '''
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'{datetime.datetime.now()}.mp4', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = capture.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    capture.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
