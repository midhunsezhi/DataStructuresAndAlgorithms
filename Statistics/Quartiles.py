def get_median(arr):
    if len(arr)%2 == 0:
        q2 = (arr[len(arr)//2] + arr[len(arr)//2 -1])/2
    else:
        q2 = arr[len(arr)//2]

    return q2

def get_quartiles(data):
    q2 = get_median(data)

    if len(data) % 2 == 0:
        half1 = data[:len(data)//2]
        half2 = data[len(data)//2:]

    else:
        half1 = data[:len(data)//2]
        half2 = data[len(data)//2 + 1:]

    q1 = get_median(half1)
    q3 = get_median(half2)
    
    return (q1, q2, q3)