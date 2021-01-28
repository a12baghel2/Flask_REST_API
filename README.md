# This is a simple __API__ that provides you the data in ```JSON``` format.

***

> # To get the all the ```characters``` information :- 

## Get/ ```api/search/?characters```

> This will get you information of all the characters like this :- 

```javascript
{
    "0": {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "Tatooine",
        "species": "Human"
    },
    "1": {
        "name": "C-3PO",
        "height": "167",
        "mass": "75",
        "hair_color": "NA",
        "skin_color": "gold",
        "eye_color": "yellow",
        "birth_year": "112BBY",
        "gender": "NA",
        "homeworld": "Tatooine",
        "species": "Droid"
    }
}
 ```
 > ## To get detail about specific id 
 
 ## Get/```api/search/?key=characters&id=0```
 
 > You will the information for id=0 
 ```JSON
 {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "Tatooine",
        "species": "Human"
    }
 ```
 
