# Create dictionary with user info
user_info = {
    "name": "Morteza",
    "lastname" : "Khalvati",
    "city": "Tabriz",
    "age": 27,
    "field": "Computer Engineer",
    "university": "Tabriz University"
}

# Keys for print values
target_keys = ["name", "field", "university"]

print("#### Student Information ####")
for key, value in user_info.items():
    if key in target_keys:
        print(f"{key}: {value}")
