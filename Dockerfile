FROM python:2-alpine AS Step 
ENV PYTHONBUFFERED 1
COPY . . 
ENTRYPOINT ["python","calculator.py"]
