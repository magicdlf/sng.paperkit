# Modelling

## Model 1

### Population transition

We divide the colony into eggs $E$, larvae $L$, pupae $P$, hive workers $H$ and foragers $F$. Only foragers go out for pollination. We use one day as a step. A proportion $p_i$ of surviving bees moves to the next group each day and the others stay. For example,

$$
L_{t+1}=s_L(1-p_L)L_t+s_Ep_EE_t.
$$ {#eq:larvae}

The other groups are calculated in the same way. The queen adds $b$ eggs to the first group every day, and the last group has survival but no further transition. The initial numbers are 3000, 4500, 10000, 15000 and 6000. We chose these because there should be more adult bees than young bees. We took stage lengths of 3, 5, 12 and 21 days from the literature [@model2015]. Therefore, $p_E=1/3$, $p_L=1/5$, $p_P=1/12$ and $p_H=1/21$. These probabilities make bees spend the required number of days in each stage.
\n
## Remaining transition equations

$$
E_{t+1}=s_E(1-p_E)E_t+b.
$$ {#eq:eggs}

The equations for pupae, hive bees and foragers can be obtained similarly. We put the five groups into a transition matrix and use Python to calculate them day by day.

[Insert the full matrix here. Check whether the forager group needs a leaving probability.]

## Model 2

Model 2 keeps the population equations of Model 1. We add an activity proportion $a_t$: it is 1 on sunny days and 0.45 during rain. The available foragers are $a_tF_t$. This improves the population prediction by considering rain.

## Model 3

### Weather adjustment

The sunny values are used as the basic parameters. For rainy days we reduce the birth rate and the transition probability, and use a lower survival rate. The coefficients are given with the simulation results below. The weather adjustment makes the model closer to the actual situation.

### Pollination model

The daily number of visits is $V_t=100a_tF_t$. We use the average during the rainy period to calculate the number of hives. Therefore, $h=\lceil D/\overline{V}\rceil$.

[Need to explain the average and add the units.]
