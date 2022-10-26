FROM python:3.10.5
COPY . .

RUN pip install ./meds-csv-fix
RUN python -m meds-csv-fix /path
