if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    scores_sorted = sorted(scores,key=lambda x: x[1])
    mi = scores_sorted[0][1]
    #copy = scores_sorted[:]   # copy for the iterator
    scores_sorted2 = [scores_sorted[i] for i in range(len(scores_sorted))  if scores_sorted[i][1] != mi]         
    mi = scores_sorted2[0][1]
    names = [scores_sorted2[i][0] for i in range(len(scores_sorted2)) if scores_sorted2[i][1] == mi]
    for i in names:
        print(i)
   
