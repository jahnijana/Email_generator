Email_pool = [     
    "jahnij@gmail.com",
    "bhavithach@gmail.com", 
    "geethug@gmail.com",
    "janu@gmail.com", 
    "lucky@gmail.com", 
    "jasmithaj@gmail.com",
    "priya@gmail.com",
    "soni@gmail.com", 
    "shabrin@gmail.com",
    "ananyarao@gmail.com",
    "bhanuk@gmail.com",
    "geethuk@gmail.com", 
    "nikkik@gmail.com",
    "snehak@gmail.com",
    "amita@gmail.com",
    "kavyajain@gmail.com", 
    "deepakyadav@gmail.com",
    "shrutiagarwal@gmail.com",
    "manishak@gmail.com", 
    "pallavireddy@gmail.com"
]

first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
email_domain = input("Enter your email domain (e.g. @gmail.com): ").lower()

if not email_domain.startswith("@") or "." not in email_domain or email_domain.count("@")!=1 or ".." in email_domain :
    print("Invalid Email.Enter valid email like 'jahnijana@gmail.com'.")
else:
    Email= f"{first_name}{last_name}{email_domain}"
    if Email in Email_pool:
        print(f"The email {Email} already existed.")
    else:
        print(f"Congratulations! Your email {Email} has been successfully created.")
        Email_pool.append(Email)

    
    print("\nUpdated email list:")
    for email in Email_pool:
        print(email)
