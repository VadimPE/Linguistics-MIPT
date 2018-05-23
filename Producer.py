import pymongo
from nltk.stem import PorterStemmer

class Producer:
    
    def __init__(self, host, port):
        client = pymongo.MongoClient(host, port)
        db = client["lingvabd4"]
        self.posts = db.posts
    
    def GetInfo(self, word):
        for res in self.posts.find({"name": word}):
            return res["info"]

    def GetCount(self, word):
        for res in self.posts.find({"name": word}):
            return res["info"]["count"]
    
    def GetRole(self, word):
        for res in self.posts.find({"name": word}):
            return res["info"]["role"]

    def GetStatistic(self):
        tmp = {}
        for post in self.posts.find():
            tmp[post["name"]] = post["info"]["count"]
        array = sorted(tmp, key=tmp.get, reverse=True)
        ans = []
        for word in array:
            ans.append((word, tmp[word]))
        return ans
    
    def GetNormalForm(self, word):
        ps = PorterStemmer()
        return ps.stem(word)
