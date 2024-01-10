import cv2 as cv
import time
from utils import CvFpsCalc

def main():
    # Variables for FPS calculation
    cap = cv.VideoCapture(1, cv.CAP_DSHOW)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    print(cap.get(cv.CAP_PROP_FPS))
    frame_count = 0
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process frame here

        frame_count += 1
        cv.imshow('Frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Calculate FPS
    end_time = time.time()
    elapsed_time = end_time - start_time
    fps = frame_count / elapsed_time
    print(f"FPS: {fps:.2f}")

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()