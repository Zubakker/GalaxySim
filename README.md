# GalaxySim
This is a repository of two python programs
1) designer.py is used to create new objects (planets)
   PRO TIP: to delete object, click in the red zone, then type "DELETE" in the terminal and then type the object number
2) simulator.py is used to simulate physics behind those objects

Both programs save their data to the file OBJECTS.json, which is an array of dictionaries. Each dictionary represents an object.
The dictionary has this keys: "COORDS": {float, float}, "SIZE": float <- it is the radius of the circle, "MASS": float and lastly "SPEED": {float, float} <- x and y directions
