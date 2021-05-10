import sys
import time
import insomniac
from random import randint

# Sleeping for random seconds
random_no = randint(0,3600)
print(f"Selecting a random number between 0 and 3600... Selected {random_no}.")
print(f"Sleeping for {random_no} seconds...")
time.sleep(random_no)

print("Starting insomniac script...")
activation_code = ""
insomniac.run(activation_code)
