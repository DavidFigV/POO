  // Clase base: Persona
  class Persona {
    String nombre;
    int edad;

    // Constructor
    Persona(this.nombre, this.edad);

    // Método: presentarse
    void presentarse() {
      print("Hola, me llamo $nombre y tengo $edad años.");
    }
  }

  // Clase Estudiante (hereda de Persona)
  class Estudiante extends Persona {
    String grado;
    double _promedio; // Atributo encapsulado

    // Constructor
    Estudiante(String nombre, int edad, this.grado, this._promedio)
        : super(nombre, edad);

    // Getter y Setter para promedio
    double get promedio => _promedio;

    set promedio(double nuevoPromedio) {
      if (nuevoPromedio >= 0 && nuevoPromedio <= 10) {
        _promedio = nuevoPromedio;
      } else {
        print("Promedio inválido, debe estar entre 0 y 10.");
      }
    }

    // Sobrescribir el método presentarse
    @override
    void presentarse() {
      print(
          "Soy $nombre, tengo $edad años, estudio en el grado $grado, y mi promedio es $_promedio.");
    }

    // Método: estudiar
    void estudiar() {
      print("$nombre está estudiando para mejorar su promedio.");
    }
  }

  // Clase Profesor (hereda de Persona)
  class Profesor extends Persona {
    String materia;
    int experiencia; // Años de experiencia

    // Constructor
    Profesor(String nombre, int edad, this.materia, this.experiencia)
        : super(nombre, edad);

    // Sobrescribir el método presentarse
    @override
    void presentarse() {
      print(
          "Soy $nombre, tengo $edad años, enseño $materia, y tengo $experiencia años de experiencia.");
    }

    // Método: enseñar
    void ensenar() {
      print("$nombre está enseñando $materia.");
    }
  }

  // Función genérica que utiliza polimorfismo
  void interactuarConPersona(Persona persona) {
    persona.presentarse(); // Polimorfismo: se llama el método adecuado según el tipo del objeto

    if (persona is Estudiante) {
      persona.estudiar(); // Uso de un método específico de Estudiante
    } else if (persona is Profesor) {
      persona.ensenar(); // Uso de un método específico de Profesor
    }
  }

  // Programa principal
  void main() {
    // Creando objetos
    Estudiante estudiante1 = Estudiante("David", 23, "2do Cuatrimestre", 9.4);
    Estudiante estudiante2 = Estudiante("Dario", 18, "2do Cuatrimestre", 9.0);
    Profesor profesor = Profesor("Mtro. Kevin Porter", 34, "Fundamentos de Redes", 10);

    
    // Llamando al método genérico
    interactuarConPersona(estudiante1);
    // Usando métodos
    estudiante1.promedio = 9.5; // Usando el setter
    print("Nuevo promedio para ${estudiante1.nombre}: ${estudiante1.promedio}");

    print("");
    interactuarConPersona(estudiante2);
    print("");
    interactuarConPersona(profesor);
  }
