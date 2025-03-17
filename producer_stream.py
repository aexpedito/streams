import pandas as pd



def main():
	print("Starting producer")
	data = pd.read_csv("creditCardData/card_transdata.csv")
	print(data.info())

if __name__ == '__main__':
	main()