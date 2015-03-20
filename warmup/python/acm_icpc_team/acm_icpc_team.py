def max_topic_number(lst, M):
    """Expect list"""
    topics_k = [0 for i in range(M)]
    for item in lst:
        print(topics_k)
        topics_k = [p | k for p, k in zip(topics_k, item)]
    print(topics_k)
    return topics_k.count(1)

def max_topic_number2(lst, M):
    """Expect a list of people and an integer of the maximum number of topics known"""
    max_topics = 0
    skip = []
    possible_match = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j not in skip and i != j:
                temp = [p | k for p, k in zip(lst[i], lst[j])]
                if temp.count(1) > max_topics:
                    max_topics = temp.count(1)
                    skip.append(j)
                    skip.append(i)
                elif temp.count(1) == max_topics:
                    possible_match.append([i, j, max_topics])
    return {'max':max_topics, 'match': possible_match}

def know_all_teams2(lst, max_topics, M):
    """Expect a list of people and an integer of the maximum number of topics known"""
    teams = 0
    for i in M:
        if i[2] == max_topics:
            teams += 1 
    return teams

def know_all_teams(lst, max_topics, M):
    """Expect a list of people and an integer of the maximum number of topics known"""
    teams = 0
    skip = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j not in skip and i != j:
                temp = [p | k for p, k in zip(lst[i], lst[j])]
                if temp.count(1) == max_topics:
                    teams += 1 
                    skip.append(j)
                    skip.append(i)
    return teams

if __name__ == "__main__":
    topics = teams = 0
    a = input().split(" ")
    N, M = [int(x) for x in input().split(' ')]
    people = []
    for i in range(N):
        people.append([int(i) for i in list(input())])
    topics = max_topic_number2(people, M)
    teams = know_all_teams2(people, topics['max'], topics['match'])
    print("%d\n%d" % (topics['max'], teams))

