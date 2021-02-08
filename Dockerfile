FROM arm32v7/python
RUN pip install -U pip
COPY ./app /app
WORKDIR /app
RUN cd /app && pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]