FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ADD . /
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]