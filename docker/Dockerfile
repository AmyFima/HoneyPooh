FROM python:3

EXPOSE 8080

RUN pip install datetime
RUN pip install elasticsearch
RUN pip install flask
RUN pip install requests

ADD config /
ADD bruteForce_dos_sessionPrediction_detection.py /
ADD elasticsearch_functions.py /
ADD get_config_data.py /
ADD get_location_by_ip.py /
ADD remote_code_execution_detection.py /
ADD proxy.py / 

CMD [ "python", "./proxy.py" ]
