import apache_beam as beam



class ParseFileFn(beam.DoFn):
    def __init__(self, headers):
        self.headers = headers
        print(self.headers)
        






with beam.Pipeline as p:
    user_request_header = ['id', 'first_name', 'last_name', 'email', 'gender']
    input_rows = (p
                    | 'ReadFile' >> beam.Create([""])
                    | 'ParseFile' >> beam.ParDo(ParseFileFn(user_request_header))
                    )
