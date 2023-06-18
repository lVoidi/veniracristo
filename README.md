# Venir a cristo script
This is the most useless script i've made so far. Basically, it can subscribe
a full dataset of people you want, so some missionaires will call them and email them inspirational quotes. This is basically a troll program

## Some things you must take into account
First of all, you should create a **info.json** file to add the dataset 

it should look like this:

```json
    "members": [
        {
            "firstName": "First Name",
            "lastName": "Last Name",
            "email": "email@gmail.com",
            "phone": "Costa Rican Number"
        }, (...)
    ]
}
```
You CAN add any number for any country, but you HAVE to modify the code 
in order to make it work 
```py 
    "country": "Costa Rica",
    "locID": "106",
    "countryISO3": "CRI",
    "addr": get_direction[1],
    "city": get_direction[0],
    "state": get_direction[0],
    "zip": f"{random.randint(100, 100000)}",
    "phoneCountryCode": "+506",
    "phone": phone_number,
    "phoneCountry": "cr",
```
Check [this imgur thread](https://imgur.com/a/mExbtvE) to see how to make it. I made a whole tutorial (lmao).