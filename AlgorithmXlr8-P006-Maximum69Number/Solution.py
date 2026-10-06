def main():
    num = input().strip()
    # Write your solution here.
    # Print the maximum number after changing at most one digit 6 to 9.
    # print(num.replace('6', '9', 1)) 
    val_list=list(num)
    for i ,val in enumerate(val_list):
        if val=='6':
            val_list[i]='9'
            break
    print(''.join(val_list))




if __name__ == "__main__":
    main()
