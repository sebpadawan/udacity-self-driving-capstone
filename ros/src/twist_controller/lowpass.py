
class LowPassFilter(object):
    def __init__(self, tau, ts):
        # First order low pass filter
        self.a = 1. / (tau / ts + 1.) # Input contribution
        self.b = tau / ts / (tau / ts + 1.); # Inertia contribution

        self.last_val = 0.
        self.ready = False

    def get(self):
        return self.last_val

    def filt(self, val):
        if self.ready:
            val = self.a * val + self.b * self.last_val
        else:
            self.ready = True

        self.last_val = val
        return val
