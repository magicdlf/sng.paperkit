# Bee population

We assume there are 1000 bees in the hive at first. The queen produces 150 new bees every day and 200 bees die every day, so the population is $N=1000+150t-200t$. We used Python to calculate the population for 30 days. From the graph we can see the population decreases steadily. At day 20 there are no bees left, which means the colony cannot survive. Therefore, we think the queen should produce at least 200 bees every day to solve this problem. This model is reasonable because both birth and death are considered.

![The number of bees in 30 days](assets/population.png){#fig:population width=90%}
