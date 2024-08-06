FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /Employee

COPY requirements.txt /Employee/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /Employee/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]