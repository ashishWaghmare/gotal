FROM python:rc-alpine
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
#ENTRYPOINT ["FLASK_APP=app.py","flask","run"]
ENTRYPOINT ["python"]
CMD ["app.py"]
