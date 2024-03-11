FROM python
COPY *.py ./
COPY image/* ./image/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py"]