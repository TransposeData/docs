# Billing

## Credits and Limits

Transpose uses a credits system to manage API usage.  Each team has an associated tier, and each tier comes with a fixed number of credits used per month.  For information on our tiers, and to understand more about how much credits get you in terms of compute and data, check out our [pricing page](https://transpose.io/pricing) and our [pricing blog post](https://www.transpose.io/blogs/sql-usage-pricing).

## Overages

## Tracking your usage

### Overall Usage

Understanding how many credits you use is an important capability.  To track your monthly usage so far, visit the [Transpose App](https://app.transpose.io).

### Per-Request Usage

Every API request returns the number of credits used in a

{{ transpose_fenced_sql('SELECT * from ethereum.nfts LIMIT 1') }}

Questions?  Join our Discord, and chat with the team today.

{{ transpose_colored_link(link_type='discord') }}
