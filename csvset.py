import numpy as np 
import pandas as pd
df = pd.read_csv('D:\\fraudTest.csv\\fraudTest.csv')
data_array = df.to_numpy()

# Identify fraudulent transactions
fraud_df = df[df['is_fraud'] == 1]
print("\nNumber of fraudulent transactions:", len(fraud_df))

# Get unique fraudulent card numbers
fraud_cards = fraud_df['cc_num'].unique()
print("\nFraudulent cards (cc_num):")
for card in fraud_cards:
    print(card)

# Get unique users associated with fraudulent cards
blacklisted_users = fraud_df[['cc_num', 'first', 'last']].drop_duplicates()
print("\nBlacklisted users (card blacklisted):")
for index, row in blacklisted_users.iterrows():
    print(f"Card: {row['cc_num']} - User: {row['first']} {row['last']} (Blacklisted)")
