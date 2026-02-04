

age = 20

if age > 18:
    print('Beer')
else:
    print('Coke Zero')

print(age > 18)

# ===================== lazy behavior
age = 20
is_adult: bool = age > 18  # lazy  Not computed yet
age = 16
print(is_adult)  # lazy -- False computed now
age = 20
print(is_adult)  # lazy -- True computed now

# ===================== eager behavior
age = 20
is_adult: bool = age > 18  # eager  True - computed instantly , never again
age = 16
print(is_adult)  # eager -- True

# lazy
# for _ in range(age):
#   pass

if is_adult == True:
    print('Beer')
else:
    print('Coke')

if is_adult:
    print('Beer')
else:
    print('Coke')

if is_adult == False:
    print('Coke')
else:
    print('Beer')

if not is_adult:
    print('Coke')
else:
    print('Beer')

# input rating from the user, the range should be 1-5
#   is_valid should be True if in range and False if not in range
#   if is_valid:
#      print('in range')
#   else:
#      print('not in range')
#
# is_best should be True if the rating was 5
#   if is_valid and is_best:
#      print('highest score')
#   else:
#      print('not highest score')
#
# is_medium should be True if the rating was between 2-4
#   if is_valid and not is_medium:
#      print('score high or low')
#   else:
#      print('medium score')
#
# input number from user
#   is_positive should be True if number > 0
#   write if with print
#
# input number from user
#   is_even should be True if number % 2 == 0
#   write if with print
#
# **Bonus: input number from user, is_prime should be True if the number is prime otherwise False