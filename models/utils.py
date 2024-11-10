import pickle
import json
import numpy as np
import pandas as pd
import config  # Assuming you have a config file to store paths

class Auto():
    def __init__(self, length, curb_weight, engine_size, city_mpg, highway_mpg, make, drive_wheels, num_of_cylinders):
        # Initializing the attributes with the provided values
        self.length = length
        self.curb_weight = curb_weight
        self.engine_size = engine_size
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.make = "make_" + str(make)  # Assuming make is a categorical variable
        self.drive_wheels = "drive-wheels_" + str(drive_wheels)  # Assuming drive wheels is categorical
        self.num_of_cylinders = "num-of-cylinders_" + str(num_of_cylinders)  # Assuming num_of_cylinders is categorical

    def load_model(self):
        # Loading the model and JSON metadata
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        # Loading the model and JSON metadata
        self.load_model()

        # Retrieving the column indexes for categorical features
        make_index = self.json_data['columns'].index(self.make)
        drive_wheels_index = self.json_data['columns'].index(self.drive_wheels)
        num_of_cylinders_index = self.json_data['columns'].index(self.num_of_cylinders)

        # Preparing the input array
        array = np.zeros(len(self.json_data['columns']))  # Creating an array of zeros with length of all columns

        # Assigning the input values to the correct positions
        array[0] = self.length
        array[1] = self.curb_weight
        array[2] = self.engine_size
        array[3] = self.city_mpg
        array[4] = self.highway_mpg

        # Encoding categorical features
        array[make_index] = 1
        array[drive_wheels_index] = 1
        array[num_of_cylinders_index] = 1

        print("Test Array -->\n", array)

        # Predicting the car price
        predicted_price = self.model.predict([array])[0]

        return np.around(predicted_price, 2)  # Returning the predicted price rounded to 2 decimal places

if __name__ == "__main__":
    # Example input values for prediction
    length = 180  # Example value for car length
    curb_weight = 3000  # Example value for curb weight
    engine_size = 200  # Example value for engine size
    city_mpg = 25  # Example value for city mpg
    highway_mpg = 30  # Example value for highway mpg
    make = 9  # Example car make (assuming the "make" feature is indexed as 9)
    drive_wheels = 1  # Example value for drive wheels (1 for front-wheel drive)
    num_of_cylinders = "four"  # Example cylinder type (could be 'four', 'six', etc.)

    # Create an instance of Auto class
    auto = Auto(length, curb_weight, engine_size, city_mpg, highway_mpg, make, drive_wheels, num_of_cylinders)

    # Get the predicted price
    predicted_price = auto.get_predicted_price()

    print(f"Predicted Car Price: ${predicted_price} USD")
