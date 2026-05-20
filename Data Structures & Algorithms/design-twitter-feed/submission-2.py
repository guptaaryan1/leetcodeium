class Twitter:

    def __init__(self):
        #userid -> followers, following, [tweet, ts]
        # tweets -  userid -> [[tweet, ts]]
        self.time = 0
        self.users = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [[], [], []]
        self.users[userId][2].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        idsfortweets = [userId]
        for someid in self.users[userId][1]:
            idsfortweets.append(someid)
        tweets = []
        for someid in idsfortweets:
            for tweet in self.users[someid][2]:
                tweets.append(tweet)

        feed = heapq.nlargest(10, tweets)
        return [tweetid for ts, tweetid in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = [[], [], []]
        if followeeId not in self.users:
            self.users[followeeId] = [[], [], []]

        if followerId not in self.users[followeeId][0]:
            self.users[followeeId][0].append(followerId)

        if followeeId not in self.users[followerId][1]:
            self.users[followerId][1].append(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[], [], []]
        if followeeId not in self.users:
            self.users[followeeId] = [[], [], []]

        if followerId in self.users[followeeId][0]:
            self.users[followeeId][0].remove(followerId)

        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
