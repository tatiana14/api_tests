FROM python:3.7.0
WORKDIR /api_test
COPY ./proj/requirements.txt ./proj/requirements.txt
RUN pip install -r ./proj/requirements.txt
COPY ./tests ./tests
COPY ./helper ./helper
WORKDIR /api_test/tests
CMD ["pytest","--html=report/report.html"]