# szurubooru-bot
Some python to perform admin tasks in [szurubooru](https://github.com/rr-/szurubooru), able to be used containerized or cli (or cli in container)  

## Features
+ Deploy as you need:
  + Docker in Bot mode, doing bot tasks but also allowing to exec into and run commands via cli using the container config
  + Docker in Single command, runs the command and closes
  + Cli can do both as well
+ Admin tools:
  + Mass Tagging *WIP*
  + Run commands in api
+ Bot tools:
  + *Todo*

## Variables

| Docker          | Cli           | Default    | Description                                                                                                                                                                                               |
| ----------------|:-------------:|:----------:| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| SERVER_ADDRESSE | *TODO*        | server     | if the addresse includes http/s (and port is default or 80/443) it is assumed you are external, meaning it will add /api/ (if not present). Else it assumes to be talking directly to the backend server. |
| SERVER_PORT     | *TODO*        | 6666       | default port of the backend server of szurubooru                                                                                                                                                          |
| USER            | *TODO*        | *required* | Username, can be a regular user, but moderator is recommended                                                                                                                                             |
| TOKEN           | *TODO*        | *required* | Login Token for this user, no password authentication, easiest way is to generate one via the standard web interface                                                                                      |
| MODE            | *TODO*        | bot        | Mode, can be either bot for running in bot mode, command (c or com) to run a single command or api which allows you to run an api command                                                                      |
| METHODE         | *TODO*        | *optional* | Ignored in Bot mode, but is required for command and api mode. It is the [command](https://github.com/TheLichten/szurubooru-bot/blob/master/doc/Commands.md) for command mode and the api [url-ending](https://github.com/rr-/szurubooru/blob/master/doc/API.md) for api mode                                                                        |


Running the programm in Bot Mode will lead to the automatic creation of a config.json (a dicitonary using the Docker names as keys).  
Variables from cli/docker enviroment will take priority, anything missing will be added from the config.json (no need to pass the server_address and credentials then, but you can to control someone else).  
If the config.json exists it won't be overwritten.  
You can create/edit a config.json to set defaults, including setting the MODE to something other then bot.  

## Plans
+ Mass Tagging (and other mass editing)
+ Gathering Text from Images
+ Auto Tagging
