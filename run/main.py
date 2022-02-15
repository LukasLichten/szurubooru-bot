import json;
import base64;
import time;

from . import api_handler;

# called by docker_entry or cli after gathering their enviroment variables
def init(settings):
    # basic clean up:
    for key, value in settings.copy().items():
        if value == '':
           del settings[key]; 

    file_settings = read_conf();

    # there is a config file, enviroment variables have priority
    if len(file_settings) > 0:
        print('Setting File found, adding values, enviroment variables keep priority');
        for key, value in file_settings.copy().items():

            if key == 'SERVER_ADDRESSE' and key in settings and settings[key] == 'server':
                # the addresse in env is the default, we will use the one from the file
                settings[key] = file_settings[key];
            elif key == 'SERVER_PORT' and key in settings and settings[key] == '6666':
                # the port in env is the default, we will use the one from the file
                settings[key] = file_settings[key];
            elif key == 'MODE' and key in settings and settings[key] == 'boT':
                # the mode is default, using the mode from the file
                settings[key] = file_settings[key];
            elif key not in settings:
                settings[key] = file_settings[key];
    
    elif 'MODE' not in settings or settings['MODE'].lower() == 'bot':
        # we only write the config if it does not exist already
        print('Writing Setting File');
        write_conf(settings);
    

    # formating url
    print('Preparing Config...')

    if 'SERVER_ADDRESSE' not in settings:
        lacking_key_error_thrower('SERVER_ADDRESSE');

    api_url = settings['SERVER_ADDRESSE'];

    has_http = api_url.find('http') != -1;
    if 'SERVER_PORT' not in settings:
        settings['SERVER_PORT'] = '-1'

    if not has_http or (has_http and settings['SERVER_PORT'] not in ['-1', '80', '443', '6666']):
        if not has_http:
            api_url = 'http://' + api_url;
    
        if api_url.endswith('/'):
            # so we can add the port we remove the last slash
            api_url = api_url[:(len(api_url)-1)];
    
        # TODO: Check for existing port in the url

        if settings['SERVER_PORT'] == '-1':
            lacking_key_error_thrower('SERVER_PORT');

        api_url = api_url + ':' + settings['SERVER_PORT'] + '/';
    else: #external mode, insuring http
        if not api_url.endswith('/api/'):
            if api_url.endswith('/'):
                # uniform adding of the api
                api_url = api_url[:(len(api_url)-1)];
            api_url = api_url + '/api/';
    
    settings['API_URL'] = api_url;
    
    print('Server: {0}'.format(api_url))

    # formating header
    if 'USER' not in settings:
        lacking_key_error_thrower('USER');
    if 'TOKEN' not in settings:
        lacking_key_error_thrower('TOKEN');
    
    auth = settings['USER'] + ':' + settings['TOKEN'];
    authBase64 = str(base64.b64encode(auth.encode("utf-8")), "utf-8");
    settings['AUTH'] = authBase64;

    header = {'Accept': 'application/json','Content-Type':'application/json','Authorization':'Token {0}'.format(authBase64)};
    settings['HEADER'] = header;
    print('User: {0}'.format(settings['USER']));

    # Branching between single run and continues execution
    if 'MODE' not in settings or settings['MODE'].lower() == 'bot':
        run(settings);
    else:
        if 'METHODE' not in settings:
            lacking_key_error_thrower('METHODE');
        

        if settings['MODE'].lower() == 'command' or settings['MODE'].lower() == 'c' or settings['MODE'].lower() == 'com':
            print('Entering Command Mode...');

        elif settings['MODE'].lower() == 'api':
            print('Entering API Mode...');
            method = settings['METHODE'];
            print('Executing {0}'.format(method));
            api_handler.get_and_out(settings, method);
    
    print('Finished execution');

def run(settings):
    print('Entering Bot Mode...');

    # TODO: proper programm
    while True:
        time.sleep(10);

def read_conf():
    settings = {};
    try:
        with open('config.json', 'r') as f:
            settings = json.load(f);
    finally:
        return settings;

def write_conf(settings):
    with open('config.json', 'w') as f:
        json.dump(settings, f);

def lacking_key_error_thrower(key):
    print('Missing {0}, which is required to be passed in'.format(key));
    raise NameError('{0} was not passed in, and is missing'.format(key));