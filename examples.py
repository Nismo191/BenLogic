data = file_operations.read_json('input/demo_data.json')
size_data = file_operations.read_json('input/demo_data_2.json')

# Change key names
data = flow.change_key('colour', 'color', data)

# Add value (time)
data = flow.add_value('time', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), data)

# Remove creator value
data = flow.remove_key('creator', data)

# Join two objects
data, unmatched = flow.join(data, size_data, 'name', 'name')

file_operations.write_json('output/demo_data_copy.json', data)
file_operations.write_json('output/unmatched.json', unmatched)

api_data = rest.get('https://jsonplaceholder.typicode.com/todos/')

file_operations.write_json('output/api_test.json', api_data, True)

api_post_url = 'https://ce8bf00f2f0dc7399b515ab8626fd424.m.pipedream.net/test'
# api_post_data = {'name': 'John', 'age': '25'}
api_post_data = file_operations.read_json('input/demo_data.json')

rest.post(api_post_url, api_post_data)

files, folders = file_operations.directory_browser('input')