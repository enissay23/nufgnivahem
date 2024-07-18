from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', key_serializer=str.encode, value_serializer=int.encode)

key_list = ["product1", "product2", "product3"]
value_list = [15, 20, 33, 1, 50, ]

for _ in range(10):
    producer.send('orders', random.choice(key_list), random.randrange(10))
    producer.flush()    

print(producer.metrics())

producer.close()