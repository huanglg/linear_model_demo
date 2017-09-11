# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def get_data(file_name):
    data = pd.read_csv(file_name)
    x_parameter = []
    y_parameter = []

    for single_feet, single_price in zip(data['square_feet'], data['price']):
        x_parameter.append([float(single_feet)])
        y_parameter.append(float(single_price))

    print "x_parameter:", x_parameter, "y_parameter:", y_parameter
    return (x_parameter, y_parameter)


def linear_model_main(x_parameters, y_parameters, predict_value):
    object = linear_model.LinearRegression()
    object.fit(x_parameters, y_parameters)
    predict_output = object.predict(predict_value)

    predictions = {}
    predictions['intercept'] = object.intercept_
    predictions['coefficient'] = object.coef_
    predictions['predicted_value'] = predict_output

    return predictions


def get_predict_value():
    x, y = get_data("input_data.csv")
    test_feet = 700
    result = linear_model_main(x, y, test_feet)

    print "Intercept value:", result['intercept']
    print "coefficient:", result['coefficient']
    print "Predicted value:", result['predicted_value']


def show_linear_line():
    x, y = get_data("input_data.csv")

    object = linear_model.LinearRegression()
    object.fit(x, y)

    plt.scatter(x, y, color='blue')
    plt.plot(x, object.predict(x), color='red', linewidth=4)
    plt.show()



if __name__ == '__main__':
    get_predict_value()
    # show_linear_line()
