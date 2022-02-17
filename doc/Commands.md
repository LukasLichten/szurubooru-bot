# Methodes
This is a list of Methodes and their arguments.  
It is important that when running in Docker to add `ARG_` infront of each argument key (and the key has to be captialized), while in CLI the prefix can be omitted.  
In CLI `-arg` has to be put infront of your arguments, you can chain however multiple Key Value pairings without needing to put -arg infront every one (but you can). The pair has to be in the Key=Value format.  
  
Generally, Argument Values that take multiple values use `,` as seperator  
  
## API-Mode
For documentation for the Methodes for the api command visit [szurubooru api documentation](https://github.com/rr-/szurubooru/blob/master/doc/API.md).  
It is important to omit the first /, as this one is included in the server url (even if you omitted it), for example: 'users/'  
  
## Command-Mode
### Mass Tag
  
`mass_tag`  
  
Serves to tag multiple posts with one or many tags in one go. It can create tags that don't exist yet in a specified category, or abort  
  
| Argument key | Description                                                                  |
| -------------|:----------------------------------------------------------------------------:|
| TAGS         | The Tags, *multi value*                                                      |
| POSTS        | The Post IDs, defined as a range, *example: 1,3-5 is equivalent to 1,3,4,5*  |
| CREATE_TAG   | True or False to creating tags that don't exist yet, *default: True*         |
| TAG_CATEGORY | Only applies to newly created tags, *default: default category*              |