import matplotlib.pyplot as plt
import numpy as nmp
import math


class LinearRegression:
    def __init__(self, data_set):
        self.data_set = data_set

    def __calc_slope_and_b(self):
        if len(self.data_set) == 0:
            return "The given data set is empty or the data set has different number of x and y values"

        total_x_values = 0
        total_y_values = 0
        total_xy_values = 0
        total_x_seq_values = 0
        x_amount = len(self.data_set)

        for i in range(len(self.data_set)):
            total_x_values += self.data_set[i][0]
            total_y_values += self.data_set[i][1]
            total_xy_values += self.data_set[i][0] * self.data_set[i][1]
            total_x_seq_values += self.data_set[i][0] ** 2

        slope_term_1 = (x_amount * total_xy_values) - (total_x_values * total_y_values)
        slope_term_2 = x_amount * total_x_seq_values - total_x_values**2
        slope = slope_term_1 / slope_term_2
        b_value = (total_y_values - slope * total_x_values) / (x_amount)

        return (slope, b_value)

    def calc_one_point(self, x_point):
        slope, b_value = self.__calc_slope_and_b()
        y_value = slope * x_point + b_value
        return y_value

    def calc_set_of_points(self, x_points):
        y_values = []
        slope, b_value = self.__calc_slope_and_b()
        for i in range(len(x_points)):
            y_value = slope * x_points[i] + b_value
            y_values.append(round(y_value, 4))

        return y_values

    def graph(self, x_points):
        y_points = self.calc_set_of_points(x_points)
        x_values = [data_set[i][0] for i in range(len(data_set))]
        y_values = [data_set[i][1] for i in range(len(data_set))]

        plt.plot(x_points, y_points)
        plt.scatter(x_values, y_values)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("linear regression")
        plt.show()


# This class poly will solve only polynomial of second degree
# Later on I will make it more dynamic to solve higher poly degrees
class PolynomialRegression:
    def __init__(self, data_set):
        self.data_set = data_set

    def __calc_coeff(self):
        if len(self.data_set) == 0:
            return "The given data set is empty or the data set has different number of x and y values"
        matrix = []
        vector = []

        n = len(data_set)
        total_y_values = 0
        total_x_values = 0
        total_x_2_values = 0
        total_x_3_values = 0
        total_x_4_values = 0
        total_x_2y_values = 0
        total_x_y_values = 0

        for i in range(len(data_set)):
            total_y_values += data_set[i][1]
            total_x_values += data_set[i][0]
            total_x_2_values += data_set[i][0] ** 2
            total_x_3_values += data_set[i][0] ** 3
            total_x_4_values += data_set[i][0] ** 4
            total_x_2y_values += (data_set[i][0] ** 2) * (data_set[i][1])
            total_x_y_values += data_set[i][0] * data_set[i][1]

        matrix.append([n, total_x_values, total_x_2_values])
        vector.append(total_y_values)

        matrix.append([total_x_values, total_x_2_values, total_x_3_values])
        vector.append(total_x_y_values)

        matrix.append([total_x_2_values, total_x_3_values, total_x_4_values])
        vector.append(total_x_2y_values)
        coeffs = nmp.linalg.solve(matrix, vector)

        return coeffs

    def calc_one_point(self, x_point):
        coeffs = self.__calc_coeff()
        y = (coeffs[0] * x_point**2) + coeffs[1] * x_point + coeffs[2]

        return y

    def calc_set_of_points(self, x_points):
        coeffs = self.__calc_coeff()
        y_values = []
        for i in range(len(x_points)):
            y_point = self.calc_one_point(x_points[i])
            y_values.append(y_point)

        return y_values

    def graph(self, x_points):
        y_points = self.calc_set_of_points(x_points)
        x_values = [data_set[i][0] for i in range(len(data_set))]
        y_values = [data_set[i][1] for i in range(len(data_set))]

        plt.plot(x_points, y_points)
        plt.scatter(x_values, y_values)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("polynomial regression")
        plt.show()


class ExponentialRegression:
    def __init__(self, data_set):
        self.data_set = data_set

    def __calc_b_a_values(self):
        if len(self.data_set) == 0:
            return "The given data set is empty or the data set has different number of x and y values"

        total_x_hat = 0
        total_z_hat = 0
        data_set_len = len(self.data_set)

        for i in range(data_set_len):
            self.data_set[i].append(round(math.log(data_set[i][1]), 3))

            total_x_hat += self.data_set[i][0]
            total_z_hat += self.data_set[i][2]

        total_x_hat /= data_set_len
        total_z_hat /= data_set_len

        numerator = 0
        denominator = 0
        for i in range(data_set_len):
            x = self.data_set[i][0]
            z = self.data_set[i][2]

            numerator += (z) * (x - total_x_hat)
            denominator += (x) * (x - total_x_hat)

        b = numerator / denominator
        a = total_z_hat - (total_x_hat * b)
        return (b, a)

    def calc_one_point(self, x_point):
        b, a = self.__calc_b_a_values()
        new_a = math.e**a
        y = new_a * (math.e ** (b * x_point))
        return round(y, 3)

    def calc_set_of_points(self, x_points):
        y_values = []
        b, a = self.__calc_b_a_values()
        new_a = math.e**a
        for i in range(len(x_points)):
            y = new_a * (math.e ** (b * x_points[i]))
            y_values.append(round(y, 3))

        return y_values

    def graph(self, x_points):
        y_points = self.calc_set_of_points(x_points)
        x_values = [data_set[i][0] for i in range(len(data_set))]
        y_values = [data_set[i][1] for i in range(len(data_set))]

        plt.plot(x_points, y_points)
        plt.scatter(x_values, y_values)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("polynomial regression")
        plt.show()


if __name__ == "__main__":
    x_values = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y_values = [7.5, 16.1, 38.9, 67.0, 146.6, 266.2]

    data_set = [[x_values[i], y_values[i]] for i in range(len(x_values)) if len(x_values) == len(y_values)]

    required_point = 1.2
    required_points = [round(0 + 0.1 * i, 4) for i in range(32 * 2)]

    lr = LinearRegression(data_set)
    pr = PolynomialRegression(data_set)
    er = ExponentialRegression(data_set)
