from flask import Flask, request, jsonify
from datetime import datetime
from collections import defaultdict
 
app = Flask(__name__)
 
# In-memory storage (for simplicity)
users = {}  # user_id: username
tweets = defaultdict(list)  # user_id: list of tweets
follows = defaultdict(set)  # user_id: set of followees
timelines = defaultdict(list)  # user_id: list of recent tweets in timeline
 
# API to post a tweet
@app.route('/postTweet', methods=['POST'])
def post_tweet():
    user_id = request.json['user_id']
    content = request.json['content']
    tweet_id = len(tweets[user_id]) + 1
    timestamp = datetime.now()
    tweet = {'tweet_id': tweet_id, 'content': content, 'timestamp': timestamp}
 
    # Store tweet for the user
    tweets[user_id].append(tweet)
 
    # Fan-out to followers
    for follower in follows[user_id]:
        timelines[follower].append(tweet)
 
    return jsonify({"message": "Tweet posted successfully!"})
 
# API to view timeline
@app.route('/timeline', methods=['GET'])
def view_timeline():
    user_id = request.args.get('user_id')
    return jsonify({"timeline": timelines[user_id]})
 
# API to follow a user
@app.route('/follow', methods=['POST'])
def follow_user():
    user_id = request.json['user_id']
    followee_id = request.json['followee_id']
    follows[user_id].add(followee_id)
    return jsonify({"message": f"You are now following user {followee_id}!"})
 
# API to unfollow a user
@app.route('/unfollow', methods=['POST'])
def unfollow_user():
    user_id = request.json['user_id']
    followee_id = request.json['followee_id']
    if followee_id in follows[user_id]:
        follows[user_id].remove(followee_id)
        return jsonify({"message": f"You have unfollowed user {followee_id}."})
    return jsonify({"message": f"You are not following user {followee_id}."})
 
if __name__ == "__main__":
    app.run(debug=True)
