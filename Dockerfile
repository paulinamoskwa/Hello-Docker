FROM python:3.9
ADD main.py .

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt