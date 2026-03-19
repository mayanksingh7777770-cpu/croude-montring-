
class SimpleTracker:
    def __init__(self):
        self.next_id = 0

    def update(self, detections):
        tracks = []
        for det in detections:
            tracks.append((det, self.next_id))
            self.next_id += 1
        return tracks
