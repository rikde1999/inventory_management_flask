FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /inventory_management_system
WORKDIR /inventory_management_system

COPY requirements.txt /inventory_management_system/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /inventory_management_system/

EXPOSE 8000

CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0 --port=8000"]
