class Libro:
    def __init__(self, titulo, autor, paginas, leidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = leidas

    def leer(self, cantidad):
        if cantidad > 0 and self._progreso + cantidad <= self.paginas:
            self._progreso += cantidad
        else:
            print("Cantidad inválida")

    def progreso(self):
        if self.paginas == 0:
            return 0
        return self._progreso / self.paginas * 100

    def resumen(self):
        return (
            f"{self.titulo} - {self.autor} "
            f"({self.progreso():.0f}%): "
            f"{self._progreso} páginas leídas de {self.paginas}"
        )


l1 = Libro("Pachinko", "Min Jin Lee", 496, 193)
l2 = Libro("El Conde de Monte Cristo", "Alexander Dumas", 1276)

l1.leer(200)
print(l1.progreso())
print(l1.resumen())
print(l2.resumen())