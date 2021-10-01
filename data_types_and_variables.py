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


amount