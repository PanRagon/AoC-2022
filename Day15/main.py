from test import test_input

sensors = test_input.split('\n')

for idx, sensor in enumerate(sensors):
    sensor = sensor.split(':')
    print(sensors[0])
    beacon_x = sensor[1].split('x=')[1]
    beacon_y = sensor[1].split('y=')[1]
    sensor_x = sensor[0].split('x=')[1]
    sensor_y = sensor[0].split('y=')[1]
    print(beacon_x)