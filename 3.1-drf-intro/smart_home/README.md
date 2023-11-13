# Умный дом в Docker

## Порядок команд в терминале для запуска проекта

1. ```mkdir hw_docker_django``` <- создаем папку для проекта
2. ```cd hw_docker_django``` <- переходим в созданную папку
3. '''git clone https://github.com/Jeckilla/HW_django_1.git''' <- клонируем проект из гитхаб
4. '''cd HW_django_1/3.1-drf-intro/smart_home''' <- заходим в папку с приложением
5. '''python3 -m venv env''' <- создаем виртуальное окружение
6. '''source env/bin/activate''' <- активируем виртуальное окружение
7. '''sudo apt-get install docker-compose''' <- устанавливаем докер
7. '''pip install -r requirements.txt''' <- устанавливаем зависимости
8. '''cd smart_home''' <- переходим в папку с файлом settings.py
9. '''nano settings.py''' <- корректируем настройки БД на sqlite3
10. '''cd ..''' <- возвращаемся
11. '''nano django_dockerfile''' <- создаем файл с настройками контейнера
12. '''docker build -t django_new_pr:v1 -f django_dockerfile .''' <- создаем контейнер
13. '''docker run -p 8000:8000 django_new_pr:v1''' <- запускаем
