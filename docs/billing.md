# Billing

## Credits and Limits

Transpose uses a credits system to manage API usage. Each team has an associated tier, and each tier comes with a fixed number of credits used per month. For information on our tiers, and to understand more about how much credits get you in terms of compute and data, check out our [pricing page](https://transpose.io/pricing) and our [pricing blog post](https://www.transpose.io/blogs/sql-usage-pricing).

## Overages

Overages allow you to use more credits than your monthly allowance at a fixed-price per credit. To protect you against accidental usage and charges, Overages are turned off by default. You can enable Overages through the [Transpose App](https://app.transpose.io).

## Tracking your usage

### Overall Usage

To track your monthly usage so far, visit the [Transpose App](https://app.transpose.io).

### Per-Request Usage

Every API request returns the number of credits used by the query in an `X-Credits-Charged` header. For example:

{{ transpose_fenced_sql('SELECT contract_address from ethereum.nfts LIMIT 100') }}

{{ transpose_colored_link(link_type='discord', text='Got questions?  Join our Discord') }}
