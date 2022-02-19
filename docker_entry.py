import os;
import run.main;

# Getting the settings from the docker envirment variables
print('Starting via Docker...');

settings = {};

settings['SERVER_ADDRESSE'] = os.getenv('SERVER_ADDRESSE', 'server');
settings['SERVER_PORT'] = os.getenv('SERVER_PORT', '6666');
settings['USER'] = os.getenv('USER', '');
settings['TOKEN'] = os.getenv('TOKEN', '');
settings['MODE'] = os.getenv('MODE', '');
settings['METHODE'] = os.getenv('METHODE', '');

settings['DATA_PATH'] = os.getenv('DATA_PATH', '');

# Additional Arguments
settings['ARG_TAGS'] = os.getenv('ARG_TAGS', '').split(',');
settings['ARG_CREATE_TAG'] = os.getenv('ARG_CREATE_TAG', '');
settings['ARG_TAG_CATEGORY'] = os.getenv('ARG_TAG_CATEGORY', '');
settings['ARG_POSTS'] = os.getenv('ARG_POSTS', '').split(',');


run.main.init(settings);