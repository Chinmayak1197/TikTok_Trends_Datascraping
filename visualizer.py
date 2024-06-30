# Correcting the cleaning process and handling edge cases
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the provided CSV file
file_path = '/mnt/data/TikTok via Magical - Sheet1.csv'
df = pd.read_csv(file_path)

# Extract relevant columns
df_relevant = df[['Comment Count', 'URL', 'hashtags', 'Likes', 'Views']]

# Clean and format data
# Remove "Comments (" prefix and ")" suffix from Comment Count and convert to integer
df_relevant['Comment Count'] = df_relevant['Comment Count'].str.extract(r'(\d+)').astype(int)

# Function to convert likes and views to numerical format
def convert_to_number(x):
    if 'K' in x:
        return float(x.replace('K', '')) * 1e3
    elif 'k' in x:
        return float(x.replace('k', '')) * 1e3
    elif 'M' in x:
        return float(x.replace('M', '')) * 1e6
    else:
        return float(x)

df_relevant['Likes'] = df_relevant['Likes'].apply(convert_to_number).astype(int)
df_relevant['Views'] = df_relevant['Views'].apply(convert_to_number).astype(int)

# Calculate engagement rate
df_relevant['Engagement Rate (%)'] = (df_relevant['Likes'] + df_relevant['Comment Count']) / df_relevant['Views'] * 100

# Display cleaned data
cleaned_data = df_relevant.head()

# Extract hashtags
all_hashtags = df_relevant['hashtags'].dropna().str.split().explode()

# Count the frequency of each hashtag
hashtag_counts = all_hashtags.value_counts()

# Plot engagement rate
plt.figure(figsize=(10, 6))
sns.histplot(df_relevant['Engagement Rate (%)'], bins=20, kde=True)
plt.title('Distribution of Engagement Rates')
plt.xlabel('Engagement Rate (%)')
plt.ylabel('Frequency')
plt.show()

# Plot the most common hashtags
plt.figure(figsize=(10, 6))
sns.barplot(x=hashtag_counts.head(10).values, y=hashtag_counts.head(10).index)
plt.title('Top 10 Hashtags')
plt.xlabel('Frequency')
plt.ylabel('Hashtags')
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Cleaned TikTok Data", dataframe=cleaned_data)

cleaned_data, hashtag_counts.head(10)
