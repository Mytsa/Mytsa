# comparison data in row

class Comparison():
    def __init__(self):
        self.data_row_in = data_row_in
        self.data_row_out = data_row_out

    def comparison(self):
        if self.data_row_in == self.data_row_out:
            return None  # return something
        else:
            return self.data_row_in   # return data from row input ---test test
