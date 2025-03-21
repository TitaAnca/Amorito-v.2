import json

class ModeloMensaje:
    def __init__(self, id_mensaje, remitente_id, receptor_id, contenido, fecha_envio):
        self.id_mensaje = id_mensaje
        self.remitente_id = remitente_id
        self.receptor_id = receptor_id
        self.contenido = contenido
        self.fecha_envio = fecha_envio
    
    def a_diccionario(self):
        return {
            "id_mensaje": self.id_mensaje,
            "remitente_id": self.remitente_id,
            "receptor_id": self.receptor_id,
            "contenido": self.contenido,
            "fecha_envio": self.fecha_envio
        }
    
    def a_json(self):
        return json.dumps(self.a_diccionario(), indent=4)
    
    @staticmethod
    def desde_json(json_str):
        datos = json.loads(json_str)
        return ModeloMensaje(**datos)