
import cv2
import asyncio
from services.detection import PersonDetector
from services.tracker import SimpleTracker
from services.line_counter import LineCounter

class CameraWorker:
    def __init__(self, rtsp_url, line_y=300):
        self.cap = cv2.VideoCapture(rtsp_url)
        self.detector = PersonDetector()
        self.tracker = SimpleTracker()
        self.line_counter = LineCounter(line_y)
        self.count = 0

    async def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                await asyncio.sleep(1)
                continue

            detections = self.detector.detect(frame)
            tracks = self.tracker.update(detections)

            for det, tid in tracks:
                x1, y1, x2, y2, _ = det
                center_y = (y1 + y2) / 2
                if self.line_counter.check(tid, center_y, y1):
                    self.count += 1

            await asyncio.sleep(0)
