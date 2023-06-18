# Made by lvoidi 
# https://github.com/lvoidi
# This program takes costa rican numbers and sign in them into veniracristo.com
# In order to make the program work, you must create a *info.json* file in the current
# directory, with the following info
# --------- HOW TO ORGANIZE YOUR DATASET ---------
# "members": [
#     {
#         "firstName": "First Name",
#         "lastName": "Last Name",
#         "email": "emailWithValidFormar@gmail.com",
#         "phone": "8323 1238" # This must be a COSTA RICAN NUMBER
#     }, (...)
# ]
# members SHOULD have an array with all of your victims (XD)
# PD: If you want to use any number that isn't from Costa Rica, you must modify get_adress and 
# return_data_dict 
# MODIFY THESE VALUES
# "country": "Your Country",
# "locID": "106",
# "countryISO3": "your country iso3",
# "addr": get_direction[1],
# "city": get_direction[0],
# "state": get_direction[0],
# "zip": f"{random.randint(100, 100000)}",
# "phoneCountryCode": "your phone number country code",

import random
import colorama
import time
import requests 
import json

dataset = {}

with open("info.json") as file: 
    dataset = json.load(file)

url = "https://www.veniracristo.org/comeuntochrist/api/forms"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
}

def get_address():
    """
    This function will return a random costa rican adress in this order 
    (Province, city, random places) 
    
    You can customize this function, btw the adress value don't matter at all so 
    that's why you can literally invent your addr data. 
    """ 
    provinces = ["Alajuela", "San José", "Limón", "Cartago", "Heredia", "Puntarenas", "Guanacaste"]
    cardinates = ["Norte", "Sur", "Este", "Oeste"]
    cities = ["San Carlos", "Upala", "Playas del coco", "Lindora"]
    locations = ["A la par del parque", "Centro", f"{random.randint(100, 1000)}m de la iglesia hacia el {random.choice(cardinates)}"]
    return random.choice(provinces), f"{random.choice(cities)} {random.choice(locations)}" 

def return_data_dict(name,  last_name, phone_number, email):
    get_direction = get_address()
    result = {
        "firstName": name,
        "lastName": last_name,
        "email": email,
        "subscriptions": "mDGLSPAInspirationSubscribed",
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
        "offerType": "meetWithMissionaries",
        "customWhitelist": "true",
        "formType": "request",
        "lang": "spa",
        "preferredLanguageId": "2",
        "countryIso2": "undefined",
        "successPageURL": "*!veniracristo!success!spa!published",
        "cancelPageURL": "*!veniracristo!cancel!spa!published",
        "formTopicId": "2c54b042-6c2c-4ed0-927e-2919b627a551",
        "system_source": "ComeUntoChrist",
        "submittingURL": "https://www.veniracristo.org/",
        "pageTitle": "Bienvenido | veniracristo",
        "offerId": "134",
        "sourceId": "5502",
        "offerType": "meetWithMissionaries",
        "munchkinId": "",
        "marketoToken": "", 
        "domain": "www.veniracristo.org",
        "offerDetails": """[{"description":"¿Cómo prefieres que te contactemos?","text":"¿Cómo prefieres que te contactemos?","type":"MULTI_SELECT","options":["Llamada telefónica","Mensaje de WhatsApp","Mensaje de texto"],"availableDate":"2020-01-13T15:00:00","endDate":"2024-12-31T23:59:59","userEditableOption":false,"missionaryEditable":true,"sortOrder":"8","locale":"spa","questionGuid":"8d544658-2c0f-4030-93e2-03e19c1996f5","selected":["Llamada telefónica","Mensaje de WhatsApp","Mensaje de texto"]},{"description":"Por favor, confirma - missionaries","text":"Por favor, confirma:","type":"MULTI_SELECT","options":["Entiendo que los misioneros se pondrán en contacto conmigo para responder a mis preguntas y compartir un mensaje edificante."],"availableDate":"2020-05-13T15:00:00","userEditableOption":false,"missionaryEditable":false,"sortOrder":"1","locale":"spa","questionGuid":"07ff6313-f364-4a18-8ff4-d5d25cb4ee7e","selected":["Entiendo que los misioneros se pondrán en contacto conmigo para responder a mis preguntas y compartir un mensaje edificante."]}]""",
        "transactionId": "16870503377102267",
        "hashed": "2908ec72",
        "adobeVisitorId": "" ,
        "MDCampaignId": "10",
        "boncomCampaignId": "0"
    }
    return result

for member in dataset["members"]:
    data = return_data_dict(
        member["firstName"],
        member["lastName"],
        member["phone"],
        member["email"],
    )

    r = requests.post(url, data=data, headers=headers)

    b = colorama.Style.BRIGHT
    reset = colorama.Style.RESET_ALL
    status_code = f"{colorama.Fore.GREEN}{r.status_code}{reset}" if r.status_code == 200 else f"{colorama.Fore.RED}"
    
    print(f"""
{b}{colorama.Fore.YELLOW}FIELD               VALUE{reset}
Status code:        {status_code}      
Server response:    {r.content}
Currently on:       {member["firstName"]}

Waiting {b}{colorama.Fore.CYAN}45{reset} seconds...
    """)
    time.sleep(45)