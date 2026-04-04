from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'alerts',
    bootstrap_servers='broker:9092',
    auto_offset_reset='earliest',
    group_id='alerts-reader',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    tx = message.value
    print(f"ALERT | {tx['tx_id']} | {tx['amount']:.2f} PLN | score={tx['score']} | {tx['rules']}")
