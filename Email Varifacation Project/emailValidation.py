
# Email Validation program

emailInput = input("Enter Your Email : ")
k,j,d= 0,0,0
if len(emailInput) >= 6 :

  if emailInput[0].isalpha():

    if ("@" in emailInput) and (emailInput.count("@")==1):

      if (emailInput[-4]==".") ^ (emailInput[-3]=="."):
        for i in emailInput:
          if i == i.isspace():
            k = 1

          elif i.isalpha():
            if i==i.upper():
              j = 1

          elif i.isdigit():
            continue

          elif i=="_" or i=="." or i=="@":
            continue
          
          else:
            d=1

        if k==1 or j==1 or d==1 :
             print(f'Space " " , UpperCase and special characters are not allowed in email : {emailInput}')
        else:
          print(f'Your Email is valid : {emailInput}')
      else:
        print(f'Add at least two or three letter after "." in Email :{emailInput}')
    else:
      print(f"@ is missing or wrote @ more than 1 in Email :{emailInput}")

  else:
    print("Email's first letter should be alphabet ")

else:
  print("Email's letters should be greater than 5 ")


