'''
Q. Find the growth rate of active users for Dec 2020 to Jan 2021 for each account. 
   The growth rate is defined as the number of users in January 2021 divided by 
   the number of users in Dec 2020. Output the account_id and growth rate.
    material: https://platform.stratascratch.com/coding/2052-user-growth-rate?code_type=2

    date: datetime64[ns]
    account_id: object
    user_id: object
'''

# 0. final goal: (growth rate) = (number of users in Dec 2021) / (number of users in Dec 2020)

# 1. define "active users"
#       (active users) = (users who have at least one event in the month we are interested in)
import pandas as pd

sf_events = pd.read_csv('data.csv')

sf_events['year'] = sf_events.date.dt.year
sf_events['month'] = sf_events.date.dt.month

sf_events_before = sf_events[(sf_events['year']==2020)&(sf_events['month']==12)]
sf_events_after = sf_events[(sf_events['year']==2021)&(sf_events['month']==12)]

# 2. calculate the number of users in Dec 2020
n_active_user_before = sf_events_before.groupby('account_id').user_id.nunique()

'''
account_id  user_id
0           3
1           6
2           7
3           4
'''

# 3. calculate the number of users in Dec 2021
n_active_user_after = sf_events_after.groupby('account_id').user_id.nunique()

# 4. calculate (growth rate) = (number of users in Dec 2021) / (number of users in Dec 2020)
sf_events_before.remane(columns={'user_id':'user_id_2020'})
sf_events_after.remane(columns={'user_id':'user_id_2021'})
n_active_user = n_active_user_before.merge(n_active_user_after, on=['account_id'], how='left')

n_active_user['growth_rate'] = n_active_user['user_id_2021'] / n_active_user['user_id_2020']
print(n_active_user[['account_id','growth_rate']])

'''
account_id  growth_rate
0           1.5
1           2.0
2           1.7
3           1.2
'''
