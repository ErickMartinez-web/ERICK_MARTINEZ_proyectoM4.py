# ERICK_MARTINEZ_proyectoM4.py
Tarea (Modulo 4)

#  Proyecto Pokédex

### Visión General

This project is a command-line Pokédex built in Python. The application interacts with the **[PokéAPI](https://pokeapi.co/)** to obtain Pokémon data in real time.

---

### Características

- **Consumo de API**: It connects to the PokéAPI to search for information about any Pokémon by its name.
- **Manejo de Errores**: Provide clear messages when a Pokémon is not found.
- **Visualización de Datos**:Display the key statistics of the Pokémon (weight, height, movements, skills, and types).
- **Persistencia de Datos**: Save the information of each searched Pokémon in a file, `.json` inside a folder `pokedex`.
- **Organización Profesional**: The code follows the recommendations **PEP 8**, use variable names in English, and is structured modularly with functions.
---

### Módulos, aprendidos y aplicados.

Este proyecto es la culminación de los conocimientos obtenidos en los siguientes módulos de Python:

1.  **Variables, Operadores y Cadenas de Texto**: Utilizados para manejar y formatear la entrada del usuario y la salida de la API.
2.  **Estructuras de Control y Colecciones**: Las estructuras como `if/else`, `while` y colecciones como listas y diccionarios fueron fundamentales para la lógica del programa y para procesar los datos JSON.
3.  **Funciones, Módulos y Paquetes**: La lógica se dividió en funciones claras (`get_pokemon_data`, `save_pokemon_data`), promoviendo la reutilización del código y la legibilidad.
4.  **Manejo de Archivos, Excepciones y Consumo de APIs**: Este es el núcleo del proyecto. Se consumió la PokéAPI utilizando la biblioteca `requests`, se manejaron excepciones (`try-except`) para errores de red o Pokémon no encontrados, y se gestionaron archivos (`.json`) para guardar los datos.

---

### Cómo Ejecutar el Proyecto

Para ejecutar este proyecto, asegúrate de tener Python instalado.

1.  **Clona el repositorio**:
    ```bash
    git clone [https://github.com/tu-usuario/proyecto-pokedex.git](https://github.com/tu-usuario/proyecto-pokedex.git)
    cd proyecto-pokedex
    ```

2.  **Instala la biblioteca necesaria**: El proyecto depende de la biblioteca `requests` para hacer peticiones HTTP. Puedes instalarla con `pip`:
    ```bash
    pip install requests
    ```

3.  **Ejecuta el script principal**:
    ```bash
    python main.py
    ```

Una vez que lo ejecutes, el programa te pedirá que ingreses el nombre de un Pokémon.

---

### Demostración del Resultado:

A continuación, se muestra un ejemplo de cómo se vería la salida en la consola al buscar a "Charizard":


--- Pokémon Data ---
Name: Charizard
Image: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png
--------------------
Stats:
  - Weight: 905 lbs
  - Height: 17 ft

  - Moves:
    mega-punch, fire-punch, thunder-punch, scratch, swords-dance

  - Abilities:
    blaze, solar-power

  - Types:
    fire, flying
--------------------
Después de la ejecución, se creará un archivo `pokedex/pikachu.json` con la información completa.

Saved Pokémon data to `pokedex\charizard.json` successfully!
---------------------

## This project represents a great step in my journey as a developer. Thank you for being a part of it. Your feedback is always welcome.