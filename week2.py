import etcd3

etcd = etcd3.client()

def list_keys():
    try:
        print("Listing all keys:")
        for value, metadata in etcd.get_all():
            print(metadata.key.decode('utf-8'))
    except etcd3.exceptions.ConnectionFailedError as e:
        print("Connection to etcd server failed:", e)
    except Exception as e:
        print("An error occurred:", e)

def get_value(key):
    try:
        value, metadata = etcd.get(key)
        if value:
            print(f"Value for {key}: {value.decode('utf-8')}")
        else:
            print(f"Key {key} not found.")
    except etcd3.exceptions.KeyNotFoundError:
        print(f"Key {key} not found.")
    except etcd3.exceptions.ConnectionFailedError as e:
        print("Connection to etcd server failed:", e)
    except Exception as e:
        print("An error occurred:", e)

def put_key_value():
    try:
        key = input("Enter key: ")
        value = input("Enter value: ")
        etcd.put(key, value)
        print(f"Put {key}: {value}")
    except etcd3.exceptions.ConnectionFailedError as e:
        print("Connection to etcd server failed:", e)
    except Exception as e:
        print("An error occurred:", e)

def delete_key():
    try:
        key = input("Enter key to delete: ")
        etcd.delete(key)
        print(f"Deleted key: {key}")
    except etcd3.exceptions.KeyNotFoundError:
        print(f"Key {key} not found.")
    except etcd3.exceptions.ConnectionFailedError as e:
        print("Connection to etcd server failed:", e)
    except Exception as e:
        print("An error occurred:", e)


# Example usage:
try:
    put_key_value()
    get_value(input("Enter key to get value: "))
    list_keys()
    
    # Deleting a key
    delete_key()
    list_keys()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print("An error occurred:", e)
