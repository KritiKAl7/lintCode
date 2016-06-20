'''
http://www.lintcode.com/en/problem/mini-twitter/
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
import time
from collections import defaultdict
from collections import deque
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.users = defaultdict(list)
        self.tweets = {}


    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        tweet = Tweet.create(user_id, tweet_text)
        self.tweets[time.time()] = tweet
        return tweet


    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        userList = self.users[user_id]
        userList.append(user_id)
        keyList = sorted(self.tweets.keys())[::-1]
        tweetList = []
        for i in keyList:
            if len(tweetList) < 10:
                if self.tweets[i].user_id in userList:
                    tweetList.append(self.tweets[i])
            else:
                break
        return tweetList
            
        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        keyList = sorted(self.tweets.keys())[::-1]
        tweetList = []
        for i in keyList:
            if len(tweetList) < 10:
                if self.tweets[i].user_id == user_id:
                    tweetList.append(self.tweets[i])
            else:
                break
        return tweetList
                
            
    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if to_user_id not in self.users[from_user_id]:
            self.users[from_user_id].append(to_user_id)


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if to_user_id in self.users[from_user_id]:
            self.users[from_user_id].remove(to_user_id)