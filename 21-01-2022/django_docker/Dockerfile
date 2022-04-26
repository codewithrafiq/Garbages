FROM python:3-alpine
RUN pip install --upgrade pip
RUN mkdir app
COPY . /app
WORKDIR /app
RUN python3 -m venv tutorial-env
RUN . tutorial-env/bin/activate
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py migrate_all_db
CMD python3 manage.py runserver 0.0.0.0:8000