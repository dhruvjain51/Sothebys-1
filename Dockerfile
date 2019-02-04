FROM tp33/django

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

ENV MYSQL_ROOT_PASSWORD="$3cureUS"

COPY . /app/

