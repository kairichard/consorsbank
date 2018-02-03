FROM joyzoursky/python-chromedriver

RUN pip install selenium
ADD main.py main.py

CMD python main.py
