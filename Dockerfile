FROM python:3.8

COPY model.pkl model.pkl
COPY requirements.txt requirements.txt
COPY app.py app.py
EXPOSE 5010
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
CMD ["python", "app.py"]