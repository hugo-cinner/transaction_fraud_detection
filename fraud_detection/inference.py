import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import pickle


class FraudDetection():
    def __init__(self):
        super(FraudDetection, self).__init__()
        self.model = self.load_model()

    # Add the Backbone option in the parameters
    def load_model(self):
        model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
        with open(model_dir + '/model.pickle', 'rb') as f:
            model = pickle.load(f)
        return model

    def process_input(self, input_dict):
        dict = input_dict.copy()

        if dict['type'] == 'CASH_OUT':
            dict['type'] = 0
        else:
            dict['type'] = 1

        input_arr = []
        for key in dict.keys():
            if key not in ['nameOrig', 'nameDest']:
                input_arr.append(dict[key])

        return [input_arr]

    def run_inference(self, input_dict):
        if input_dict['type'] not in ['TRANSFER', 'CASH_OUT']:
            return False

        if input_dict['amount'] == 0:
            return True

        input = self.process_input(input_dict)
        output = self.model.predict(input)

        if output[0]:
            return True
        return False
