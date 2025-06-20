#!/bin/bash

#swiftBar Plugin 
#Title: Exchange Rate (USD -> EUR)
#Refresh: 5m

rate=$(curl -s "https://api.exchangerate.host/latest?base=USD&symbols=EUR" | jq '.rates.EUR')

printf "💱 USD→EUR: %.4f\n" "$rate"
echo "---"
echo "Updated: $(date)"