class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f'{hh}:{mm}:{ss}'

    def next_second(self):
        self.seconds += 1
        if self.seconds >= Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= Time.max_hours:
                    self.hours = 0

        return self.get_time()




time = Time(9, 30, 60)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(24, 59, 59)
print(time.next_second())
