data = [
    {"name":'jane', 'age':1, 'county':'kajiado','facility':'Ngong SCK' },
    {"name":'jones', 'age':3, 'county':'nakuru','facility':'naivasha' },
    {"name":'John', 'age':5, 'county':'Narok','facility':'Transmara Wets' },
    {"name":'Peter', 'age':6, 'county':'Kiambu','facility':'Tigoni' },
    ]
# write a function to change the above data structure to a list with lists structure see sample data
sample_output = [
    ['actualname',1,'kajiado','Ngong'],
    ['jones',3,'nakuru','Ngong'],
    ['john',5,'narok','Ngong'],
    ['Peter',6,'kiambu','Tigoni'],
]
def transform_data(data):
    transformed_data = []
    for entry in data:
        transformed_entry = [entry['name'], entry['age'], entry['county'], entry['facility']]
        transformed_data.append(transformed_entry)
    return transformed_data
    
print(transform_data(data))
# return sample_output             
# Inside sample endpoint the 
## data = sample output
## key
## worksheet