FROM tp33/django

RUN mkdir /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

