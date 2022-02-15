import argparse
import run.main;

# Argument Parser
parser = argparse.ArgumentParser(prog='szuru',description='CLI for the Szurubooru-bot.\nThe cli will also make use of the config.json if it exists, you don\'t need to pass paramters that are set there.\nBut Parameters based in here take priority.\nIf you run the programm in bot mode and the config.json does not exist it will create a config.json');

connectGroup = parser.add_argument_group('Connection')
connectGroup.add_argument('-s','-S','--server',help='The Server Addresse. If the addresse includes http/s (and port is default or 80/443) it is assumed you are external, meaning it will add /api/ (if not present). Else it assumes to be talking directly to the backend server (default=server)');
connectGroup.add_argument('-p','-P','--port',help='The Server Port. (default=6666)',type=int);

connectGroup.add_argument('-u','-U','--user',help='Username, can be a regular user, but moderator is recommended (as it required for some tasks)');
connectGroup.add_argument('-t','-T','--token',help='Login Token for this user, no password authentication, easiest way is to generate one via the standard web interface');

modeUpGroup = parser.add_argument_group('Mode')
modeGroup = modeUpGroup.add_mutually_exclusive_group();
modeGroup.add_argument('-b','-B','--bot',action='store_true',help='Bot Mode, continues running (default)');
modeGroup.add_argument('-c','-C','--com','--command',action='store_true',help='Command Mode, will exectue the METHODE and exit');
modeGroup.add_argument('-a','-A','--api',action='store_true',help='API Mode, will call METHODE on the api and exit');

paramGroup = parser.add_argument_group('Parameters')
paramGroup.add_argument('-m','--methode',help='Required for Command and API mode, ignored in Bot mode, use --list-methodes to get a list');
paramGroup.add_argument('--list-methodes',action='store_true',help='List of Commands');

pre_settings = vars(parser.parse_args());

# List Commands
if 'list_methodes' in pre_settings and pre_settings['list_methodes'] == True:
    header="Methodes:\nFor documentation for the Methodes for the api command visit https://github.com/rr-/szurubooru/blob/master/doc/API.md .\nIt is important to omit the first /, as this one is included in the server url (even if you omitted it), for example: 'users/' \n\n"
    commands="";
    print(header + commands);
    exit();

# Parsing Arguments into the settings
settings = {};
if pre_settings['server'] != None:
    settings['SERVER_ADDRESSE'] = pre_settings['server'];
else:
    settings['SERVER_ADDRESSE'] = 'server';

if pre_settings['port'] != None:
    settings['SERVER_PORT'] = ''.format(pre_settings['port']);
else:
    settings['SERVER_PORT'] = '6666';

if pre_settings['user'] != None:
    settings['USER'] = pre_settings['user'];
if 'token' in pre_settings:
    settings['TOKEN'] = pre_settings['token'];

if pre_settings['bot'] == True:
    settings['MODE'] = 'bot';
elif pre_settings['com'] == True:
    settings['MODE'] = 'com';
elif pre_settings['api'] == True:
    settings['MODE'] = 'api';
else:
    settings['MODE'] = '';

if pre_settings['methode'] != None:
    settings['METHODE'] = pre_settings['methode'];

# Back to our regularly scheduled programm
run.main.init(settings);