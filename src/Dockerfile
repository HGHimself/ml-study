FROM python:latest

WORKDIR /src

# RUN pip install jupyterlab
RUN pip install notebook
RUN pip install numpy
RUN pip install matplotlib
# RUN jupyter notebook --host 0.0.0.0 --port 4000

EXPOSE 4000

COPY . /src

CMD [ "python", "perceptron.py" ]
