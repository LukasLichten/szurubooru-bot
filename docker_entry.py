import os;
import run.main;

# Getting the settings from the docker envirment variables
print('Starting via Docker...');

settings = {};

settings['SERVER_ADDRESSE'] = os.getenv('SERVER_ADDRESSE', 'server');
settings['SERVER_PORT'] = os.getenv('SERVER_PORT', '6666');
settings['USER'] = os.getenv('USER', '');
settings['TOKEN'] = os.getenv('TOKEN', '');
settings['MODE'] = os.getenv('MODE', 'boT');
settings['METHODE'] = os.getenv('METHODE', '');

run.main.init(settings);