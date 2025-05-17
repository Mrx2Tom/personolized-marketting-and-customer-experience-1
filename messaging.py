from jinja2 import Template

def generate_message(user, segment):
    with open("templates/email_template.txt") as file:
        template = Template(file.read())
    
    category_offers = {
        0: "a 20% discount on Tech gadgets",
        1: "exclusive access to premium Sports gear",
        2: "a buy-one-get-one-free deal in Fashion"
    }
    
    offer = category_offers.get(segment, "special discounts available now")
    
    message = template.render(
        name=user.get("user_id")[:6], 
        category=user.get("preferred_category"),
        offer=offer
    )
    return message

def send_campaign(df):
    for _, user in df.iterrows():
        msg = generate_message(user, user['segment'])
        print(f"Sending to {user['user_id'][:8]}:\n{msg}\n---\n")
