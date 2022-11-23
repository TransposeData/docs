# Quickstart

## Introduction

Let’s start by setting the scene; you’re a developer working on a cutting-edge Web3 data enabled product.  You need low-latency, high-bandwidth, interpretable, realtime information from the blockchain to make your product stand out.  Fortunately, you’ve chosen Transpose, and this makes integrating any arbitrary Web3 data into your production application a breeze.

In this example, we’ll be focusing on pulling daily [floor prices](https://blog.chain.link/what-is-an-nft-floor-price/) for the CryptoPunks NFT collection.  You might be interested in integrating this data for any number of reasons; maybe you want this information for analytics, for executing realtime trades, or for helping to understand the liquidity of the NFT collection.

Before we get started, it’s important to note that NFT pricing data is only one of the limitless applications of Transpose data.  Transpose indexes over 99.9% of trading volume on the Ethereum blockchain, and all of this data is accessible through our REST and SQL APIs.  We’ll work with our SQL API, and with one of our REST APIs, in this quickstart guide.

## Authentication

{{ get_transpose_api_key() }}

{{ transpose_fenced_rest('https://api.transpose.io/token/owners-by-contract-address', { 'chain_id': 'ethereum', 'contract_address': '0x123' }) }}

{{ transpose_fenced_sql('SELECT 2 FROM nft.sales') }}
