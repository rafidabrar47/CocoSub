# tc_3_random.py
# A test case for generating and validating a random user profile.

import random
import string

def generate_random_user():
    """
    Creates a dictionary representing a user with randomized attributes.
    """
    user_id = random.randint(1000, 9999)
    
    # Generate a random name like 'UserAbcd'
    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    username = f"user_{random_suffix}_{user_id}"
    
    # Randomly assign a status and a role
    possible_statuses = ['active', 'pending', 'inactive', 'suspended']
    status = random.choice(possible_statuses)
    
    permissions_level = random.randint(1, 5) # 1=guest, 5=admin
    
    user_profile = {
        'user_id': user_id,
        'username': username,
        'status': status,
        'permissions_level': permissions_level,
    }
    
    return user_profile

def run_test_case_3():
    """
    Runs the test: generates a user and validates its properties.
    """
    print("--- Running TC_3: Random User Profile Validation ---")
    
    # 1. Generate the random user data
    print("Step 1: Generating random user profile...")
    user = generate_random_user()
    print(f"Generated Profile: {user}")
    
    # 2. Validate the generated data
    print("\nStep 2: Validating data integrity...")
    try:
        # Check if user_id is in a valid range
        assert 1000 <= user['user_id'] <= 9999
        print("  - PASSED: User ID is within the expected range.")
        
        # Check if the status is one of the allowed values
        assert user['status'] in ['active', 'pending', 'inactive', 'suspended']
        print("  - PASSED: Status is a valid option.")
        
        # Check if the permissions level is valid
        assert 1 <= user['permissions_level'] <= 5
        print("  - PASSED: Permissions level is within the valid range (1-5).")
        
        print("\n--- TC_3 Result: SUCCESS ---")
        
    except AssertionError as e:
        print(f"\n--- TC_3 Result: FAILED ---")
        print(f"Validation failed: {e}")

# This block allows the script to be run directly
if __name__ == "__main__":
    run_test_case_3()