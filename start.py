import sys
import time
import insomniac
from random import randint

# Sleeping for random minutes
random_no = randint(0,59)
print(f"Selecting a random number between 0 and 59... Selected {random_no}.")
print(f"Sleeping for {random_no} minutes...")
# time.sleep(random_no)

print("Starting insomniac script...")
activation_code = ""
insomniac.run(activation_code)
