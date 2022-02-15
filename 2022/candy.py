def cases(case_num):

    (total_bags, num_kids) = map(int, input().split())
    candy_counts = list(map(int, input().split()))
    # print(candy_counts)
    total_candy = 0
    for i in range(total_bags+1):
        total_candy += candy_counts[i]
    print("total candy ->", total_candy)
    candy_remaining = total_candy % num_kids
    # print("Candy remains ->", candy_remaining)
    print(f'Case #{case_num}: {candy_remaining}')

# Iterater through each case
num_cases = int(input())

for i in range(num_cases):
    cases(i+1)