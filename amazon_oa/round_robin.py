def cpu(arr, ela, q):

    queue = []

    queue += (0, 0),
    total, added, cur = 0, 1, 0
    
    while queue:
        i, run = queue.pop()

        nextcpu = run + q
        if nextcpu >= ela[i]:
            cur += ela[i] - run
            total += cur - arr[i] - ela[i]
        else:
            cur += q

        while added < len(arr):
            if arr[added] <= cur:
                queue.insert(0, (added, 0))
                added += 1
            else:
                break

        if nextcpu < ela[i]:
            queue.insert(0, (i, run+q))
            
    return total * 1.0 / len(arr)



print cpu([0, 1, 4], [5, 2, 3], 3)

print cpu([0,1,3,9], [2,1,7,5], 2)

print cpu([0,2,4,5], [7,4,1,4], 3)









        


