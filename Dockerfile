FROM python:3.6-slim
COPY . /python-test-calculator
WORKDIR /python-test-calculator
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-v", "--junitxml=reports/result.xml"]
#CMD tail -f /dev/null
RUN apt-get update && apt-get install -y python3-pytest
