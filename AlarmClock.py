import time



class AlarmClock:
    def __init__(self):
        self.current_time = ''
        self.alarm_on = False
        self.alarm_time = ''

    def set_current_time(self):
        response = input('What time would you like to set?')
        self.current_time = response

    def check_time(self):
        print(f'The time is now {self.current_time}')

    def toggle_alarm(self):
        self.alarm_on = not self.alarm_on
        # if self.alarm_on:
        #     self.alarm_on = False
        # elif not self.alarm_on:
        #     self.alarm_on = True

    def set_alarm_time(self):
        response = input('What time would you like to set the alarm to?')
        self.alarm_time = response
        print(f'The alarm is now set for {self.alarm_time}')

    def check_alarm(self):
        if self.alarm_on:
            print(f'The alarm is set for {self.alarm_time}!')
        else:
            print('The alarm is not set!')

    def get_actual_time(self):
        time_of_day = time.localtime()
        self.current_time = time.strftime("%H:%M:%S", time_of_day)

