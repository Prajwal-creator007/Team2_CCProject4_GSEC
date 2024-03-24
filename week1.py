import etcd3

etcd = etcd3.client()

def list_keys():
    print("Listing all keys:")
    for value, metadata in etcd.get_all():
        print(metadata.key.decode('utf-8'))

def get_value(key):
    value, metadata = etcd.get(key)
    if value:
        print(f"Value for {key}: {value.decode('utf-8')}")
    else:
        print(f"Key {key} not found.")

def put_key_value(key, value):
    etcd.put(key, value)
    print(f"Put {key}: {value}")


put_key_value("srn", "398")
get_value("key")
get_value("srn")
list_keys()