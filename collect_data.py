# collect_data.py

import json
import re

import numpy as np
import pandas as pd
import requests
import soundfile as sf
from bs4 import BeautifulSoup
from kafka import KafkaConsumer
import paho.mqtt.client as mqtt
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. CSV file
def load_csv(path="data/my_data.csv"):
    df = pd.read_csv(path)
    print("CSV sample:")
    print(df.head())
    return df


# 2. SQL database (example: MySQL) - needs real DB to work
def load_sql(
    conn_str="mysql+pymysql://user:password@localhost:3306/mydb",
    query="SELECT * FROM my_table;",
):
    import sqlalchemy as sa
    engine = sa.create_engine(conn_str)
    df = pd.read_sql(query, engine)
    print("SQL sample:")
    print(df.head())
    return df


# 3. REST API (JSON) - needs real API URL
def load_rest_api(url="https://jsonplaceholder.typicode.com/posts"):
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    df = pd.json_normalize(data)
    print("REST API sample:")
    print(df.head())
    return df


# 4. Web scraping (static) - example.com used as demo
def scrape_static(url="https://example.com"):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    rows = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href")
        if href:
            rows.append({"text": text, "href": href})

    df = pd.DataFrame(rows)
    print("Static page links sample:")
    print(df.head())
    return df


# 5. Dynamic website (Selenium) - requires chromedriver + real site
def scrape_dynamic(url="https://example.com"):
    driver = webdriver.Chrome()
    driver.get(url)

    rows = []
    for a in driver.find_elements(By.TAG_NAME, "a"):
        rows.append({"text": a.text, "href": a.get_attribute("href")})

    driver.quit()
    df = pd.DataFrame(rows)
    print("Dynamic page links sample:")
    print(df.head())
    return df


# 6. Kafka streaming (prints messages) - requires running Kafka
def consume_kafka(topic="my_topic", servers=None):
    if servers is None:
        servers = ["localhost:9092"]

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=servers,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )

    for msg in consumer:
        print("Kafka message:", msg.value)


# 7. MQTT / IoT sensor data (prints messages) - requires broker
def start_mqtt(broker="broker.emqx.io", topic="my/iot/topic"):
    def on_message(client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        print("MQTT message:", payload)

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker, 1883, 60)
    client.subscribe(topic)
    client.loop_forever()


# 8. Text file
def read_text(path="data/notes.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("Text file sample:")
    for line in lines[:5]:
        print(line.strip())
    return lines


# 9. Audio file
def read_audio(path="data/audio.wav"):
    data, sample_rate = sf.read(path)
    print("Audio shape:", data.shape)
    print("Sample rate:", sample_rate)
    return data, sample_rate


# 10. Log file
def read_logs(path="logs/app.log"):
    rows = []
    pattern = re.compile(r"(?P<time>\S+) (?P<level>\S+) (?P<msg>.*)")
    with open(path) as f:
        for line in f:
            m = pattern.match(line)
            if m:
                rows.append(m.groupdict())
    df = pd.DataFrame(rows)
    print("Log sample:")
    print(df.head())
    return df


# 11. JSON file
def read_json(path="data/data.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    print("JSON sample:")
    print(df.head())
    return df


if __name__ == "__main__":
    # quick local test, uses files created by input.py
    load_csv()
    read_text()
    read_json()
    read_logs()
    read_audio()
