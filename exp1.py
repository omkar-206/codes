
a = [None]

def MaxMin(i, j, max, min):
    if i == j:
        max = min = a[i]
        
    elif i == j - 1:
        if a[i] < a[j]:
            max = a[j]
            min = a[i]
        else:
            max = a[i]
            min = a[j]
            
    else:
        mid = (i + j) // 2
        
        max1, min1 = MaxMin(i, mid, max, min)
        max2, min2 = MaxMin(mid + 1, j, max, min)
        
        # Combine the solutions
        if max1 > max2:
            max = max1
        else:
            max = max2
            
        if min1 < min2:
            min = min1
        else:
            min = min2
            
    print(f"i = {i}  j = {j}  min = {min}  max = {max}")
    
    return max, min


if __name__ == "__main__":
    try:
        user_input = input("Enter array values separated by spaces: ")
        input_list = user_input.split()
        
        if len(input_list) == 0:
            print("Array is empty.")
        else:
            for item in input_list:
                a.append(int(item))
                
            print("\nTrace Output:")
            maximum, minimum = MaxMin(1, len(a) - 1, None, None)
            
            print(f"\nFinal Result: min = {minimum}   Max = {maximum}")
            
    except ValueError:
        print("Error: Invalid input! Please enter integers only.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")