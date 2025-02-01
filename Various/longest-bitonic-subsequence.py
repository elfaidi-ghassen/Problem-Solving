# problmem: https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688
# tags: dynamic programming, DP, LIS
from typing import List

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    inc_subseq = [1] * len(arr)
    dec_subseq = [1] * len(arr)
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and inc_subseq[j] + 1 > inc_subseq[i]:
                inc_subseq[i] = inc_subseq[j] + 1

    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i] and dec_subseq[j] + 1 > dec_subseq[i]:
                dec_subseq[i] = dec_subseq[j] + 1

    max_length = 0
    for i in range(len(arr)):
        max_length = max(max_length, inc_subseq[i] + dec_subseq[i] - 1)

    return max_length