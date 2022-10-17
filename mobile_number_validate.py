import re
check = re.fullmatch('\d{3}([-]*)\d{6}',"080-265955")
if check:
   print("Valid")
else:
   print("Invalid")