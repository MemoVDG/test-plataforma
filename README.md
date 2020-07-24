# API para obtener productos con DJANGO

Entorno de desarrollo
  - Python 3.8
  - Django 3.0.8

# Instalacion
* Es recomendable [crear un virtualenv para poder correr el proyecto](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

* Una vez dentro del ambiente virtual con [pip](https://pip.pypa.io/en/stable/) en la consola escribimos para instalar las depenciencias necesarias

```bash
pip install -r requirements.tx
```

* En el archivo setting.py configuramos las credenciales de la base de datos

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'products',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

* Creamos las migraciones hacia la base de datos

```bash
python manage.py migrate
```

* Corremos la aplicación
```bash
python manage.py runserver
```

# Consultas
* Para hacer consultas se puede [descargar el paquete de postman y cargar las colecciones](https://www.getpostman.com/collections/dea75d01c85cc2bc1f6c)


* Endpoints
    * Crear producto

```bash
http://127.0.0.1:8000/api/products/bulk_insert
```

![Add information](https://res.cloudinary.com/memovdg/image/upload/v1595615576/1_evwen0.png)


    Los datos deben ir en el body en un formato

```bash
{
    "products":[
        {
            "name": "Dulces",
            "value": 50,
            "discount_value": 60,
            "stock": 2
        },
        {
            "name": "Dulce con chile",
            "value": 20.5,
            "discount_value": 10,
            "stock": 5
        }
    ]
}
```

* Listar productos

```bash
http://127.0.0.1:8000/api/products
```

![Add information](https://res.cloudinary.com/memovdg/image/upload/v1595615949/2_nphja8.png)






# Correr pruebas

Para correr los testnos posicionamos dentro de la terminal y escribimos

```bash
python manage.py test productos
```


# Tareas del ejercicio
🟩 ~~Creacion del API/endpoint.~~

🟩 ~~Modelado y arquitectura de los objetos.~~

🟩 ~~Guardado de los productos en base de datos.~~

🟩 ~~Testing de los modelos y el endpoint.~~

🟩 Deployment a AWS.



## License
[MIT](https://choosealicense.com/licenses/mit/)
