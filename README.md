# szurubooru-bot
Some python to perform admin tasks in [szurubooru](https://github.com/rr-/szurubooru), able to be used [containerized](https://hub.docker.com/r/generalfluff/szurubooru-bot) or cli (or cli in container)  

## Features
+ Deploy as you need:
  + [Docker](https://hub.docker.com/r/generalfluff/szurubooru-bot) in Bot mode, doing bot tasks but also allowing to exec into and run commands via cli using the container config
  + [Docker](https://hub.docker.com/r/generalfluff/szurubooru-bot) in Single command, runs the command and closes
  + Cli can do both as well
+ Admin tools:
  + Mass Tagging
  + Run commands on the api
+ Bot tools:
  + *Todo*

## Variables

| Docker          | Cli           | Default    | Description                                                                                                                                                                                               |
| ----------------|-------------|----------| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVER_ADDRESSE | --server *add*   | server     | The Server Addresse. If the addresse includes http/s (and port is default or 80/443) it is assumed you are external, meaning it will add /api/ (if not present). Else it assumes to be talking directly to the backend server. |
| SERVER_PORT     | --port *port*    | 6666       | The Port to access the server with, the default port of 6666 is the default port of the backend server of szurubooru                                                                                                                                                          |
| USER            | --user *user*    | *required* | Username, can be a regular user, but moderator is recommended (as it required for some tasks)                                                                                                                                            |
| TOKEN           | --token *token*  | *required* | Login Token for this user, no password authentication, easiest way is to generate one via the standard web interface                                                                                      |
| MODE            | -b/-c/-a         | bot        | Mode, can be either bot for running in bot mode, command (c or com) to run a single command or api which allows you to run an api command                                                                      |
| METHODE         |  --methode *met* | *optional* | Ignored in Bot mode, but is required for command and api mode. It is the [command](doc/API.md) for command mode and the api [url-ending](https://github.com/rr-/szurubooru/blob/master/doc/API.md) for api mode                                                                        |
| ARG_*KEY*         |  -arg *Key*=*Value* | *optional* | Additional arguments needed for certain commands in Command Mode, see [here](doc/API.md) for a list.                                                                        |


Running the programm in Bot Mode will lead to the automatic creation of a config.json (a dicitonary using the Docker names as keys).  
Variables from cli/docker enviroment will take priority, anything missing will be added from the config.json (no need to pass the server_address and credentials then, but you can to control someone else).  
If the config.json exists it won't be overwritten.  
You can create/edit a config.json to set defaults, including setting the MODE to something other then bot.  

## Plans
+ Other mass editing
+ Gathering Text from Images
+ Auto Tagging
