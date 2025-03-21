import json

class ModeloEmparejamiento:
    def __init__(self, id_emparejamiento, usuario_id_1, usuario_id_2, es_coincidencia, fecha_creacion):
        self.id_emparejamiento = id_emparejamiento
        self.usuario_id_1 = usuario_id_1
        self.usuario_id_2 = usuario_id_2
        self.es_coincidencia = es_coincidencia
        self.fecha_creacion = fecha_creacion
    
    def a_diccionario(self):
        return {
            "id_emparejamiento": self.id_emparejamiento,
            "usuario_id_1": self.usuario_id_1,
            "usuario_id_2": self.usuario_id_2,
            "es_coincidencia": self.es_coincidencia,
            "fecha_creacion": self.fecha_creacion
        }
    
    def a_json(self):
        return json.dumps(self.a_diccionario(), indent=4)
    
    @staticmethod
    def desde_json(json_str):
        datos = json.loads(json_str)
        return ModeloEmparejamiento(**datos)