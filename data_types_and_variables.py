def get_total_price():
    the_little_mermaid = 3
    brother_bear = 5
    hercules = 1
    return (the_little_mermaid + brother_bear + hercules)*3


print(get_total_price())


def get_that_cheese():
    google = 400
    amazon = 380
    facebook = 350
    return (google * 6) + (amazon * 4) + (facebook * 10)

print(get_that_cheese())


can_enroll = True
schedule_conflict = False
can_take_class = can_enroll and not schedule_conflict

print(can_take_class)


product_offer = True
more_than_two_items = True
offer_expired = False
premium_member = True

if (more_than_two_items and offer_expired) or premium_member:
    print(product_offer)

print('hello')

username = 'codeup'
password = 'notastrongpassword'

pw_at_least_five_characters = len(password) >= 5
    
user_name_less_than_twenty = len(username) < 20

not_the_same = username != password


print(pw_at_least_five_characters)
print(user_name_less_than_twenty)
print(not_the_same)