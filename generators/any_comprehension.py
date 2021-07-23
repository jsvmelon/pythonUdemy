from data import people, plants_list, plants_dict

# make sure people are not empty too
if bool(people) and all(person[1] for person in people):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# mini challenge
if bool(plants_dict.values()) and any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("Grass in dict")
else:
    print("No grass in dict")

# variant
if bool(plants_dict.values()) and any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("Grass in dict")
else:
    print("No grass in dict")
