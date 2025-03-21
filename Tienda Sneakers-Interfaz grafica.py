from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QInputDialog, QMessageBox
import sys


class SneakerManager(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialización de la lista de sneakers
        self.sneakers_list = [
            {'nombre': 'Nike Air Force 1', 'marca': 'Nike', 'precio': 2500.0, 'stock': 10, 'ID': 1},
            {'nombre': 'Adidas Superstar', 'marca': 'Adidas', 'precio': 2200.0, 'stock': 5, 'ID': 2},
            {'nombre': 'Puma RS-X', 'marca': 'Puma', 'precio': 2700.0, 'stock': 0, 'ID': 3}
        ]

        self.setWindowTitle("Gestor de Sneakers 👟")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        # Crear botones y asignarles sus funciones
        btn_agregar = QPushButton("📥 Dar de Alta Modelo Nuevo")
        btn_agregar.clicked.connect(self.agregar_sneaker)
        layout.addWidget(btn_agregar)

        btn_baja = QPushButton("❌ Dar de Baja Modelo Viejo")
        btn_baja.clicked.connect(self.baja_sneaker)
        layout.addWidget(btn_baja)

        btn_modificar = QPushButton("✏️ Modificar Modelo Existente")
        btn_modificar.clicked.connect(self.modificar_sneaker)
        layout.addWidget(btn_modificar)

        btn_consultar = QPushButton("🔍 Consultar Modelos Disponibles")
        btn_consultar.clicked.connect(self.consultar_sneakers)
        layout.addWidget(btn_consultar)

        btn_salir = QPushButton("🚪 Salir")
        btn_salir.clicked.connect(self.close)
        layout.addWidget(btn_salir)

        self.setLayout(layout)

    def imprimir_sneakers(self, sneakers):
        lista_str = ""
        for sneaker in sneakers:
            lista_str += f"{sneaker['ID']}. {sneaker['nombre']} ({sneaker['marca']}) - Precio: ${sneaker['precio']} - Stock: {sneaker['stock']} unidades\n"
        return lista_str

    def agregar_sneaker(self):
        nombre, ok = QInputDialog.getText(self, "Agregar Modelo 📝", "Nombre del modelo:")
        if not ok or not nombre:
            return

        marca, ok = QInputDialog.getText(self, "Agregar Modelo 📝", "Marca del modelo:")
        if not ok or not marca:
            return

        precio, ok = QInputDialog.getDouble(self, "Agregar Modelo 💵", "Precio del modelo:")
        if not ok:
            return

        stock, ok = QInputDialog.getInt(self, "Agregar Modelo 📦", "Stock disponible:")
        if not ok:
            return

        # Asignación del ID secuencial
        new_id = len(self.sneakers_list) + 1

        nuevo_sneaker = {
            'nombre': nombre,
            'marca': marca,
            'precio': precio,
            'stock': stock,
            'ID': new_id
        }
        self.sneakers_list.append(nuevo_sneaker)

        QMessageBox.information(self, "✅ Éxito", f"Modelo {nombre} agregado con éxito.")

    def baja_sneaker(self):
        ids = [str(sneaker['ID']) for sneaker in self.sneakers_list]
        id_baja, ok = QInputDialog.getItem(self, "Dar de Baja Modelo ❌", "Selecciona el modelo a dar de baja:", ids, 0, False)
        if ok:
            id_baja = int(id_baja)
            for sneaker in self.sneakers_list:
                if sneaker['ID'] == id_baja:
                    self.sneakers_list.remove(sneaker)
                    QMessageBox.information(self, "✅ Éxito", f"Modelo con ID {id_baja} dado de baja.")
                    return
            QMessageBox.warning(self, "⚠️ Error", "El modelo con el ID seleccionado no existe.")

    def modificar_sneaker(self):
        ids = [str(sneaker['ID']) for sneaker in self.sneakers_list]
        id_modificar, ok = QInputDialog.getItem(self, "Modificar Modelo ✏️", "Selecciona el modelo a modificar:", ids, 0, False)
        if ok:
            id_modificar = int(id_modificar)
            for sneaker in self.sneakers_list:
                if sneaker['ID'] == id_modificar:
                    self.modificar_atributo(sneaker)
                    return
            QMessageBox.warning(self, "⚠️ Error", "El modelo con el ID seleccionado no existe.")

    def modificar_atributo(self, sneaker):
        opciones = ["Nombre ✨", "Marca 🏷️", "Precio 💲", "Stock 📦"]
        opcion, ok = QInputDialog.getItem(self, "Modificar Atributo ✏️", "Selecciona el atributo a modificar:", opciones, 0, False)
        if ok:
            if opcion == "Nombre ✨":
                nuevo_nombre, ok = QInputDialog.getText(self, "Modificar Nombre ✨", "Nuevo nombre del modelo:")
                if ok and nuevo_nombre:
                    sneaker['nombre'] = nuevo_nombre
            elif opcion == "Marca 🏷️":
                nueva_marca, ok = QInputDialog.getText(self, "Modificar Marca 🏷️", "Nueva marca del modelo:")
                if ok and nueva_marca:
                    sneaker['marca'] = nueva_marca
            elif opcion == "Precio 💲":
                nuevo_precio, ok = QInputDialog.getDouble(self, "Modificar Precio 💲", "Nuevo precio del modelo:")
                if ok:
                    sneaker['precio'] = nuevo_precio
            elif opcion == "Stock 📦":
                nuevo_stock, ok = QInputDialog.getInt(self, "Modificar Stock 📦", "Nuevo stock disponible:")
                if ok:
                    sneaker['stock'] = nuevo_stock

            QMessageBox.information(self, "✅ Éxito", f"Modelo {sneaker['nombre']} modificado correctamente.")

    def consultar_sneakers(self):
        opciones = ["1. Ordenados por precio (de mayor a menor) 📉", "2. Ordenados por marca 🔠", "3. Imprimir todo por ID 🆔"]
        opcion, ok = QInputDialog.getItem(self, "Consultar Sneaker 🔍", "Selecciona cómo deseas consultar los sneakers:", opciones, 0, False)
        if ok:
            # Filtrar sneakers con stock disponible
            sneakers_disponibles = [sneaker for sneaker in self.sneakers_list if sneaker["stock"] > 0]
            if not sneakers_disponibles:
                QMessageBox.warning(self, "⚠️ No hay sneakers", "No hay sneakers disponibles en stock.")
                return

            if opcion == "1. Ordenados por precio (de mayor a menor) 📉":
                sneakers_ordenados = sorted(sneakers_disponibles, key=lambda x: x["precio"], reverse=True)
                consulta_str = "Sneakers ordenados por precio (de mayor a menor):\n" + self.imprimir_sneakers(sneakers_ordenados)
            elif opcion == "2. Ordenados por marca 🔠":
                sneakers_ordenados = sorted(sneakers_disponibles, key=lambda x: x["marca"].lower())
                consulta_str = "Sneakers ordenados por marca:\n" + self.imprimir_sneakers(sneakers_ordenados)
            elif opcion == "3. Imprimir todo por ID 🆔":
                consulta_str = "Todos los sneakers por ID:\n" + self.imprimir_sneakers(self.sneakers_list)
            else:
                consulta_str = "Opción no válida."

            QMessageBox.information(self, "Consulta de Sneakers 🔍", consulta_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SneakerManager()
    ventana.show()
    sys.exit(app.exec())