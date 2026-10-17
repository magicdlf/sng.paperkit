# Model 3 Weather adjustment and pollination

### Weather adjustment

The sunny values are used as the basic parameters. For rainy days we reduce the birth rate and the transition probability, and use a lower survival rate. The coefficients are given with the simulation results below. The weather adjustment makes the model closer to the actual situation.

### Pollination model

The daily number of visits is $V_t=100a_tF_t$. We use the average during the rainy period to calculate the number of hives. Therefore, $h=\lceil D/\overline{V}\rceil$.

[Need to explain the average and add the units.]
