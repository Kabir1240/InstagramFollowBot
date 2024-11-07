import os
import time
from dotenv import load_dotenv
from insta_follower import InstaFollower

# link to account
ACCOUNT_TO_FOLLOW = os.environ.get("ACCOUNT_TO_FOLLOW")

# creates InstaFollower object. logs into Instagram. Finds followers for given account. Follows everyone in account
follower = InstaFollower()
follower.login()
follower.find_followers(link=ACCOUNT_TO_FOLLOW)
