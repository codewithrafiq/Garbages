FROM python:3-alpine
RUN pip install --upgrade pip
RUN mkdir app
COPY . /app
WORKDIR /app
ENV FLASK_APP=run.py
RUN python3 -m venv tutorial-env
RUN . tutorial-env/bin/activate
RUN pip install -r requirements.txt
CMD flask run --host 0.0.0.0
