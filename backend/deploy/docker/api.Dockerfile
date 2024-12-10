FROM python:3.12.3

EXPOSE 7070

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH="${PYTHONPATH}:/project/src"

COPY requirements.txt .

RUN apt-get update && rm -rf /var/lib/apt/lists/*  &&  apt-get clean
RUN pip install -r requirements.txt

COPY src src

CMD ["sh", "-c", "python src/main.py"]