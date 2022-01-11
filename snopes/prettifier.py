import json

def prettify(src_path, dst_path):
    src_file = open(src_path, mode='r')
    data = json.load(src_file)
    print('number of facts= ' + str(len(data)))
    dst_data = json.dumps(data, indent=1)
    
    dst_file = open(dst_path, mode='w')
    dst_file.write(dst_data)

    src_file.close()
    dst_file.close()


if __name__ == "__main__":
    src_path = 'facts.json'
    dst_path = 'prettified_facts.json'
    prettify(src_path, dst_path)
