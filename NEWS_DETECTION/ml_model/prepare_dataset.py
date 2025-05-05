import pandas as pd

# CSV files load karo
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

# label column add karo
fake_df['label'] = 0
true_df['label'] = 1

# Merge both
combined_df = pd.concat([fake_df, true_df], ignore_index=True)

# Save final file
combined_df.to_csv("dataset/fake_or_real_news.csv", index=False)

print("✅ Final file ready hai: dataset/fake_or_real_news.csv")
