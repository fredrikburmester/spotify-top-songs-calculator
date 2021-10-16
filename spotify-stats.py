import json
  
# Opening JSON file
f = open('./MyData/StreamingHistory0.json',)
f2 = open('./MyData/StreamingHistory1.json',)
  
data1 = json.load(f)
data2 = json.load(f2)

songs = {}
  
def addTimesPlayed(data):
    for i in data:
        item = songs.get(i['trackName'])
        if item != None:
            songs[i['trackName']] += i['msPlayed']
        else: 
            songs[i['trackName']] = i['msPlayed']

def addTimePlayed(data):
    for i in data:
        item = songs.get(i['trackName'])
        if item != None:
            songs[i['trackName']] += i['msPlayed']
        else: 
            songs[i['trackName']] = i['msPlayed']
  
# addTimesPlayed(data1)
addTimesPlayed(data2)

songs_sorted = {k: v for k, v in sorted(songs.items(), key=lambda item: item[1], reverse=True)}

first_three = list(songs_sorted)[:10]
for i,k in enumerate(first_three):
    print(f"{i}: {k}")