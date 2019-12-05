from tqdm import tqdm

path1_instructions = []
path2_instruction = []
path1_points = []
path2_points = []
intersections = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    path1_instructions = [
        (
            instruction[0],
            int(instruction[1:])
        ) for instruction in lines[0].split(',')
    ]
    path2_instructions = [
        (
            instruction[0],
            int(instruction[1:])
        ) for instruction in lines[1].split(',')
    ]

current_x = 0
current_y = 0

for direction, distance in tqdm(path1_instructions):
    x_delta = 0
    y_delta = 0
    if direction == 'U':
        y_delta = -1
    elif direction == 'D':
        y_delta = 1
    elif direction == 'R':
        x_delta = 1
    elif direction == 'L':
        x_delta = -1

    for i in range(1, distance + 1):
        current_x += x_delta
        current_y += y_delta
        path1_points.append((current_x, current_y))

current_x = 0
current_y = 0
for direction, distance in tqdm(path2_instructions):
    x_delta = 0
    y_delta = 0
    if direction == 'U':
        y_delta = -1
    elif direction == 'D':
        y_delta = 1
    elif direction == 'R':
        x_delta = 1
    elif direction == 'L':
        x_delta = -1

    for i in range(1, distance + 1):
        current_x += x_delta
        current_y += y_delta
        coords = (current_x, current_y)
        path2_points.append((current_x, current_y))

        if coords in path1_points and coords != (0, 0):
            # print(coords)
            intersections.append(coords)

print("p1:", path1_points)
print("p2:", path2_points)
print("intersections:", intersections)

distances = [abs(point[0]) + abs(point[1]) for point in intersections]
print("dists:", distances)

print(f"Answer: {min(distances)}")
