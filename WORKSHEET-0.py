#TASK-1
#1,2,3
'''
time_data = [ 
(3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0), 
(4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5), 
(5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0), 
(3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0), 
(4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0) 
]
#1
low = []
moderate = []
high = []
#2
for study, entertainment, sleep in time_data:
    if study < 3:
        low.append(study)
    elif 3<=study<=5:
        moderate.append(study)
    else:
        high.append(study)
#3
print("Low study time:",low)
print("moderate study time:",moderate)
print("high study time:",high)
'''


#Task-3
'''
time_data = [
    (3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
    (4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
    (5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
    (3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
    (4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]

study_minutes = []
for study, entertainment, sleep in time_data:
    minutes = study * 60
    study_minutes.append(minutes)
print("Study hours in minutes:",study_minutes)
'''

#Task-4
'''
time_data = [
    (3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
    (4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
    (5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
    (3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
    (4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]
#Create empty lists
study_hours = []
entertainment_hours = []
sleep_hours = []

#Extract values
for study, entertainment, sleep in time_data:
    study_hours.append(study)
    entertainment_hours.append(entertainment)
    sleep_hours.append(sleep)

#Calculate averages
avg_study=sum(study_hours)/len(study_hours)
avg_entertainment=sum(entertainment_hours)/len(entertainment_hours)
avg_sleep=sum(sleep_hours)/len(sleep_hours)

#Print averages
print("Average study hours:",avg_study)
print("Average entertainment hours:",avg_entertainment)
print("Average sleep hours:",avg_sleep)
'''


#Task-5
'''
import matplotlib.pyplot as plt
time_data = [
    (3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
    (4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
    (5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
    (3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
    (4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]

#Extraction of study and sleep 
study=[x[0] for x in time_data]
sleep=[x[2] for x in time_data]

#Scatter plot
plt.scatter(study,sleep)
plt.xlabel("Study Hours")
plt.ylabel("Sleep Hours")
plt.title("Study vs Sleep Pattern")
plt.show()
'''


#Recursion exercise
#Task-1
'''
def sum_nested_list(nested_list):
    total=0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total
nested_list = [1,[2,[3,4],5],6,[7,8]]
result = sum_nested_list(nested_list)
print("Nested List:",nested_list)
print("Total Sum:", result)
'''

#Task-2
'''
def generate_permutations(s):
    if len(s) <=1:
        return [s]
    permutations = []
    for i in range(len(s)):
        current_char = s[i]
        remaining = s[:i]+ s[i+1:] #Remove the chosen characters
        # Recursively generate permutations of the remaining string
        for perm in generate_permutations(remaining):
            permutations.append(current_char+perm)
        return list(set(permutations))
print("Permutations of 'abc':")
print(generate_permutations("abc"))
print("\nPermutations of 'aab':")
print(generate_permutations("aab"))
'''
#Task-3
'''
def calculate_directory_size(directory):
    total_size=0
    for item in directory.values():
        if isinstance(item, dict): #If it's a subdirectory
            total_size +=calculate_directory_size(item)
        else: #If it's a file, add its size
            total_size += item
    return total_size
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}
total_size = calculate_directory_size(directory_structure)
print(f"Total Directory Size: {total_size} KB")
'''

#DYNAMIC PROGRAMMING
#Task-1
'''
def min_coins(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i],dp[i - coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1
coins = [1,2,5]
amount = 11
result = min_coins(coins, amount)
print(f"Minimum coins required to make {amount} with coins {coins}: {result}")
'''

#Task-2
'''
def longest_common_subsequence(s1, s2):
    dp = [[0]*(len(s2)+1) for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+1 #Match: extend LCS
            else:
                dp[i+1][j+1]= max(dp[i][j+1], dp[i+1][j]) #No match: take max
    return dp[len(s1)][len(s2)]
s1 = "abcde"
s2 = "ace"
print(f"The length of the LCS of '{s1}' and '{s2}' is:", longest_common_subsequence(s1,s2))
'''

#Task-3
def knapsack(weight, values, capacity):
    n = len(weights)
    dp = [0]*(capacity+1)
    for i in range(n):
        for w in range(capacity, weights[i]-1,-1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(weights, values, capacity)
print(f"Maximum value that can be carried: {result}")
    
