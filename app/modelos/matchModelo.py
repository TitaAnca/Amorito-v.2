class Match:
    def __init__(self, id_usuario_1, id_usuario_2, estado, datos_match):
        self.id_usuario_1 = id_usuario_1
        self.id_usuario_2 = id_usuario_2
        self.estado = estado  # 'pendiente', 'aceptado', 'rechazado'
        self.datos_match = datos_match  # Contiene la compatibilidad de edades, géneros y preferencias

    def __repr__(self):
        return f"Match({self.id_usuario_1}, {self.id_usuario_2}, {self.estado})"
