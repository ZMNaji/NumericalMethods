# This function could be used whenever we want to get a one value of the interpolation.
def find_lag_interpolation(data_set, x_value):
    result = 0
    for i in range(len(data_set)):
        y_value = data_set[i][1]
        lx = 1
        for j in range(len(data_set)):
            if i != j:
                lx *= (x_value - data_set[j][0]) / (data_set[i][0] - data_set[j][0])

        current = y_value * lx
        result += current

    return round(result, 2)


# This function could be used whenever we want to get a mutliple values of our the interpolation
def find_set_of_lag_interpolation(data_set, required_points):
    point_values = []
    for point in required_points:
        current_point = find_lag_interpolation(data_set, point)
        point_values.append(current_point)

    return point_values


if __name__ == "__main__":
    x_values = [2, 4, 7, 8, 10]
    y_values = [1.5, 4.5, 9.3, 6.4, 8.5]
    one_point = 0
    set_of_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

    data_set = [[x, y] for x, y in zip(x_values, y_values)]

    print(find_lag_interpolation(data_set, one_point))
    print("")
    print(find_set_of_lag_interpolation(data_set, set_of_points))
