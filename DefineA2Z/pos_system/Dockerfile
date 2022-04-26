FROM python:3.8.10
RUN pip install --upgrade pip
RUN mkdir app
COPY . /app
WORKDIR /app
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000