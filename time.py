
class Time:
    def __init__(self,start_time: str('10:00'), end_time: str ('19:00'), delta: str('0:30')):
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta

    def get_timeline(self):
        print('начало' + str(self.start_time), + 'конец'+ str(self.end_time), + 'промежуток' + str(self.delta))
        while(True):
            if self.start_time + self.delta:
                print(' нет свободного времени')
                break






















