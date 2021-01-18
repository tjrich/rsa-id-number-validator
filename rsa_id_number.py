# TIMOTHY RICH
# +27745243897
# timothy.rich25@gmail.com

# Validating SA ID numbers

id_number = input('Please enter a South African ID number:')        # ask user to enter id number

id_number = str(id_number)                                  # converts id number to string

YYMMDD = id_number[0:6]
MM = id_number[2:4]
DD = id_number[4:6]
SSSS = id_number[6:10]
Z = id_number[10]
R = id_number[11]
K = id_number[12]

i = 0
A = 0
while i < 12:
    A = A + int(id_number[i])
    i += 2

i = 1
B = ""
while i < 12:
    B = B + id_number[i]
    i += 2

B2 = str((2 * int(B)))
i = 0
C = 0

while i < len(B2):
    C += int(B2[i])
    i += 1

D = A + C
Q = D % 10
W = (10 - (D%10))

if len(id_number) == 13:

    if (int(MM) < 13) and (int(DD) < 32):

        if int(Z) == 0 or int(Z) == 1:

            if int(R) == 8 or int(R) == 9:
                
                if (10 - Q) == int(K) or Q == 0: 
                    print('This is a valid SA ID number')
                else:
                    print('This is not a valid SA ID number')
            else:
                    print('This is not a valid SA ID number')
        else:
            print('This is not a valid SA ID number')            
    else:
        print('This is not a valid SA ID number')
else:
    print('This is not a valid SA ID number')
