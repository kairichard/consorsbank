FROM joyzoursky/python-chromedriver

RUN pip install selenium==3.8.0
ADD main.py main.py

ENTRYPOINT ["python", "main.py"]
CMD [ "total" ]