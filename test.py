from utils.transcriber import recognize_from_microphone
from utils.stringCleaner import to_clean_string
from utils.differenceFinder import find_differences

class Test:
    def __init__(self, answer_key, test_number):
        self.answer_key = answer_key
        self.test_number = test_number
        self.transcriber_result = recognize_from_microphone()
        self.raw_string = self.transcriber_result["text"]
        self.duration = self.transcriber_result["duration"]
        self.rounded_duration = round(self.duration)
        self.cleaned_string = to_clean_string(self.raw_string)
        self.marker_results = find_differences(self.cleaned_string, self.answer_key)

    def add_errors(self, total_errors):
        for err in self.marker_results["errors"]:
            total_errors[err] += self.marker_results["errors"][err]

    def print_results(self):
        results = {
            "test_number": self.test_number,
            "rounded_duration": self.rounded_duration,
            "answer_key": self.answer_key,
            "cleaned_string": self.cleaned_string,
            "raw_string": self.raw_string,
            "marked_numbers": self.marker_results['marked_numbers'],
            "errors": self.marker_results['errors'],
            "differences": self.marker_results["differences"]
        }
        return results
        


    


    