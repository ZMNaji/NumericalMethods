import matplotlib.pyplot as plt


# Function that will use cramer's rule to solve the k values
def solve_uing_carmer_rule(matrix, vector):
    # Define the matrix and vector as lists

    # Calculate the determinant of the matrix
    def determinant(matrix):
        return (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )

    solutions = []
    for i in range(len(vector)):
        modified_matrix = [row[:] for row in matrix]
        for j in range(len(vector)):
            modified_matrix[j][i] = vector[j]
        det = determinant(modified_matrix)
        solutions.append(round(det / determinant(matrix), 4))

    return solutions


# Function that will return k values for specific data_set
def return_k_values(data_set):
    k_exp = [0, 1, 1, 1, 0]
    results = []
    expressions = []
    x_values = [data_set[i][0] for i in range(len(data_set))]
    y_values = [data_set[i][1] for i in range(len(data_set))]

    # For loop to create k_equations
    for i in range(len(data_set)):
        if 0 < i < len(data_set) - 1:
            x1, x2, x3 = x_values[i - 1], x_values[i], x_values[i + 1]
            y1, y2, y3 = y_values[i - 1], y_values[i], y_values[i + 1]

            # I used this if statement to prevent division by zero errors
            if x1 == x2 or x2 == x3:
                continue

            expressions.append([0, 0, 0, 0, 0])
            for j in range(3):
                match j:
                    case 0:
                        k = k_exp[i - 1]
                        exp = x1 - x2
                        expressions[-1][i - 1] = k * exp
                    case 1:
                        k = k_exp[i]
                        exp = 2 * (x1 - x3)
                        expressions[-1][i] = k * exp
                    case 2:
                        k = k_exp[i + 1]
                        exp = x2 - x3
                        expressions[-1][i + 1] = k * exp

            result = 6 * (((y1 - y2) / (x1 - x2)) - ((y2 - y3) / (x2 - x3)))
            results.append(round(result, 2))

    # the following for loop is fo getting rid for the zero values for the first and last k
    for i in range(len(expressions)):
        expressions[i].pop(0)
        expressions[i].pop(-1)

    k_values_array = solve_uing_carmer_rule(expressions, results)

    k_values_array.append(0)
    k_values_array.insert(0, 0)
    return k_values_array


# This function will be used mutliple times and will return one interpolation point base on the required x value
def return_cubic_spline_point(k_values, data_set, x):
    point1 = 0
    point2 = 0
    x_values = [data_set[i][0] for i in range(len(data_set))]
    y_values = [data_set[i][1] for i in range(len(data_set))]

    for i in range(len(x_values)):
        if x < x_values[0] or x > x_values[-1]:
            return "the required point is outside the give data set x values intervals"

        if x == x_values[i]:
            return y_values[i]

        if x_values[i] < x < x_values[i + 1]:
            point1 = i
            point2 = i + 1

    point_result = (
        -(k_values[point1] / 6) * ((x * x_values[point2]) ** 3 - (x - x_values[point2]))
        + (k_values[point2] / 6) * ((x - x_values[point1]) ** 3 - (x - x_values[point1]))
        - (y_values[point1] * (x - x_values[point2]) - y_values[point2] * (x - x_values[point1]))
    )

    term1 = (k_values[point1] / 6) * (
        (((x - x_values[point2]) ** 3) / (x_values[point1] - x_values[point2]))
        - ((x - x_values[point2]) * (x_values[point1] - x_values[point2]))
    )

    term2 = -(k_values[point2] / 6) * (
        (((x - x_values[point1]) ** 3) / (x_values[point1] - x_values[point2]))
        - ((x - x_values[point1]) * (x_values[point1] - x_values[point2]))
    )

    term3 = (y_values[point1] * (x - x_values[point2]) - y_values[point2] * (x - x_values[point1])) / (x_values[point1] - x_values[point2])

    point_result2 = term1 + term2 + term3

    return point_result2


# This function will call the return_cubic_spline_point function mutliple times to return mutliple points
def return_cubic_spline_points(k_values, data_set, required_points):
    points_list = []
    for i in range(len(required_points)):
        single_point = return_cubic_spline_point(k_values, data_set, required_points[i])
        points_list.append(round(single_point, 3))

    return points_list


def draw_graph(required_points, spline_points):
    plt.plot(required_points, spline_points)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("cubic spline interpolation graph")
    plt.show()


if __name__ == "__main__":
    x_values = [2, 4, 7, 8, 10]
    y_values = [1.5, 4.5, 9.3, 6.4, 8.5]
    data_set = [[x_values[i], y_values[i]] for i in range(len(x_values))]
    required_points = [round(2 + 0.02 * i, 2) for i in range(400)]
    k_values = return_k_values(data_set)
    print(required_points)
    print("----------------------------------------------")
    spline_points = return_cubic_spline_points(k_values, data_set, required_points)
    draw_graph(required_points, spline_points)
