FROM python:latest

WORKDIR /src

RUN pip install numpy
RUN pip install matplotlib

COPY . /src

CMD [ "python", "perceptron.py" ]
