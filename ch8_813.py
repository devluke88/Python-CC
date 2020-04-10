#User profile

def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile

user_profile = build_profile('tyler', 'durden', location='new york', field='phycology', job='fighter')
print(user_profile)