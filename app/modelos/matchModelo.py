class Match:
    def __init__(self, id_usuario_1, id_usuario_2, estado, datos_match):
        self.id_usuario_1 = id_usuario_1
        self.id_usuario_2 = id_usuario_2
        self.estado = estado
        self.datos_match = datos_match

    def __repr__(self):
        return f"Match({self.id_usuario_1}, {self.id_usuario_2}, {self.estado})"

    def to_dict(self):
        return {
            'id_usuario_1': self.id_usuario_1,
            'id_usuario_2': self.id_usuario_2,
            'estado': self.estado,
            'datos_match': self.datos_match
        }