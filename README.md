# py-spatially

## Authorization:
A valid token must be passed when calling any function.  To get this token use the `api.GetToken` function.  Example:
```
applicationCode = "{your code}"
applicationKey = "{your key}"
token = api.GetToken(applicationCode, applicationKey)
```

## Functions
Examples of calls to all functions can be found in the `tests` directory.

### Grid Functions:

 - GetPopulation(token, wktPoint, radius)
 - GetTradeAreaPopulation(token, ata)
 - GetActivity(token,wktPoint, radius)
 - GetDistanceSensitivity(token, wktPoint, radius)
 - GetHighlights(token,wktPoint, radius)

 ### ATA Functions:

  - NewATA(token,locationWKT,timeOfDay="AllDay", locationType="Home", geoFence=False)