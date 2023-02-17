from copy import deepcopy
import pandas
import json
import ast
import os
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


def input_type_val(in_data_val):
        if isinstance(in_data_val, list):
            
            input_list_json=[]
            for value in in_data_val:
                my_json_str = json.dumps(value)
                
                json_data = json.loads(my_json_str)
                
                input_list_json.append(json_data)
            
            return input_list_json

        elif isinstance(in_data_val,str):
            if in_data_val.startswith('[') and in_data_val.endswith(']'):
                res = json.loads(in_data_val)
                return input_type_val(res)
            else:
                in_data_val=json.dumps(in_data_val)
                json_data = json.loads(in_data_val)
                return json_data
        else:
            return "error dfata"

def input_validation(input_data):
    input_data="""{}""".format(input_data)
    if input_data.endswith('.json') or input_data.endswith('.txt'):
        if os.path.isfile(input_data) is True:
            json_file_data = open(input_data)
            input_json_data=json.load(json_file_data)
            validated_json=input_type_val(input_json_data)
        else:
            print(FileNotFoundError)
    else:
        validated_json=input_type_val(input_data)
    final_list=[]
    if isinstance(validated_json,dict):
        for value in validated_json:
            value=json.dumps(value)
            json_data = json.loads(value)
            df = json_normalizer(json_data)
            final_list.append(df)
    elif isinstance(validated_json,str):
            validated_json=json.dumps(validated_json)
            json_data = json.loads(validated_json)
            df = json_normalizer(json_data)
            final_list.append(df)
    elif isinstance(validated_json,list):
        for value in validated_json:
            value=json.dumps(value)
            json_data = json.loads(value)
            df = json_normalizer(json_data)
            final_list.append(df)

    return final_list
    






    


if __name__ == '__main__':
    input_data='''[{"data":[{"MainId":1111,"firstName":"Sherlock","lastName":"Homes","categories":[{"CategoryID":1,"CategoryName":"Example"}]},{"MainId":122,"firstName":"James","lastName":"Watson","categories":[{"CategoryID":2,"CategoryName":"Example2"}]}],"messages":[],"success":true},{"data":[{"MainId":1112,"firstName":"Sherlock","lastName":"Homes","categories":[{"CategoryID":2,"CategoryName":"Example2"}]},{"MainId":123,"firstName":"James","lastName":"Watson","categories":[{"CategoryID":3,"CategoryName":"Example2"}]}],"messages":[],"success":true}]'''
    #input_data="""{"data":[{"MainId":1111,"firstName":"Sherlock","lastName":"Homes","categories":[{"CategoryID":1,"CategoryName":"Example"}]},{"MainId":122,"firstName":"James","lastName":"Watson","categories":[{"CategoryID":2,"CategoryName":"Example2"}]}],"messages":[],"success":true}"""
    input_data='''C:/Users/sprakashreddychin/Videos/new 1.json'''
    final_result=input_validation(input_data)
    print(final_result)
 
