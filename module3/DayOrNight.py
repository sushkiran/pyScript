import time

'''
Weather forecasting organization wants to show is it day or night. So, write a
program for such organization to find whether is it dark outside or not.
Hint: Use time module.
'''


def set_time(hour, mins, sec):
    t = time.localtime()
    return t.tm_year, t.tm_mon, t.tm_mday, hour, mins, sec, t.tm_wday, t.tm_yday, t.tm_isdst


now = time.ctime()
sunrise = time.asctime(set_time(6, 0, 0))
sunset = time.asctime(set_time(19, 20, 0))

print(sunrise, '-- Sunrise')
print(now, '-- Now')
print(sunset, '-- Sunset')

if sunrise < now < sunset:
    print('it is a day')
else:
    print('it is a night')
