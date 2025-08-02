# Accept user input to create two sets of integers and find their intersection
set1 = set(map(int, input("Enter integers for set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for set 2 (space-separated): ").split()))
common_elements = set1 & set2
print(f"Common elements: {common_elements}")
