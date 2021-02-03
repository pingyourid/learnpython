class Survey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    def insert_response(self, response):
        self.responses.append(response)
        # self.responses
    def report(self):
        print(f'\n------------------------------\nYour question is {self.question}:')
        print('\nand responses:')
        for response in self.responses:
            print(response)