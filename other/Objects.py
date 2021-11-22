Objects = []
class Form:
    def __init__(self, name, x, y, scale_x, scale_y):
        self.name = name
        self.x = x
        self.y = y
        self.scale_x = scale_x
        self.scale_y = scale_y

def Create_Triangle(x,y,scale_x,scale_y,obj_name):
    global Objects
    newTriangle = Form(obj_name, x, y, scale_x, scale_y)
    objNumber = len(Objects)
    obj_name = obj_name + str(objNumber)
    Objects.append(obj_name)
    objPos = Objects.index(obj_name)
    print("object: ", obj_name, " created edit it on list number: ", objPos) 
    return obj_name

Create_Triangle(4,2,1,1,"test")

    
