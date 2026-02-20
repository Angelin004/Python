class goa:
    name=""
    extrovert=""
    def party(self):
        print("lets party....!")
    def beach(self):
        print("enjoying the beach")

sutakar=goa()
jegan=goa()

sutakar.party()
jegan.beach()

sutakar.extrovert="yes"
jegan.extrovert="no"

sutakar.name=sutakar
jegan.name=jegan

print(sutakar.name)
print("extrovert:", sutakar.extrovert)
print(jegan.name)
print("extrovert:", jegan.extrovert)