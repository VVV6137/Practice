def inverse(p):
    n = len(p)
    inv = [0] * n
    for i in range(n):
        inv[p[i] - 1] = i + 1
    return inv

def decrypt(word_1, p, k):
    n = len(word_1)
    inv = inverse(p)
    curr_word = word_1
    for _ in range(k):
        curr_word = ''.join(curr_word[inv[i] - 1] for i in range(n))
    return curr_word

l = input().split()
n = int(l[0])
k = int(l[1])
l1 = input().split()
p = list(map(int,l1))
word_1 = input().strip()
word_0 = decrypt(word_1, p, k)
print(word_0)

