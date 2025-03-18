from kafka import KafkaConsumer
import json as json

consumer = KafkaConsumer(
	'test_topic',
	bootstrap_servers='localhost:9094',
	group_id='group1',
	max_poll_records= 1,
	#value_deserializer=lambda m: json.loads(m.decode('utf-8')),
	auto_offset_reset='latest'
)

def main():
	print("Starting consumer...")
	for message in consumer:
		print(json.loads(message.value))

if __name__ == '__main__':
	main()