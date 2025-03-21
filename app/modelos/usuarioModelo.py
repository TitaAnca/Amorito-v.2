import json

class UserModel:
    def __init__(self, user_id, name, email, password, age, gender, interested_in, is_active=True):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password  # Se debe encriptar en la lógica de negocio
        self.age = age
        self.gender = gender
        self.interested_in = interested_in
        self.is_active = is_active
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "age": self.age,
            "gender": self.gender,
            "interested_in": self.interested_in,
            "is_active": self.is_active
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return UserModel(**data)