import pandas as pd
data = pd.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)
print(type(data_dict))

data_list = data['temp'].to_list()
print(data_list)
print(type(data_list))

print(data)
print(type(data))
print(data.mean())
print()

# get the row data

# Data frame from Scratch

data_dic = {
    "students": ["Amy", "John", "Kumar"],
    "scores": [78, 45, 45]
}

df = pd.DataFrame(data_dic)
df.to_csv("PandasToCSV.csv")
print(data.describe())

df.to_excel('Excel_Sample.xlsx', sheet_name='Sheet1')




