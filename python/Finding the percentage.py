def marks(student_marks,query_name):
        for k,v in student_marks.items():
            if k == query_name:
                res =  sum(v)/len(v)
                return f'{res:.2f}'


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(marks(student_marks, query_name))
 
    