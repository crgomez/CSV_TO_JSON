# CSV_TO_JSON

Utilizing content within a CSV file we can go ahead and define field headers such as:

*  ”is_negated"	
*  "is_regex"
*  "replace_target"
* "rule_id" 
* "target"
* "target_match"

## Context should be placed under respective field headers within the .CSV
```
is_negated,is_regex,replace_target,rule_id,target,target_match
TRUE,FALSE,,973333,ARGS,ibe-data
TRUE,FALSE,,973344,ARGS,ibe-data
TRUE,FALSE,,950001,ARGS,OPTOUTMULTI
TRUE,FALSE,,973344,ARGS,ibe-data
TRUE,FALSE,,950001,ARGS,OPTOUTMULTI
TRUE,FALSE,,973333,ARGS,ibe-data
TRUE,FALSE,,959070,ARGS,remarksToAgent
TRUE,FALSE,,959072,ARGS,remarksToAgent
TRUE,FALSE,,981247,ARGS,remarksToAgent
TRUE,FALSE,,981256,ARGS,remarksToAgent
```
## Run python script RTU’s.py which will output RTU’s in JSON format
```
{
    "target": "ARGS", 
    "replace_target": "", 
    "rule_id": "973333", 
    "is_regex": "FALSE", 
    "is_negated": "TRUE", 
    "target_match": "ibe-data"
}
{
    "target": "ARGS", 
    "replace_target": "", 
    "rule_id": "973344", 
    "is_regex": "FALSE", 
    "is_negated": "TRUE", 
    "target_match": "ibe-data"
}
```
