import json
import pickle
import numpy as np
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

__location = None
__data_columns = None
__model = None

def get_estimated_price(location,squarefeet,bhk,bathrooms):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    input_array = np.zeros(len(__data_columns))
    input_array[0] = squarefeet
    input_array[1] = bhk
    input_array[2] = bathrooms
    if loc_index >= 0:
        input_array[loc_index] = 1

    #return round(__model.predict([input_array])[0],2)
    predicted_price = __model.predict([input_array])[0]

    # Convert to a positive value and get the first seven digits
    positive_value = str(abs(predicted_price))[:2]
    return positive_value


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location

    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    global __model
    if __model is None:
        with open("./artifacts/UAE_home prices_model.pickle","rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __location

def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1 residences, wasl1, al kifaf, dubai',1323,3,2))