
def robot_route(matrix):
    """
    Recieves matrix m x n and returns one dimension massive .
    
    :param matrix: matrix with size m x n
    """
    route = []
    if matrix:
        for m in range(len(matrix)):
            if m % 2 == 0:
                route.extend(matrix[m])
            else:
                route.extend(matrix[m][::-1])
            
    return route

x = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    ]

print(robot_route(x))

def robot_route_reversed(matrix):
    route = []
    if matrix:
        for m in reversed(range(len(matrix))): 
            if m % 2 == 0:
                route.extend(matrix[m])
            else:
                route.extend(matrix[m][::-1])
            
    return route

x = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

print(robot_route_reversed(x))
