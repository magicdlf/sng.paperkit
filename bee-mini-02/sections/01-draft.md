# Honeybee population and pollination

## Population model

We start with 1000 bees. Every day 150 bees are born and 200 bees die, so $N(t)=1000+150t-200t$, where $t$ is days. Figure 1 shows the population in 30 days. It becomes zero at day 20, so the hive will disappear. This answers how the population changes with time. The result is reasonable because we included both birth and death.

## Seasonal improvement

In summer bees are more active, so we multiply the birth number by 1.5. The improved model is $N_s(t)=1000+1.5(150)t-200t$. Now the population increases and reaches 1750 on day 30. Compared with the first model, the seasonal model is more accurate because it considers the weather. The population changes from decreasing to increasing, so birth rate is the most important factor. We suggest keeping the hive warm to increase the birth rate.

![Population predicted by the original and summer models.](assets/population.png){#fig:population width=90%}

## Number of hives

For the 20-acre field, we assume there are 2,000,000 flowers and each bee visits 100 flowers per day. One hive has 1750 bees according to our summer model, so it can pollinate 175,000 flowers per day. Therefore, the number of hives is $h=2000000/(1750\times100)=11.43$. We round up and recommend 12 hives. Figure 2 shows that 12 hives can cover all the flowers, while 10 hives cannot. Thus our model solves the pollination problem and farmers can use 12 hives for their field.

![Daily pollination capacity for different numbers of hives.](assets/pollination.png){#fig:pollination width=90%}
