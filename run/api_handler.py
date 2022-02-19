import requests;

def get_and_out(settings,method):
    url = settings['API_URL'] + method;
    (code, j) = get(url,settings['HEADER'])

    print(code);
    #json_response = response.json();
    print(j);

def get_code(url):
    response = requests.get(
        url
    );
    
    return response.status_code;
    
def download_file(url, file):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk);
    
    return file;

def get(url, header):
    response = requests.get(
        url,
        headers=header
    );
    if response.status_code == 500:
        return (response.status_code,{'description':'Internal Server Error'});
    
    return (response.status_code,response.json());

def post(url, header, json_payload):
    response = requests.post(
        url,
        headers=header,
        data=json_payload
    );
    if response.status_code == 500:
        return (response.status_code,{'description':'Internal Server Error'});
    
    return (response.status_code,response.json());

def put(url, header, json_payload):
    response = requests.put(
        url,
        headers=header,
        data=json_payload
    );
    if response.status_code == 500:
        return (response.status_code,{'description':'Internal Server Error'});
    
    return (response.status_code,response.json());