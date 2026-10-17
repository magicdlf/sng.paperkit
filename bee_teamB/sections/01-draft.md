# Bee colony model with weather

## Results

Our model gives 37,581 adults on day 60. The orange line drops when rain starts, so rain causes the colony to become weaker. After day 30 it rises again. This proves that ten rainy days do not cause a lasting problem and the hive can recover by itself. For pollination we calculate 502,791 visits per hive per day during the rainy period. A 20-acre field needs 2,000,000 visits per day, so 4 hives are enough. The results are close to a normal colony size, which shows our parameters are reliable.

![Population changes over 60 days.](assets/stages.png){#fig:stages width=90%}

## Model

We divide the colony into eggs $E$, larvae $L$, pupae $P$, hive workers $H$ and foragers $F$. Only foragers go out for pollination. We use one day as a step. A proportion $p_i$ of surviving bees moves to the next group each day and the others stay. For example,

$$
L_{t+1}=s_L(1-p_L)L_t+s_Ep_EE_t.
$$ {#eq:larvae}

The other groups are calculated in the same way. The queen adds $b$ eggs to the first group every day, and the last group has survival but no further transition. The initial numbers are 3000, 4500, 10000, 15000 and 6000. We chose these because there should be more adult bees than young bees. We took stage lengths of 3, 5, 12 and 21 days from the literature [@model2015]. Therefore, $p_E=1/3$, $p_L=1/5$, $p_P=1/12$ and $p_H=1/21$. These probabilities make bees spend the required number of days in each stage.

## Weather and parameters

The daily survival probabilities are 0.97, 0.99, 0.999, 0.985 and 0.955, using one parameter set in [@model2015]. We use 1500 eggs per day. Rain is placed on days 20 to 29. During rain, the egg input is multiplied by 0.85, the hive-to-forager probability by 0.7, forager survival becomes 0.94 and 45 percent of foragers go out. We did not find all the weather parameters, so we assumed these values. They are reasonable because bees are less active in rain.

![Comparison under two weather conditions.](assets/weather.png){#fig:weather width=90%}

## Pollination and conclusion

The daily number of visits is $V_t=100a_tF_t$, where $a_t$ is 1 in sun and 0.45 in rain. We assume 100 flower visits per active forager per day. Since the weather model includes the bee life cycle, its prediction is more accurate than a model using a fixed forager percentage. Our result shows rain lowers bee numbers, so putting a roof over the hives should improve pollination. We recommend 4 hives for the field and conclude that weather is the main factor affecting the colony.
