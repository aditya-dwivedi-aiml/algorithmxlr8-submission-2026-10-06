def main():
    coordinates = input().strip()
    if coordinates[0] in ['a','b','c','d','e','f','g','h'] and coordinates[1] in ['1','2','3','4','5','6','7','8']:
            
        if coordinates [0] in ['a','c','e','g']:
            if  int(coordinates[1])%2==1:
                print("Black")
            else:
                print("White")
        else :
          if  int(coordinates[1])%2==0:
            print("Black")
          else:
            print("White")
            




if __name__ == "__main__":
    main()
