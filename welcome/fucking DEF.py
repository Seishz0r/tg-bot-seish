def minimal(l):
    minn = l[0]
    for el in l:
        if el < minn:
            minn = el

    return minn


nums1 = [5, 4, 7, 1]
ans1 = minimal(nums1)

nums2 = [5.6, 3.4, 7, 1.9]
ans2 = minimal(nums2)

if ans1 < ans2:
    print(ans1)
else:
    print(ans2)
