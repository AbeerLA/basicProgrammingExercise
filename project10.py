# Input the email address
email = input("Enter the email address: ")

# Extract the domain name
domain = email.split('@')[-1]

# Print the domain name
print("Domain name:", domain)