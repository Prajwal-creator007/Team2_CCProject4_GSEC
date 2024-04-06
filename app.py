from flask import Flask, render_template, request
import etcd3

app = Flask(__name__)  # Corrected from _name to _name_
etcd = etcd3.client()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    keys_list = list_keys()  # Fetch keys list for every page load or operation
    if request.method == 'POST':
        if 'put' in request.form:
            key = request.form.get('key')
            value = request.form.get('value')
            result = put_key_value(key, value)
        elif 'get' in request.form:
            key = request.form.get('key')
            result = get_value(key)
        elif 'delete' in request.form:
            key = request.form.get('key')
            result = delete_key(key)

    return render_template('index.html', result=result, keys_list=keys_list)

def get_value(key):
    #key = request.form['key']
    try:
        value, _ = etcd.get(key)
        if value:
            return f"Value for {key}: {value.decode('utf-8')}"
        else:
            return f"Key {key} not found."
    except etcd3.exceptions.ConnectionFailedError as e:
        return f"Connection to etcd server failed: {e}"
    except Exception as e:
        return f"Failed to get {key}: {e}"

def put_key_value(key, value):
    #key = request.form['key']
    #value = request.form['value']
    try:
        etcd.put(key, value)
        return f"Put {key}: {value}"
    except etcd3.exceptions.ConnectionFailedError as e:
        return f"Connection to etcd server failed: {e}"
    except Exception as e:
        return f"Failed to put {key}: {e}"

def delete_key(key):
    try:
        value, _ = etcd.get(key)
        if value:
            etcd.delete(key)
            return f"Deleted key: {key}"
        else:
            return f"Key {key} not found."
    except etcd3.exceptions.ConnectionFailedError as e:
        return f"Connection to etcd server failed: {e}"
    except Exception as e:
        return f"Failed to delete {key}: {e}"

def list_keys():
    try:
        keys = [metadata.key.decode('utf-8') for value, metadata in etcd.get_all()]
        if keys:
            return "Keys: " + ", ".join(keys)
        else:
            return "No keys found."
    except etcd3.exceptions.ConnectionFailedError as e:
        return f"Connection to etcd server failed: {e}"
    except Exception as e:
        return f"Failed to list keys: {e}"

if __name__ == '__main__':  # Corrected from _name to _name_
    app.run(debug=True)
