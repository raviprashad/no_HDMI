from flask import Flask, Response
import cv2
import numpy as np
import mss
import time

app = Flask(__name__)

def generate_frames():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # primary screen

        while True:
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            # Optional: resize for performance
            frame = cv2.resize(frame, (1280, 720))

            ret, buffer = cv2.imencode(
                '.jpg', frame,
                [int(cv2.IMWRITE_JPEG_QUALITY), 60]
            )

            if not ret:
                continue

            frame_bytes = buffer.tobytes()

            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'
                + frame_bytes +
                b'\r\n'
            )

            time.sleep(1 / 15)  # 15 FPS


@app.route('/')
def index():
    return '<h2>LAN Screen Cast</h2><img src="/video">'


@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
