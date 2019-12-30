import numpy as np
import joblib


class Car:
    def __init__(self, car):
        self.car = car

    def prepare(self):
        result = np.zeros(58)
        result[0] = float(self.car[0])
        result[1] = float(self.car[1])
        result[2] = float(self.car[2])
        result[3] = float(self.car[3])
        result[4] = float(self.car[4])
        result[5] = float(self.car[5])
        result[6] = float(self.car[6])
        result[7] = float(self.car[7])
        make = {'acura': 8, 'audi': 9, 'bmw': 10, 'buick': 11, 'cadillac': 12, 'chevrolet': 13, 'chrysler': 14,
                'dodge': 15, 'ford': 16, 'gmc': 17, 'honda': 18, 'hummer': 19, 'hyundai': 20, 'infiniti': 21, 'isuzu': 22,
                'jaguar': 23, 'jeep': 24, 'kia': 25, 'land_rover': 26, 'lexus': 27,
                'lincoln': 28, 'mini': 29, 'mazda': 30, 'mercedes-benz': 31, 'mercury': 32, 'mitsubishi': 33,
                'nissan': 34, 'oldsmobile': 35, 'pontiac': 36, 'porsche': 37, 'saab': 38, 'saturn': 39,
                'scion': 40, 'subaru': 41, 'suzuki': 42, 'toyota': 43, 'volkswagen': 44, 'volvo': 45, 'asia': 46,
                'europe': 47, 'usa': 48, 'hybrid': 49, 'suv': 50, 'sedan': 51, 'sports': 52, 'truck': 53,
                'wagon': 54, '4wd': 55, 'fwd': 56, 'rwd': 57}
        result[make[self.car[8]]] = 1
        result[make[self.car[9]]] = 1
        result[make[self.car[10]]] = 1
        result[make[self.car[11]]] = 1
        return result

    def predict(self, car):
        car_to_predict = [car]
        model = joblib.load('model.pkl')
        predicted_car_value = model.predict(car_to_predict)
        value = predicted_car_value[0]
        return value
