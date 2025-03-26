class Mensaje:
    def __init__(self, id_emisor, id_receptor, contenido, timestamp):
        self.id_emisor = id_emisor
        self.id_receptor = id_receptor
        self.contenido = contenido
        self.timestamp = timestamp

    def a_dict(self):
        return {
            "id_emisor": self.id_emisor,
            "id_receptor": self.id_receptor,
            "contenido": self.contenido,
            "timestamp": self.timestamp,
        }