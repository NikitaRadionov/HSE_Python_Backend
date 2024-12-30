PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS := venv/bin/pytest -v ./test_controllers.py

# Удаление виртуального окружения
clear:
	rm -rf venv

# Создание виртуального окружения
venv:
	python3 -m venv venv

# Установка зависимостей
install_requirements: venv
	${PIP} install --upgrade pip
	${PIP} install -r requirements.txt

# Запуск тестов
test: venv install_requirements
	${TESTS}

# Запуск сервера
run: venv install_requirements
	${PYTHON3} server.py
