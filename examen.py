import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
                             QPushButton, QMessageBox, QButtonGroup, QStackedLayout, QGroupBox)
from PyQt5.QtCore import QTimer
import random

preguntas = [
    {"tipo": "TF", "pregunta": "En Python, las variables deben declararse con un tipo de dato específico, como en C o Java.", "respuesta": False},
    {"tipo": "TF", "pregunta": "El operador == se utiliza para comparar si dos valores son iguales.", "respuesta": True},
    {"tipo": "TF", "pregunta": "Las listas en Python son inmutables.", "respuesta": False},
    {"tipo": "TF", "pregunta": "El índice de la primera posición de una lista en Python es 1.", "respuesta": False},
    {"tipo": "TF", "pregunta": "Python es un lenguaje compilado.", "respuesta": False},
    {"tipo": "TF", "pregunta": "Python fue creado por Guido van Rossum.", "respuesta": True},
    {"tipo": "TF", "pregunta": "Python no soporta programación orientada a objetos.", "respuesta": False},
    {"tipo": "TF", "pregunta": "La palabra clave 'def' se usa para definir funciones en Python.", "respuesta": True},
    {"tipo": "TF", "pregunta": "Los diccionarios en Python se definen con corchetes [].", "respuesta": False},
    {"tipo": "TF", "pregunta": "Una clase en Python se define con la palabra clave 'class'.", "respuesta": True},
    {"tipo": "TF", "pregunta": "El código escrito en Python3 funciona en un entorno con Python2.", "respuesta": False},
    {"tipo": "TF", "pregunta": "La variable _Humedad maracaría error.", "respuesta": False},
    {"tipo": "TF", "pregunta": "La variable _Humedad maracaría error.", "respuesta": False},
    {"tipo": "TF", "pregunta": "La estructura de control while permite ejecutar repetidamente un bloque de código mientras una condición sea verdadera.", "respuesta": True},
    {"tipo": "MC", "pregunta": "¿Quién creó Python?", 
     "opciones": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"], "respuesta": 1},
    {"tipo": "MC", "pregunta": "¿Cuál es el tipo de dato inmutable en Python?", 
     "opciones": ["Lista", "Diccionario", "Tupla", "Conjunto"], "respuesta": 2},
    {"tipo": "MC", "pregunta": "¿Cómo se define una función en Python?", 
     "opciones": ["function", "def", "func", "define"], "respuesta": 1},
    {"tipo": "MC", "pregunta": "¿Qué tipo de dato es Falso?", 
     "opciones": ["Entero", "Cadena", "Flotante", "Booleano"], "respuesta": 3},

     {"tipo": "MC", "pregunta": "Es un símbolo o palabra que especifica que una operación va a ser ejecutada", 
     "opciones": ["Operador", "Variable", "Clase", "Función"], "respuesta": 0},

     {"tipo": "MC", "pregunta": "Su finalidad es ejecutar un código que será reutilizado", 
     "opciones": ["Operador", "Variable", "Clase", "Función"], "respuesta": 3},

     {"tipo": "MC", "pregunta": "Es un símbolo o palabra que especifica que una operación va a ser ejecutada", 
     "opciones": ["Operador", "Variable", "Clase", "Función"], "respuesta": 0},

     {"tipo": "MC", "pregunta": "Es un espacio en memoria para almacenar datos", 
     "opciones": ["Operador", "Variable", "Clase", "Función"], "respuesta": 1},

     {"tipo": "MC", "pregunta": " Es un molde o plantilla que define las características (atributos) y comportamientos (métodos) que tendrán los objetos que se creen a partir de ella", 
     "opciones": ["Operador", "Variable", "Clase", "Función"], "respuesta": 2},

     {"tipo": "MC", "pregunta": " ¿Con que palabra se pueden  usar las librerias estandar de python?", 
     "opciones": ["Import", "from", "def", "for"], "respuesta": 0},

     {"tipo": "MC", "pregunta": "Son las propiedades de los objetos en POO", 
     "opciones": ["Atributos", "Módulos", "Métodos", "Paradigmas"], "respuesta": 0},

     {"tipo": "MC", "pregunta": "Son las acciones de los objetos", 
     "opciones": ["Atributos", "Módulos", "Métodos", "Paradigmas"], "respuesta": 2},

     {"tipo": "MC", "pregunta": " Ayudan a organizar el código en diferentes archivos y a que sea más fácil de entender", 
     "opciones": ["Atributos", "Módulos", "Métodos", "Paradigmas"], "respuesta": 1},


     {"tipo": "MC", "pregunta": " Elimina un elemento de la lista  por su index", 
     "opciones": ["remove()", "pop()", "sort", "append()"], "respuesta": 1},

     {"tipo": "MC", "pregunta": " Agrega un elemento al final de la lista", 
     "opciones": ["remove()", "pop()", "sort", "append()"], "respuesta": 1},



    {"tipo": "MC", "pregunta": "¿Qué palabra clave se usa para crear una clase en Python?", 
     "opciones": ["def", "class", "struct", "object"], "respuesta": 1}
]

class Bienvenida(QWidget):
    def __init__(self, iniciar_callback):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Bienvenido al Examen Final\n\nHaz clic en 'Iniciar' para comenzar. Tienes 2 horas para completar el examen.")
        self.layout.addWidget(self.label)
        self.boton_iniciar = QPushButton("Iniciar")
        self.boton_iniciar.clicked.connect(iniciar_callback)
        self.layout.addWidget(self.boton_iniciar)
        self.setLayout(self.layout)

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen de Final de Programación Básica")
        self.setGeometry(200, 200, 700, 400)

        self.stack = QStackedLayout()
        self.setLayout(self.stack)

        self.bienvenida = Bienvenida(self.comenzar_examen)
        self.stack.addWidget(self.bienvenida)

        self.quiz_widget = QWidget()
        self.quiz_layout = QVBoxLayout()

        self.timer_label = QLabel("Tiempo restante: 7200 segundos")
        self.quiz_layout.addWidget(self.timer_label)

        self.pregunta_label = QLabel()
        self.quiz_layout.addWidget(self.pregunta_label)

        self.true_radio = QRadioButton("Verdadero")
        self.false_radio = QRadioButton("Falso")
        self.tf_group = QButtonGroup()
        self.tf_group.addButton(self.true_radio)
        self.tf_group.addButton(self.false_radio)

        self.opcion_groupbox = QGroupBox("Opciones")
        self.opcion_layout = QVBoxLayout()
        self.opcion_rbs = []
        self.opcion_group = QButtonGroup()
        self.opcion_groupbox.setLayout(self.opcion_layout)

        self.quiz_layout.addWidget(self.true_radio)
        self.quiz_layout.addWidget(self.false_radio)
        self.quiz_layout.addWidget(self.opcion_groupbox)

        self.siguiente_btn = QPushButton("Siguiente")
        self.siguiente_btn.clicked.connect(self.validar_respuesta)
        self.regresar_btn = QPushButton("Regresar")
        self.regresar_btn.clicked.connect(self.regresar_pregunta)

        self.quiz_layout.addWidget(self.siguiente_btn)
        self.quiz_layout.addWidget(self.regresar_btn)

        self.quiz_widget.setLayout(self.quiz_layout)
        self.stack.addWidget(self.quiz_widget)

        self.pregunta_actual = 0
        self.puntaje = 0
        self.respuestas_incorrectas = []

        self.preguntas = []
        self.tiempo_restante = 7200
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_temporizador)


    def comenzar_examen(self):
        self.preguntas = preguntas.copy()
        random.shuffle(self.preguntas)
        self.stack.setCurrentWidget(self.quiz_widget)
        self.mostrar_pregunta()
        self.timer.start(1000)

    def mostrar_pregunta(self):
        self.tf_group.setExclusive(False)
        self.true_radio.setChecked(False)
        self.false_radio.setChecked(False)
        self.tf_group.setExclusive(True)

        self.opcion_group.setExclusive(False)
        for rb in self.opcion_rbs:
            self.opcion_layout.removeWidget(rb)
            rb.deleteLater()
        self.opcion_rbs = []
        self.opcion_group.setExclusive(True)

        pregunta = self.preguntas[self.pregunta_actual] 
        self.pregunta_label.setText(f"Pregunta {self.pregunta_actual + 1}: {pregunta['pregunta']}")

        if pregunta["tipo"] == "TF":
            self.true_radio.show()
            self.false_radio.show()
            self.opcion_groupbox.hide()
        elif pregunta["tipo"] == "MC":
            self.true_radio.hide()
            self.false_radio.hide()
            self.opcion_groupbox.show()
            for i, opcion in enumerate(pregunta["opciones"]):
                rb = QRadioButton(opcion)
                self.opcion_rbs.append(rb)
                self.opcion_group.addButton(rb, i)
                self.opcion_layout.addWidget(rb)

    def validar_respuesta(self):
        pregunta = self.preguntas[self.pregunta_actual]
        respuesta_usuario = None

        if pregunta["tipo"] == "TF":
            if self.true_radio.isChecked():
                respuesta_usuario = True
            elif self.false_radio.isChecked():
                respuesta_usuario = False
            else:
                QMessageBox.warning(self, "Aviso", "Por favor selecciona una respuesta.")
                return
            correcta = pregunta["respuesta"]
            if respuesta_usuario == correcta:
                self.puntaje += 1
            else:
                self.respuestas_incorrectas.append((pregunta["pregunta"], str(correcta), str(respuesta_usuario)))

        elif pregunta["tipo"] == "MC":
            seleccionado = self.opcion_group.checkedId()
            if seleccionado == -1:
                QMessageBox.warning(self, "Aviso", "Por favor selecciona una opción.")
                return
            correcta = pregunta["respuesta"]
            if seleccionado == correcta:
                self.puntaje += 1
            else:
                seleccionada = pregunta["opciones"][seleccionado]
                self.respuestas_incorrectas.append((pregunta["pregunta"], pregunta["opciones"][correcta], seleccionada))

        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            self.terminar_examen()

    def regresar_pregunta(self):
        if self.pregunta_actual > 0:
            self.pregunta_actual -= 1
            self.mostrar_pregunta()
        else:
            QMessageBox.information(self, "Aviso", "Ya estás en la primera pregunta.")

    def actualizar_temporizador(self):
        self.tiempo_restante -= 1
        self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante} segundos")
        if self.tiempo_restante == 0:
            self.terminar_examen()

    def terminar_examen(self):
        self.timer.stop()
        calificacion = (self.puntaje / len(self.preguntas)) * 10
        resumen = f"Examen finalizado.\n\nRespuestas correctas: {self.puntaje} de {len(preguntas)}\nCalificación: {calificacion:.2f}/10\n"
        if self.respuestas_incorrectas:
            resumen += "\nPreguntas incorrectas:\n"
            for pregunta, correcta, seleccionada in self.respuestas_incorrectas:
                resumen += f"- {pregunta}\n  Respuesta correcta: {correcta}\n  Tu respuesta: {seleccionada}\n"

        QMessageBox.information(self, "Resultado", resumen)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec_())