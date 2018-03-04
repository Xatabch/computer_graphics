sequence = [1, 2, 7, 19]

# Сравните:
idx = 0
for item in sequence:
    print(idx)
    idx += 1

print('\n')
# и
for idx, item in enumerate(sequence):
    if idx == 2:
        print(idx)