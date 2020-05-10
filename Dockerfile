FROM python:3.8.2
MAINTAINER Priyanka Gurung
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]