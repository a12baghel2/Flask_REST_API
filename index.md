# This is a simple __API__ that provides you the data in ```JSON``` format.

***

> # To get the all the ```characters``` information :- 

## Get/ ```api/search/?characters```

> This will get you information of all the characters like this :- 

```JSON
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
 > # To get the all the ```planets``` information present in star-wars universe :- 

## Get/ ```api/search/?planets```

> This will get you information of all the Planets like this :- 

```JSON
{
    "0": {
        "name": "Alderaan",
        "rotation_period": "24",
        "orbital_period": "364",
        "diameter": "12500",
        "climate": "temperate",
        "gravity": "1 standard",
        "terrain": "grasslands, mountains",
        "surface_water": "40",
        "population": "2000000000"
    },
    "1": {
        "name": "Yavin IV",
        "rotation_period": "24",
        "orbital_period": "4818",
        "diameter": "10200",
        "climate": "temperate, tropical",
        "gravity": "1 standard",
        "terrain": "jungle, rainforests",
        "surface_water": "8",
        "population": "1000"
    },
}
 ```
 > ## To get detail about specific id 
 
 ## Get/```api/search/?key=planets&id=0```
 
 > You will the information for id=0 
 ```JSON
    {
        "name": "Alderaan",
        "rotation_period": "24",
        "orbital_period": "364",
        "diameter": "12500",
        "climate": "temperate",
        "gravity": "1 standard",
        "terrain": "grasslands, mountains",
        "surface_water": "40",
        "population": "2000000000"
    }
 ```
 > # To get the all the ```Species``` information that are present in the star-wars universe :- 

## Get/ ```api/search/?species```

> This will get you information of all the Species like this :- 

```JSON
{
    "0": {
        "name": "Hutt",
        "classification": "gastropod",
        "designation": "sentient",
        "average_height": "300",
        "skin_colors": "green, brown, tan",
        "hair_colors": "NA",
        "eye_colors": "yellow, red",
        "average_lifespan": "1000",
        "language": "Huttese",
        "homeworld": "Nal Hutta"
    },
    "1": {
        "name": "Yoda's species",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "66",
        "skin_colors": "green, yellow",
        "hair_colors": "brown, white",
        "eye_colors": "brown, green, yellow",
        "average_lifespan": "900",
        "language": "Galactic basic",
        "homeworld": "NA"
    },
}
 ```
 > ## To get detail about specific id 
 
 ## Get/```api/search/?key=species&id=0```
 
 > You will the information for id=0 
 ```JSON
    {
        "name": "Hutt",
        "classification": "gastropod",
        "designation": "sentient",
        "average_height": "300",
        "skin_colors": "green, brown, tan",
        "hair_colors": "NA",
        "eye_colors": "yellow, red",
        "average_lifespan": "1000",
        "language": "Huttese",
        "homeworld": "Nal Hutta"
    }
 ```

 > # To get the all the ```Starships``` information that are present in star-wars universe:- 

## Get/ ```api/search/?starships```

> This will get you information of all the starships like this :- 

```JSON
{
    "0": {
        "name": "Executor",
        "model": "Executor-class star dreadnought",
        "manufacturer": "Kuat Drive Yards, Fondor Shipyards",
        "cost_in_credits": "1143350000",
        "length": "19000",
        "max_atmosphering_speed": "n/a",
        "crew": "279144",
        "passengers": "38000",
        "cargo_capacity": "250000000",
        "consumables": "6 years",
        "hyperdrive_rating": "2.0",
        "MGLT": "40",
        "starship_class": "Star dreadnought"
    },
    "1": {
        "name": "Sentinel-class landing craft",
        "model": "Sentinel-class landing craft",
        "manufacturer": "Sienar Fleet Systems, Cyngus Spaceworks",
        "cost_in_credits": "240000",
        "length": "38",
        "max_atmosphering_speed": "1000",
        "crew": "5",
        "passengers": "75",
        "cargo_capacity": "180000",
        "consumables": "1 month",
        "hyperdrive_rating": "1.0",
        "MGLT": "70",
        "starship_class": "landing craft"
    },
}
 ```
 > ## To get detail about specific id 
 
 ## Get/```api/search/?key=starships&id=0```
 
 > You will the information for id=0 
 ```JSON
    {
        "name": "Executor",
        "model": "Executor-class star dreadnought",
        "manufacturer": "Kuat Drive Yards, Fondor Shipyards",
        "cost_in_credits": "1143350000",
        "length": "19000",
        "max_atmosphering_speed": "n/a",
        "crew": "279144",
        "passengers": "38000",
        "cargo_capacity": "250000000",
        "consumables": "6 years",
        "hyperdrive_rating": "2.0",
        "MGLT": "40",
        "starship_class": "Star dreadnought"
    }
 ```
 > # To get the all the ```Vehicles``` information that are appeared in the starwars universe:- 

## Get/ ```api/search/?vehicles```

> This will get you information of all the vehicles like this :- 

```JSON
{
    "0": {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled"
    },
    "1": {
        "name": "T-16 skyhopper",
        "model": "T-16 skyhopper",
        "manufacturer": "Incom Corporation",
        "cost_in_credits": "14500",
        "length": "10.4",
        "max_atmosphering_speed": "1200",
        "crew": "1",
        "passengers": "1",
        "cargo_capacity": "50",
        "consumables": "0",
        "vehicle_class": "repulsorcraft"
    },
}
 ```
 > ## To get detail about specific id 
 
 ## Get/```api/search/?key=vehicles&id=0```
 
 > You will the information for id=0 
 ```JSON
    {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled"
    }
 ```
