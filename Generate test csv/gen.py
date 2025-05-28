import pandas as pd

# Read the original dataset
input_path = r"C:\Users\sinha\OneDrive\Documents\Projects\Bihari Hackathon 2\BiharChalo\bank-fraud-detection\data\processed\final_dataset.csv"
df = pd.read_csv(input_path)

# Sample 100 to 150 transactions (randomly)
sampled_df = df.sample(n=150, random_state=42)  # Change n as needed (100-150)

# Save the sampled data to the target folder
output_path = r"C:\Users\sinha\OneDrive\Documents\Projects\Bihari Hackathon 2\BiharChalo\Generate test csv\sampled_transactions.csv"
sampled_df.to_csv(output_path, index=False)

print(f"Sampled data saved to {output_path}")


