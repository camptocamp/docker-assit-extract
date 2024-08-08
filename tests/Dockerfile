FROM python:3.8

WORKDIR /testing

RUN pip install selenium
COPY ./extract_test.py /testing/

ENTRYPOINT [ "python3", "/testing/extract_test.py" ]
