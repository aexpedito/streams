from kafka import KafkaProducer
import pandas as pd
import json as json
from time import sleep

#Setup kafka producer
def serializer(message):
	return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
	bootstrap_servers=['localhost:9094'],
	value_serializer=serializer
)

# send message to topic
def send_message(topic, message):
	producer.send(topic, message)
	producer.flush()


def main():
	print("Starting producer")
	data = pd.read_csv("creditCardData/card_transdata.csv")
	iter = data.iterrows()
	for index, row in data.iterrows():
		# send payload do consumers
		payload = {
			"distance_from_home": row["distance_from_home"],
			"distance_from_last_transaction": row["distance_from_last_transaction"],
			"ratio_to_median_purchase_price": row["ratio_to_median_purchase_price"],
			"repeat_retailer": row["repeat_retailer"],
			"used_chip": row["used_chip"],
			"used_pin_number": row["used_pin_number"],
			"online_order": row["online_order"],
			"fraud": row["fraud"],
		}
		send_message('test_topic', payload)
		sleep(5)

	print("Finished producer")

if __name__ == '__main__':
	main()