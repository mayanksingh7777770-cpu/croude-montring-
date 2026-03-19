
class LineCounter:
    def __init__(self, line_y):
        self.line_y = line_y
        self.counted = set()

    def check(self, track_id, center_y, prev_y):
        if track_id in self.counted:
            return False
        if prev_y < self.line_y <= center_y:
            self.counted.add(track_id)
            return True
        return False
