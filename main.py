from flask import Flask, jsonify, render_template, request
from models.utils import Auto  # Import the Auto class for car price prediction
app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Dear Sir/Mam, Welcome to Car Price Prediction")
    return render_template("index.html")

@app.route('/predict_price', methods=["POST", "GET"])
def get_car_price():
    if request.method == "GET":
        print("We are using GET Method")

        # Retrieve form data from the user input in the HTML form
        length = float(request.args.get("length"))
        curb_weight = float(request.args.get("curb_weight"))
        engine_size = float(request.args.get("engine_size"))
        city_mpg = float(request.args.get("city_mpg"))
        highway_mpg = float(request.args.get("highway_mpg"))
        make = request.args.get("make")
        drive_wheels = request.args.get("drive_wheels")
        num_of_cylinders = request.args.get("num_of_cylinders")

        print("Received Data -> Length:", length, ", Curb Weight:", curb_weight, ", Engine Size:", engine_size,
              ", City MPG:", city_mpg, ", Highway MPG:", highway_mpg, ", Make:", make, ", Drive Wheels:", drive_wheels,
              ", Number of Cylinders:", num_of_cylinders)

        # Initialize Auto class with provided values
        auto_predict = Auto(length, curb_weight, engine_size, city_mpg, highway_mpg, make, drive_wheels, num_of_cylinders)
        predicted_price = auto_predict.get_predicted_price()

        return render_template("index.html", prediction=predicted_price)  # Return the prediction to the template

    else:
        print("We are using POST Method")

        # Retrieve form data from the user input in the HTML form
        length = float(request.form.get("length"))
        curb_weight = float(request.form.get("curb_weight"))
        engine_size = float(request.form.get("engine_size"))
        city_mpg = float(request.form.get("city_mpg"))
        highway_mpg = float(request.form.get("highway_mpg"))
        make = request.form.get("make")
        drive_wheels = request.form.get("drive_wheels")
        num_of_cylinders = request.form.get("num_of_cylinders")

        print("Received Data -> Length:", length, ", Curb Weight:", curb_weight, ", Engine Size:", engine_size,
              ", City MPG:", city_mpg, ", Highway MPG:", highway_mpg, ", Make:", make, ", Drive Wheels:", drive_wheels,
              ", Number of Cylinders:", num_of_cylinders)

        # Initialize Auto class with provided values
        auto_predict = Auto(length, curb_weight, engine_size, city_mpg, highway_mpg, make, drive_wheels, num_of_cylinders)
        predicted_price = auto_predict.get_predicted_price()

        return render_template("index.html", prediction=predicted_price)  # Return the prediction to the template

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
