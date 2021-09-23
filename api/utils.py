from fraud_detection.inference import FraudDetection


class RunFraudDetectionInference():
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.detection = FraudDetection()

    def run(self):
        res = self.detection.run_inference(self.input_dict)
        return res
