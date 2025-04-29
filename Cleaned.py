import pandas as pd

df = pd.read_csv("screen_time_app_usage_dataset.csv")

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

df = df.drop_duplicates()

df = df.drop(columns=[col for col in df.columns if "extra_col" in col])

df['category'] = df['category'].astype(str).str.strip().str.lower()

df['date'] = pd.to_datetime(df['date'], errors='coerce')

df['screen_time_min'] = pd.to_numeric(df['screen_time_min'], errors='coerce')
df['launches'] = pd.to_numeric(df['launches'], errors='coerce')
df['interactions'] = pd.to_numeric(df['interactions'], errors='coerce')
df['youtube_views'] = pd.to_numeric(df['youtube_views'], errors='coerce')
df['youtube_likes'] = pd.to_numeric(df['youtube_likes'], errors='coerce')
df['youtube_comments'] = pd.to_numeric(df['youtube_comments'], errors='coerce')

df = df.dropna(subset=['user_id', 'app_name', 'date'])

df.to_csv("screen_time_cleaned.csv", index=False)

print("CLEANED ✅")
