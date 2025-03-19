location=[("New york",(40.7128,-74.0064))
("Tokyo",(35.6895,139.6917))
("Delhi",(28.7041,77.1025))]

def get_location(city):
    for  for_name,word in location:
        if city ==for_name:
            return word

        city="Berlin"
        coordinates=get_location(city)

        if coordinates:
            print(f"The coordinates for {city} are {coordinates}")
        else:
            print(f"Coordinates for {city} not found")
