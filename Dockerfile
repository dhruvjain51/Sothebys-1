FROM tp33/django

WORKDIR /app

COPY requirements.txt /app/

COPY wait-for-it.sh

ENTRYPOINT chmod +x wait-for-it.sh

RUN pip install -r requirements.txt

COPY . /app/

