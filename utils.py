import requests
import json

def save_picture(file_name, folder_name, form_picture):
    try:
        response = requests.post("http://192.168.100.5:8888/" + folder_name, files={file_name: form_picture} )
        print('Response:\n', response.json())
        return True
    except requests.exceptions.ConnectionError:
        print("Failed to find IP and Port")
        return False

def get_pictures(folder_name, page_num):
    file_paths = []
    images = []
    # Limit of files to be shown/loaded per page
    limit = 10 

    # Get directory data in json
    url = "http://192.168.100.5:8888/" + folder_name
    try:
        response = requests.get(url, headers={'Accept': 'application/json'})
    except requests.exceptions.ConnectionError:
        print("Failed to find IP and Port")

    # Create python dict
    if response != None:
        dict_resp = json.loads(response.text)
    else:
        print("Falied first request to filer")
        return images

    # Find last file loaded based on page number requested
    last_file_num = 0
    if page_num > 1:
        last_file_num = (page_num - 1) * limit

    # Get path to last file shown
    if last_file_num < len(dict_resp['Entries']):
        last_file = dict_resp['Entries'][last_file_num]['FullPath']
        print(last_file)
    else: 
        # Set pagination to default/first page
        last_file = ""
        # Later set response.redirect

    # Get directory data with pagination
    response2 = get_dir_data(folder_name, last_file, limit)
    if response2 != None:
        file_list = json.loads(response2.text)
        for file_obj in file_list['Entries']:
            file_paths.append(file_obj["FullPath"])
    # Attempt to pass images straight back to route
    """
    for file_path in file_paths:
        response = requests.get("http://192.168.100.5:8888/" + folder_name + "/" + file_path)
        image = Image.open(BytesIO(response.content))
        images.append(image)
    """
    print(file_paths)
    return file_paths
        

def get_dir_data(folder_name, last_file, limit):
    # Use pagination in URL to get 10 images at a time
    try:
        response = requests.get("http://192.168.100.5:8888/" + folder_name + "/?pretty=y&lastFileName=" + last_file + "&limit=" + str(limit), headers={'Accept': 'application/json'})
        return response
    except requests.exceptions.ConnectionError:
        print("Failed to find IP and Port")
        return None
    
