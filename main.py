import pandas as pd
from segments import segment_customers
from messaging import send_campaign

def main():
    df = pd.read_csv("data/users.csv") 
    df, _ = segment_customers(df)
    send_campaign(df)

if __name__ == "__main__":
    main()
