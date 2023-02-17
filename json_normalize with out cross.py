from copy import deepcopy
import pandas
import json

def json_normalizer(in_data):
    new_debt_dic = {}
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            for key, value in data.items():
                flatten_json(value, prev_heading + '.' + key)
        elif isinstance(data, list):
            if len(data)<=1:
                for i in range(len(data)):
                    flatten_json(data[i], prev_heading)
            else:
                for i in range(len(data)):
                    flatten_json(data[i], prev_heading+"-"+str(i+1))
        else:
            new_debt_dic[prev_heading[1:]] = data
        

        return new_debt_dic
    return flatten_json(in_data)

    


if __name__ == '__main__':
    json_file='''{"coffee":{"region":[{"id":1,"name":"John Doe"},{"id":2,"name":"Don Joeh"}],"country":{"id":2,"company":"ACME"}},"brewing":{"region":[{"id":1,"name":"John Doe"},{"id":2,"name":"Don Joeh"}],"country":{"id":2,"company":"ACME"}}}'''
    json_data = json.loads(json_file)
    df = flatten_json(json_data)
    df=pandas.DataFrame(df)
    df.to_csv("C:/Users/sprakashreddychin/Pictures/js_to_da.csv")
    print(df)
