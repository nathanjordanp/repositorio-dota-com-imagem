class Heroes:
    def __init__(self, id, name, role, description, image):
        self.id = id
        self.name = name
        self.role = role
        self.description = description
        self.image = image

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_role(self):
        return self.role
    
    def get_description(self):
        return self.description
    
    def get_image(self):
        return self.image
    
        