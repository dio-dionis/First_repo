cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"]="simon"
cat["age"]=7
cat['characteristics']=["лагідний", "кусається"]
age = cat.get("age")
cat.update(info)
print(cat)
print(age)