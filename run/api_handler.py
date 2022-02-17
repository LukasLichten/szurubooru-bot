import requests;

def get_and_out(settings,method):
    url = settings['API_URL'] + method;
    (code, j) = get(url,settings['HEADER'])

    print(code);
    #json_response = response.json();
    print(j);

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