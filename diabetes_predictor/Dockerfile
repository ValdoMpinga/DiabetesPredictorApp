FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["gunicorn", "diabetes_predictor.wsgi:application", "--bind", "0.0.0.0:8000"]
