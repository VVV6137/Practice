def inverse(permutation):
    n = len(permutation)
    inv = [0] * n
    for i in range(n):
        inv[permutation[i] - 1] = i + 1
    return inv

def decrypt(encrypted_word, permutation, k):
    n = len(encrypted_word)
    inv = inverse(permutation)
    current_word = encrypted_word
    for _ in range(k):
        current_word = ''.join(current_word[inv[i] - 1] for i in range(n))
    return current_word

n, k = map(int, input().split())
permutation = list(map(int, input().split()))
encrypted_word = input().strip()
original_word = decrypt(encrypted_word, permutation, k)
print(original_word)
