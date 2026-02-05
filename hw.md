# Python Homework – Practice

Solve at least **one** question (recommended to try more) using **Python code**

## Question 1 – Sound system (match-case)

In a sound system there are volume levels from **1–10**

* 1 – very quiet
* 2 – quiet
* 3 – low
* 4 – low
* 5 – medium
* 6 – medium high
* 7 – loud
* 8 – very loud
* 9 and 10 – max volume

Tasks

* Input an integer from the user (1–10)
* Use `match case` to display the correct sound description
* If the number is not between 1–10 print `invalid volume`

## Question 2 – Countdown with time.sleep

Use the `time.sleep` function to create the following output

* Print 5
* Sleep 1 second
* Print 4
* Sleep 1 second
* Print 3
* Sleep 1 second
* Print 2
* Sleep 1 second
* Print 1
* Sleep 1 second
* Print `0 - Launch`

Rules

* Use `import time`
* Use `time.sleep(1)` between prints

## Question 3 – Restaurant recommendation (booleans)

Input from the user

* The time it took the restaurant to bring the meal (in minutes)
* The price of the meal (in shekels)

Create boolean variables

* `is_quick_service` – True if the time is **less than 15 minutes**, otherwise False
* `is_expensive` – True if the price is **more than 100 shekels**, otherwise False

Now check

* If `is_quick_service` and **not** `is_expensive` print `recommended`
* Otherwise print `not recommended`

## Question 4 – Post office delivery (f-string)

## Question 4 – Post Office Delivery (f-string)

For a post office delivery, input the following details from the user:

* last name
* first name
* country
* city address
* zipcode

### Fixes & Requirements

* The **last name** must be converted to **uppercase**
* The **first name** must be converted to **lowercase**
* The **country** string length must be **at most 3 letters** (for example: US, IL)
* Use a **while loop** to validate the country input
* The **zipcode** must contain **digits only**
* Use a **while loop** and `isalpha` to validate the zipcode input

---

### Example Solution

```python
last_name = input("Enter last name: ").upper()
first_name = input("Enter first name: ").lower()

country = input("Enter country (max 3 letters): ")
while not country.isalpha() or len(country) > 3:
    country = input("Country must contain letters only and be up to 3 characters. Enter again: ")

address = input("Enter city address: ")

zipcode = input("Enter zipcode: ")
while zipcode.isalpha():
    zipcode = input("Zipcode must contain digits only. Enter again: ")

print(f"FOR: {last_name}, {first_name}")
print(f"COUNTRY: {country}")
print(f"ADDRESS: {address}")
print(f"ZIPCODE: {zipcode}")
```

---

### Output Format

FOR: LASTNAME, firstname
COUNTRY: IL
ADDRESS: Tel Aviv
ZIPCODE: 12345


For a post office delivery, input the following details from the user:

last name

first name

country

city address

zipcode

Fixes & Requirements

The last name must be converted to uppercase

The first name must be converted to lowercase

The country string length must be at most 3 letters (for example: US, IL)

The zipcode must contain digits only

Use a while loop and isalpha to validate the zipcode input

For a post office delivery input the following details

* last name
* first name
* country
* city address
* zipcode

Now print the following using `print(f"...")`

FOR: {last-name}, {first-name}  
COUNTRY: {country}  
ADDRESS: {city address}  
ZIPCODE: {zipcode}  

## Question 5 – Password validation (string methods)

A valid password must include

* at least one uppercase letter
* at least one lowercase letter
* at least one digit

Tasks

* Input the password from the user
* Check if it is valid using these methods

  * `isupper`
  * `islower`
  * `isalpha`
  * `isdigit`

Notes

* If the password is valid print `valid password`
* Otherwise print `invalid password`


Submit email: **[pythonai211225+python9str@gmail.com](mailto:pythonai211225+python9str@gmail.com)**
