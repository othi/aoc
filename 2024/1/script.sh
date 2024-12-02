#!/bin/bash
col1=`cat input | cut -d' ' -f1 | sort`
col2=`cat input | cut -d' ' -f4 | sort`

# cheating using unix tools
paste <(echo "$col1") <(echo "$col2") | awk '{print $2 - $1}' | paste -sd+ - | sed -e 's/-//g' | bc

# 'pure' bash
sum=0
while IFS=$'\n' read -r val1 && IFS=$'\n' read -r val2 <&3; do
    diff=$((val2 - val1))
    sum=$((sum + ${diff#-}))
done < <(echo "$col1") 3< <(echo "$col2")

echo $sum