household = {
    "number":4,
    "person":
    [
        {"name":"Praveen Poosapati", "age":"36", "email":"praveenpoosapati@gmail.com", "phone#":"940-293-7718"},
        {"name":"Vineela Gottimukkala", "age":"29", "email":"vineela517@gmail.com", "phone#":"636-541-3019"},
        {"name":"Shanvith Varma Poosapati", "age":"1", "email":"tbd@gmail.com", "phone#":"tbd"},
        {"name":"Leo Poosapati", "age":"7", "email":"nyd@gmail.com", "phone#":"nyd"}
    ]

}

for person in household["person"]:
    if int(person.get("age")) < 30:
        if int(person.get("age")) < 10: 
            print(person.get("name") + " is a sweety... :)")
        else:
            print(person.get("name") + " is young...")
    else:
        print(person.get("name") + " is too old... :(") 