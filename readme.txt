Инструкция по установке.
	1.Клонируйте репозиторий.
	2.Создайте и включите virtualenv
	3.Установите нужный модули из req.txt находящегося корневой папки проекта
		pip install -r SPost/req.txt
	4.Сделайте миграцию моделей.
		python manage.py makemigrations
		python manage.py migrate
	5.Создайте супер юзера
		python manage.py createsuperuser
	6.Соберите статические файлы.
		python manage.py collectstatic
	7.Запустите сервер.
		python manage.py runserver

Ссылки для проверки UI:

/auth - для авторизации
/posts_list - Для создания постов

для запуска бота использовать следующую команду из корневой директории проекта
python manage.py <number_of_users> <max_posts_per_user> <max_likes_per_user> <optional:host_link>
