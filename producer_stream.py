from sys import api_version

from kafka import KafkaProducer
import pandas as pd


def main():
	print("Starting producer")
	data = pd.read_csv("creditCardData/card_transdata.csv")
	print(data.info())
	producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version)

	producer.send('test_topic',b'Hi!')

	producer.flush()

	print("Finished")

if __name__ == '__main__':
	main()