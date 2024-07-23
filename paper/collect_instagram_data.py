# filename: collect_instagram_data.py
import instaloader
import sqlite3
import datetime

# Initialize instaloader
L = instaloader.Instaloader()

# Login to Instagram
#L.login('your_username', 'your_password')  # Replace with your actual username and password
L.load-coockies

# List of Instagram accounts to analyze
accounts = ['kinnstudio', 'levnaro', 'artemer', 'frankdarling', 'heniadanielle', 'nocojewelry']

# Connect to SQLite database
conn = sqlite3.connect('instagram_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                  (account TEXT, post_id TEXT, post_type TEXT, likes INTEGER, comments INTEGER, shares INTEGER, hashtags TEXT, timestamp TEXT)''')

for account in accounts:
    profile = instaloader.Profile.from_username(L.context, account)
    for post in profile.get_posts():
        if post.date_utc > datetime.datetime.now() - datetime.timedelta(days=60):
            post_type = 'image' if post.typename == 'GraphImage' else 'video' if post.typename == 'GraphVideo' else 'carousel'
            hashtags = ' '.join(post.caption_hashtags)
            cursor.execute('''INSERT INTO posts (account, post_id, post_type, likes, comments, shares, hashtags, timestamp)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                           (account, post.shortcode, post_type, post.likes, post.comments, 0, hashtags, post.date_utc))
conn.commit()
conn.close()
print("Data collection complete.")