# 💾 oracle2python - Docker Project

Docker проект для получения данных из oracle базы посредством REST запросов.

* ✨Содержит в себе полноценный API на базе FastAPI
* ✨Поддержка авторизации
* ✨Проприетарное использование


### Использование
`POST` /
```
http://localhost:8000/
```

##### Параметры
``` json
{
    "query" : "SELECT * FROM table_name"
}
```

## Запуск приложения
Для запуска проекта нам необходимо скачать исходники проекта и запустить сборку контейнера
> Для данных дейсвтий необходимо иметь установленный git, а так же иметь доступ к текущему репозиторию


``` bash
# Клонируем репозиторий
git clone https://github.com/ErilovNikita/oracle2python.git

# Заходим в созданную папку
cd oracle2python

# Запускаем сборку докер контейнера
docker-compose up -d --build
```

## Обновление приложения
Для обновления проекта нам необходимо обновить исходники проекта и заного запустить сборку контейнера
> Для данных дейсвтий необходимо иметь установленный git, а так же иметь доступ к текущему репозиторию


``` bash
# Заходим в папку с проектом
cd ~/oracle2python

# Обновляем репозиторий
git pull

# Запускаем пересборку докер контейнера 
docker-compose up -d --no-deps --build
```
