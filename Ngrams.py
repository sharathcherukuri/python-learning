def count_ngrams(sequence, N):
    freq = {}
    length = len(sequence)

    for i in range(0, length-N+1):
        w = sequence[i:i+N]
        if w not in freq:
            freq[w] = 0
        freq[w] += 1
    return freq
