FROM python:latest

WORKDIR /src

# RUN pip install jupyterlab
RUN pip install notebook
RUN pip install numpy
RUN pip install matplotlib
RUN pip install pandas
RUN pip install scipy scikit-learn
# RUN jupyter notebook --ip 0.0.0.0 --port 4000 --allow-root

EXPOSE 4000

COPY . /src

CMD [ "python", "perceptron.py" ]
