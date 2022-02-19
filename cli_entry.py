import argparse
import run.main;

# this is for parsing the -arg command
def get_additional_arguments(pre_settings, settings):
    args = pre_settings['arg'];

    key_switch = { # format: settings key, store as array (true) or var (false)
        'tag': ('ARG_TAGS',True),
        'tags': ('ARG_TAGS',True),
        'create_tag': ('ARG_CREATE_TAG',False),
        'tag_category': ('ARG_TAG_CATEGORY',False),
        'posts':('ARG_POSTS',True),
        'post':('ARG_POSTS',True),
    }

    for a in args:
        pre_arr = a.split('=',maxsplit=1);
        if len(pre_arr) < 2:
            print('Argument {0} malformed'.format(a));
            exit();
        
        key = pre_arr[0].lower();
        # key = key.removeprefix('arg_'); # Requires Python 3.9

        (set_key, is_arr) = key_switch.get(key, ('error',False))

        if set_key == 'error':
            print('Unknown key {0}, continuing without it'.format(pre_arr[0]));
        elif is_arr:
            settings[set_key] = pre_arr[1].split(',');
        else:
            settings[set_key] = pre_arr[1];

# Entry, the Main Argument Parser
parser = argparse.ArgumentParser(prog='szuru',description='CLI for the Szurubooru-bot.\nThe cli will also make use of the config.json if it exists, you don\'t need to pass paramters that are set there.\nBut Parameters based in here take priority.\nIf you run the programm in bot mode and the config.json does not exist it will create a config.json');

connectGroup = parser.add_argument_group('Connection')
connectGroup.add_argument('-s','-S','--server',help='The Server Addresse. If the addresse includes http/s (and port is default or 80/443) it is assumed you are external, meaning it will add /api/ (if not present). Else it assumes to be talking directly to the backend server (default=server)');
connectGroup.add_argument('-p','-P','--port',help='The Server Port. (default=6666)',type=int);
connectGroup.add_argument('-d','-D','--data','--data-path',help='Path to the Data, required only for certain functions (like image2notes). The Default is that when the server is external it will fetch from there, if internal it assumes it got /data mount same as the server or client, but this will override this (read only is suffient). Also the data part is omitted, as each element path includes it');

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
paramGroup.add_argument('-arg',action='extend',nargs='+',help='Used in Command Mode to pass additional arguments. Format is "-arg Key=Value", if a key requires multiple values seperate via "," like this: "Key=Value1,Value2". Available keys can be checked in --list-methodes');

pre_settings = vars(parser.parse_args());

# List Commands
if 'list_methodes' in pre_settings and pre_settings['list_methodes'] == True:
    text = 'Unable to load doc/Commands.md, was it deleted?'
    try:
        with open('doc/Commands.md', 'r') as f:
            text = str(f.read());
    finally:
        print(text);
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
if pre_settings['token'] != None:
    settings['TOKEN'] = pre_settings['token'];

if pre_settings['data'] != None:
    settings['DATA_PATH'] = pre_settings['data'];

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

if pre_settings['arg'] != None:
    get_additional_arguments(pre_settings,settings);

# Back to our regularly scheduled programm
run.main.init(settings);