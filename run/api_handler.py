import requests;

def get_and_out(settings,method):
    url = settings['API_URL'] + method;
    response = requests.get(
        url,
        headers=settings['HEADER']
    );

    print(response.status_code);
    json_response = response.json();
    print(json_response);