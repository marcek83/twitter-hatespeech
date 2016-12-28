import json
import pdb

def get_data():
    tweets = []
    files = ['racism.json', 'neither.json', 'sexism.json']
    for file in files:
        with open('./tweet_data/' + file, 'r') as f:
            data = f.readlines()
        for line in data:
            tweet_full = json.loads(line)
            tweets.append({
                'id': tweet_full['id'],
                'text': tweet_full['text'],
                'label': tweet_full['Annotation']
                })

    #pdb.set_trace()
    return tweets


if __name__=="__main__":
    get_data()
