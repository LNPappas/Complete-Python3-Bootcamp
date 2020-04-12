import json
import re

def get_pieces():
    with open('baseball_data.json') as f:
        data = json.load(f)
        return data

def base_hits(data):
    hits = {}
    m = 0
    player = []
    for x in data:
        if x['hit_type'] != None:
            if x["event_result"] == 'double' or x["event_result"] == 'triple' or x["event_result"] == 'home_run':
                s = x['hitter_first_name'] + ' ' +x['hitter_last_name']
                if s in hits:
                    hits[s] +=1
                else:
                    hits.update({s:1})

    for i,v in hits.items():
        if v > m:
            m = v
            player = [i]
        elif v == m:
            player.append(i)
    return m, player

def hardest_pitch(data):
    for x in data:
        if (x["pitch_release_velocity"]) != None:
            if x['pitch_call'] != 'ball_called':
                if x['pitch_call'] != 'foul_ball':
                    if float(x["pitch_release_velocity"]) > 100:
                        return [x["pitcher_first_name"], x["pitcher_last_name"],x['pitch_call'], x["pitch_release_velocity"]]
                
def fastball(data):
    count = 0
    total = 0
    for x in data:
        if x["pitcher_team"] == 'COL':
            if x["pitch_type"] == 'four_seam':
                if x["pitch_release_velocity"] != None:
                    count +=1
                    total += float(x["pitch_release_velocity"])
    return round(total/count,4)

# Calculate the batting average of each player on the Giants and the Rockies. Create two
# lists of batting averages sorted descending for each team. For your answer, please
# provide two lists - first the list of the Giants’ batting averages, followed by the Rockies’
# batting averages. (Please round to 3 decimal places and leave off the leading 0. For
# example, .123 is the correct format. If any player batted 1.000, format the decimal to
# show the one’s digit )
def batting_ave(data, team):
    '''
    determined by dividing a player's 
    hits by his total at-bats for a number between zero 
    (shown as .000) and one (1.000)
    {None: 1, 'single': 1, 'sacrifice': 1, 'home_run': 1, 'out': 1, 'double': 1, 'error': 1, 'fielders_choice': 1, 'triple': 1}
    '''
    d = {}
    players = []
    for x in data:
        if x["hitter_team"] == team:
            s = x['hitter_first_name'] + ' ' + x['hitter_last_name']
            if s in d:
                temp = d[s]
                if x["event_result"] == 'single' or x["event_result"] == 'double' or x["event_result"] == 'triple' or x["event_result"] == 'home_run':
                    temp[0] += 1
                    temp[1] += 1
                else:
                    temp[0] += 1
                d[s] = temp
            else:
                if x["event_result"] == 'single' or x["event_result"] == 'double' or x["event_result"] == 'triple' or x["event_result"] == 'home_run':
                    d.update({s:[1,1]})
                else:
                    d.update({s:[1,0]})
    ba = []
    for k,v in d.items():
        temp = str(round(v[1]/v[0], 3))[1:]
        
        ba.append(temp)
    ba.sort(reverse = True) 
    return ba

def combined_ba(s, c):
    sf = [float(x) for x in s]
    co = [float(x) for x in c]
    l = []
    while len(sf) > 0 and len(co) > 0:
        if sf[0] > co[0]:
            l.append(sf[0])
            sf.pop(0)
        else:
            l.append(co[0])
            co.pop(0)
    if not sf:
        l += co
    else:
        l += sf
    l = [str(x)[1:] for x in l]
    return l

def v_check(data):
    '''
    Implement a function that takes in the baseball json data and checks if there were any
    two pitches thrown at the exact same velocity during the four-game series. Your function
    should return the velocity of the pitches that were thrown at identical speed - if there is
    more than one duplicate pair of velocities, return the first duplicate found. If no two such
    velocities exist, return None. Keep in mind that the run-time of your algorithm matters
    and do your best to optimize the time-complexity. (Please round to 4 decimal places).
    '''
    d = {}
    for x in data:
        if x["pitch_release_velocity"] not in d:
            d.update({x["pitch_release_velocity"]:1})
        else:
            return round(float(x["pitch_release_velocity"]),4)
    return None

def ops(data):
    '''
    What was the Giants OPS with runners in scoring position? (Please round to 3 decimal
    places and leave off the leading 0. For example, .123 is the correct format)
    '''
    d = {}
    players = []
    for x in data:
        if x["hitter_team"] == 'SF':
            s = x['hitter_first_name'] + ' ' + x['hitter_last_name']
            if s in d:
                temp = d[s]
                if x["event_result"] == 'single':
                    temp[0] += 1
                    temp[1] += 1
                elif x["event_result"] == 'double':
                    temp[0] += 1
                    temp[1] += 2
                elif x["event_result"] == 'triple':
                    temp[0] += 1
                    temp[1] += 3
                elif x["event_result"] == 'home_run':
                    temp[0] += 1
                    temp[1] += 3
                else:
                    temp[0] += 1
                d[s] = temp
            else:
                if x["event_result"] == 'single' or x["event_result"] == 'double' or x["event_result"] == 'triple' or x["event_result"] == 'home_run':
                    d.update({s:[1,1]})
                else:
                    d.update({s:[1,0]})
    ba = []
    for k,v in d.items():
        temp = str(round(v[1]/v[0], 3))[1:]
        
        ba.append(temp)
    ba.sort(reverse = True) 
    return ba

if __name__ == "__main__":
    data = get_pieces()
    num, name = base_hits(data)
    print(f'{name} : with {num} hits'.format(name, num))
    hp = hardest_pitch(data)
    print(hp)
    f = fastball(data)
    print(f)
    sf = batting_ave(data, 'SF')
    print(sf)
    co = batting_ave(data, 'COL')
    print(co)
    c = combined_ba(sf, co)
    print(c)
    vc = v_check(data)
    print(vc)
    o = ops(data)
    print(o)

        