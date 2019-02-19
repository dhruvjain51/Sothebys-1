FROM tp33/django

WORKDIR /app

COPY requirements.txt /app/

COPY wait-for-it.sh /app/

COPY db.json /app/

RUN chmod +x wait-for-it.sh

RUN pip install -r requirements.txt

COPY . /app/

