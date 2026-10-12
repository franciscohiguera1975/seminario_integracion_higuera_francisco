Seminario de Integración
Autor: Francisco Higuera

Presentación de la asignatura

Bienvenidos al repositorio de la materia Seminario de Integración.

Este repositorio tiene como propósito consolidar y reforzar los conocimientos adquiridos durante la formación académica mediante el repaso, la práctica y la integración de tecnologías utilizadas en el desarrollo de software moderno.

Durante la asignatura se trabajará con herramientas y tecnologías para el desarrollo backend y frontend, aplicando buenas prácticas de programación, organización de proyectos, gestión de dependencias, construcción de API y desarrollo de interfaces web.

Objetivo general

Fortalecer las competencias técnicas mediante la integración de Python, uv, FastAPI, TypeScript y Angular para desarrollar aplicaciones web estructuradas, mantenibles y escalables.

Objetivos específicos
Repasar los fundamentos de programación con Python.
Gestionar entornos virtuales y dependencias utilizando uv.
Comprender la construcción de API REST con FastAPI.
Reforzar los fundamentos de JavaScript y TypeScript.
Desarrollar interfaces web con Angular.
Integrar servicios backend con aplicaciones frontend.
Aplicar buenas prácticas de organización, documentación y control de versiones con Git.
Tecnologías de estudio
1. Python

Python es un lenguaje de programación de alto nivel, reconocido por su sintaxis clara y su versatilidad. Se utiliza en desarrollo web, automatización, análisis de datos e inteligencia artificial.

Conceptos principales:

Variables y tipos de datos.
Condicionales y estructuras de repetición.
Funciones y módulos.
Listas, tuplas, conjuntos y diccionarios.
Programación orientada a objetos.
Excepciones y manejo de errores.
Módulos, paquetes e importaciones.
Anotaciones de tipos (type hints).

Ejemplo:

def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

print(saludar("Estudiante"))

2. uv

uv es una herramienta rápida para gestionar proyectos, dependencias y entornos de Python. Permite crear proyectos, sincronizar paquetes y administrar entornos virtuales de manera eficiente.

Conceptos principales:

Inicialización de proyectos.
Creación y administración de entornos virtuales.
Instalación y actualización de dependencias.
Gestión de versiones de Python.
Configuración mediante pyproject.toml.
Reproducibilidad de dependencias mediante uv.lock.

Comandos básicos:

# Crear un proyecto
uv init backend

# Ingresar al proyecto
cd backend

# Sincronizar las dependencias
uv sync

# Agregar FastAPI
uv add fastapi

# Agregar Uvicorn
uv add "uvicorn[standard]"

# Ejecutar un archivo Python
uv run main.py


Archivos importantes:

pyproject.toml: define los metadatos, las dependencias y la configuración del proyecto.
uv.lock: registra las versiones resueltas de las dependencias.
.venv/: contiene el entorno virtual local y no debe versionarse en Git.
3. FastAPI

FastAPI es un framework de Python para desarrollar API, especialmente API REST, con soporte para programación asíncrona, validación de datos y generación automática de documentación.

Conceptos principales:

API REST y endpoints.
Métodos HTTP: GET, POST, PUT, PATCH y DELETE.
Parámetros de ruta y consulta.
Modelos de datos con Pydantic.
Validación de solicitudes y respuestas.
Inyección de dependencias.
Manejo de errores y códigos de estado HTTP.
Documentación interactiva con OpenAPI y Swagger UI.

Ejemplo:

from fastapi import FastAPI

app = FastAPI(title="API de Seminario de Integración")

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API"}

@app.get("/estudiantes/{estudiante_id}")
def obtener_estudiante(estudiante_id: int):
    return {
        "id": estudiante_id,
        "estado": "activo"
    }


Ejecutar la aplicación:

uv run uvicorn main:app --reload


Si el archivo se llama main.py, la aplicación estará disponible en:

API: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
4. TypeScript

TypeScript es un lenguaje basado en JavaScript que incorpora un sistema de tipos estáticos. Facilita la detección de errores durante el desarrollo y mejora el mantenimiento de aplicaciones de mayor tamaño.

Conceptos principales:

Tipos primitivos: string, number y boolean.
Arreglos y objetos tipados.
Interfaces y alias de tipos.
Funciones tipadas.
Clases y orientación a objetos.
Uniones de tipos y tipos opcionales.
Genéricos.
Promesas y programación asíncrona.
Módulos e importaciones.

Ejemplo:

interface Estudiante {
  id: number;
  nombre: string;
  activo: boolean;
}

function presentar(estudiante: Estudiante): string {
  return `Estudiante: ${estudiante.nombre}`;
}

const estudiante: Estudiante = {
  id: 1,
  nombre: "Ana",
  activo: true
};

console.log(presentar(estudiante));


TypeScript se transforma a JavaScript para ejecutarse en los entornos correspondientes, como los navegadores web.

5. Angular

Angular es un framework de desarrollo frontend que utiliza TypeScript para construir aplicaciones web estructuradas mediante componentes, plantillas, servicios y herramientas de navegación.

Conceptos principales:

Componentes y plantillas.
Directivas y enlace de datos (data binding).
Servicios e inyección de dependencias.
Enrutamiento con Angular Router.
Formularios reactivos y basados en plantillas.
Comunicación HTTP con HttpClient.
Observables y programación reactiva con RxJS.
Interfaces y modelos de TypeScript.
Componentes independientes (standalone).
Construcción y despliegue de aplicaciones.

Ejemplo de un componente:

import { Component } from '@angular/core';

@Component({
  selector: 'app-bienvenida',
  standalone: true,
  template: `
    <h1>{{ mensaje }}</h1>
  `
})
export class BienvenidaComponent {
  mensaje = 'Bienvenidos a Seminario de Integración';
}


Comandos básicos:

# Crear una aplicación Angular
ng new frontend

# Ingresar a la aplicación
cd frontend

# Ejecutar el servidor de desarrollo
ng serve


La instalación de Angular CLI y los requisitos de Node.js deben verificarse antes de crear el proyecto.

Integración de tecnologías

El propósito final es comprender cómo se complementan estas herramientas dentro de una aplicación web.

┌──────────────────────────────────────┐
│              FRONTEND                │
│                                      │
│        Angular + TypeScript          │
│                                      │
│  Componentes, formularios y vistas   │
└──────────────────┬───────────────────┘
                   │
                   │ HTTP / JSON
                   ▼
┌──────────────────────────────────────┐
│               BACKEND                │
│                                      │
│           FastAPI + Python           │
│                                      │
│  Endpoints, validación y lógica       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          DATOS Y SERVICIOS           │
│                                      │
│  Persistencia e integración externa  │
└──────────────────────────────────────┘


En esta arquitectura:

Angular construye la interfaz que utiliza el usuario.
TypeScript aporta tipado y estructura al código frontend.
FastAPI expone los endpoints que permiten intercambiar información.
Python implementa la lógica de negocio del backend.
uv administra las dependencias y el entorno de desarrollo de Python.
HTTP y JSON permiten la comunicación entre frontend y backend.
Estructura sugerida del repositorio

La siguiente estructura permite organizar los ejercicios, las prácticas y los proyectos de la asignatura.

seminario-integracion/
├── README.md
├── .gitignore
├── docs/
│   └── apuntes.md
├── python/
│   ├── fundamentos/
│   ├── funciones/
│   └── poo/
├── backend/
│   ├── pyproject.toml
│   ├── uv.lock
│   └── app/
│       ├── main.py
│       ├── routers/
│       ├── schemas/
│       └── services/
├── typescript/
│   ├── fundamentos/
│   └── ejercicios/
└── frontend/
    └── angular-app/


La estructura es orientativa y puede adaptarse a las actividades definidas durante el semestre. Cada proyecto puede contener sus propias configuraciones y dependencias.

Requisitos previos

Para desarrollar las prácticas se recomienda disponer de las siguientes herramientas:

Python: intérprete compatible con la versión requerida por cada proyecto.
uv: gestión de entornos y dependencias de Python.
Node.js: entorno de ejecución necesario para las herramientas de Angular.
Angular CLI: herramientas de creación y desarrollo de aplicaciones Angular.
Git: control de versiones del código fuente.
Visual Studio Code u otro editor de código.

Las versiones específicas se definirán según los requisitos de cada práctica.

Buenas prácticas de trabajo
Mantener una estructura clara de carpetas y subproyectos.
Utilizar nombres descriptivos para archivos, funciones, clases y variables.
Documentar las funciones y los endpoints relevantes.
Gestionar las dependencias de Python con uv.
Versionar pyproject.toml y uv.lock cuando correspondan al proyecto.
Mantener package.json y el archivo lock del gestor de paquetes del frontend.
Evitar subir entornos virtuales, carpetas node_modules, compilaciones y archivos temporales.
No publicar contraseñas, tokens, claves privadas ni archivos .env con secretos.
Utilizar Git para registrar avances y cambios.
Probar los endpoints del backend y su integración con el frontend.
Resultados de aprendizaje esperados

Al finalizar el trabajo de la asignatura, se espera que el estudiante pueda:

Aplicar los fundamentos de Python en ejercicios y aplicaciones.
Gestionar proyectos y dependencias con uv.
Diseñar e implementar API REST con FastAPI.
Crear modelos de datos y validar solicitudes.
Desarrollar componentes e interfaces con Angular y TypeScript.
Consumir servicios backend desde una aplicación frontend.
Organizar, documentar y versionar proyectos de software.
Integrar tecnologías para construir una solución funcional.
Organización sugerida de la asignatura
Bloque	Contenido
1	Repaso de fundamentos de Python
2	Gestión de proyectos, entornos y dependencias con uv
3	Desarrollo de API REST con FastAPI
4	Fundamentos de TypeScript
5	Componentes, servicios y rutas con Angular
6	Integración de Angular con FastAPI
7	Desarrollo y presentación del proyecto integrador
Conclusión

El repositorio de Seminario de Integración constituye un espacio de aprendizaje práctico para reforzar conocimientos, resolver problemas y desarrollar competencias de integración de tecnologías.

El trabajo progresivo permitirá pasar de ejercicios individuales de programación a aplicaciones que conecten un backend desarrollado con Python y FastAPI con un frontend construido mediante Angular y TypeScript.

Asignatura: Seminario de Integración
Enfoque: Repaso, desarrollo e integración de tecnologías
Tecnologías principales: Python · uv · FastAPI · TypeScript · Angular
Control de versiones: Git