FROM python:3.12.11-slim
WORKDIR /mybackend
COPY . /mybackend/
EXPOSE 8000
RUN pip install -r requirement.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]