import numpy as np

fuel_grid = 300
serial_num = 7672
largest_fuel = 0
largest_fuel_x = 0
largest_fuel_y = 0

matrix = np.zeros((300, 300), dtype='int32')
for x in range(0, 300, 1):
    for y in range(0, 300, 1):
        # if not y + 2 > 300 and not x + 2 > 300:
        #     power_level = 0
        #     for x2 in range(0, 3, 1):
        #         for y2 in range(0, 3, 1):
        #             rack_id = x2 + x + 10
        #             power = rack_id * (y2 + y)
        rack_id = x + 1 + 10
        power = rack_id * (y + 1)
        power += serial_num
        power = power * rack_id
        # print(str(power)[len(str(power))-3])
        matrix[x, y] = int(str(power)[len(str(power))-3]) - 5
        # if power_level > largest_fuel:
        #     largest_fuel = power_level
        #     largest_fuel_x = x
        #     largest_fuel_y = y

print("filled Matrix")
# find largest matrix within our new matrix
previous = [0, 0]
current = matrix[0]
largest_matrix = [0, 0]
for x in range(0, 299, 1):
    previous = current
    current = [300]
    for y in range(0, 299, 1):
        span = 1
        if x > 0:
            span = 1 + min(current[x - 1], min(previous[x], previous[x - 1]))
            print("span: ", span)
        if span > len(largest_matrix):
            print("span larger: ", span)
            largest_matrix = matrix[x - span + 1, y - span + 1]
        current[x] = span

print(largest_matrix)
# print("x,y", largest_fuel_x, largest_fuel_y, " power: ", largest_fuel)