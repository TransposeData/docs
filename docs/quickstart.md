# Quickstart

## Introduction

Let’s start by setting the scene; you’re a developer working on a cutting-edge Web3 data enabled product.  You need low-latency, high-bandwidth, interpretable, realtime information from the blockchain to make your product stand out.  Fortunately, you’ve chosen Transpose, and this makes integrating any arbitrary Web3 data into your production application a breeze.

In this example, we’ll be focusing on pulling daily [floor prices](https://blog.chain.link/what-is-an-nft-floor-price/) for the CryptoPunks NFT collection.  You might be interested in integrating this data for any number of reasons; maybe you want this information for analytics, for executing realtime trades, or for helping to understand the liquidity of the NFT collection.

Before we get started, it’s important to note that NFT pricing data is only one of the limitless applications of Transpose data.  Transpose indexes over 99.9% of trading volume on the Ethereum blockchain, and all of this data is accessible through our REST and SQL APIs.  We’ll work with our SQL API, and with one of our REST APIs, in this quickstart guide.

## Authentication

Before we can learn about any CryptoPunks, we need to authenticate ourselves with Transpose.  To access any Transpose API, we need an API key.  In Transpose, each user belongs to a team, and teams can share API keys between them.

As such, if you haven’t already, you’ll need to [sign up and create a team (for free!)](https://app.transpose.io).

Remember not to share your API key! Your API key is a secret and should not be stored or exposed in a public manner.

All API requests should include your API key in an `X-API-KEY` HTTP header.

## 1) Get all CryptoPunks NFT sales

Given that our final goal is to understand daily floor prices (the lowest price that a CryptoPunk was sold for on a given day), to get started it makes sense to pull the complete set of sales data from CryptoPunks throughout their entire history.

This is a very standard use-case, and we can leverage Transpose’s REST API to do this.  Specifically, we’ll use `api.transpose.io/nft/sales-by-contract-address`.  We’ll need to pass the blockchain we want (Ethereum), the CryptoPunks contract address (`0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB`), the desired ordering (ascending, specified as `asc`), and a limit on the number of results we’d like (in this case, we’ll just do 10).


{{ transpose_fenced_rest('https://api.transpose.io/nft/sales-by-contract-address', { 'chain_id': 'ethereum', 'contract_address': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB', 'order': 'asc', 'limit': 10 }) }}

Voila!  How easy was that?

## 2) Group CryptoPunks sales by date

So, we’ve got every CryptoPunk sales event in all of history.  Now, the next step is to group this data by the date that it occurred on.  

Transforms and aggregations on huge datasets?  Sounds like a job for SQL!  With the Transpose SQL API, we do all the heavy lifting for you - you give us a query, we return you the results in milliseconds.  Let’s put that to the test, and group these results by date.

The following SQL query selects all NFT sales, filters them to only include CryptoPunks, groups them by date, and returns the count of the number of sales events that occurred on that particular day - an important step towards our ultimate goal of calculating the daily floor price.

{{ transpose_fenced_sql("SELECT\n/* extract date */\ntimestamp::date AS date,\n/* count number of sales */\nCOUNT(*) AS num_sales,\n/* calculate smart floor price as bottom 5 percentile of USD sale prices */\npercentile_disc(0.2) WITHIN GROUP (ORDER BY usd_price) AS floor_price\nFROM ethereum.nft_sales AS sales \n/* specify BAYC contract address */\nWHERE sales.contract_address = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'\n/* group sales by date */\nGROUP BY date\n/* skip days with no sales */\nHAVING COUNT(*) > 0; ") }}
