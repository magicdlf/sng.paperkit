# Results and analysis

## Model 1

The model gives 38,639 adults on day 60. The population increases steadily, so the basic transition model is reasonable. Both curves in the second graph are almost the same, which shows the result is stable.

![Population changes predicted by Model 1.](assets/model-1-stages.png){#fig:m1-stages width=90%}

![Forager changes predicted by Model 1.](assets/model-1-workforce.png){#fig:m1-workforce width=90%}

The average number of visits is 1,269,285 per hive per day during days 20 to 29, so 2 hives are needed for the field.

## Model 2

The model gives 38,639 adults on day 60. The orange line drops during rain. This shows rain reduces the bee population. The stage curves are still smooth, so the model is not strongly affected by the weather.

![Population changes predicted by Model 2.](assets/model-2-stages.png){#fig:m2-stages width=90%}

![Forager changes predicted by Model 2.](assets/model-2-workforce.png){#fig:m2-workforce width=90%}

The average number of visits is 571,178 per hive per day during days 20 to 29, so 4 hives are needed for the field.

## Model 3

The model gives 37,581 adults on day 60. The curves become more realistic after we add the weather coefficients. Since this model considers more factors, we choose Model 3 as the most accurate model. The orange line recovers after rain, proving that the colony can recover by itself.

![Population changes predicted by Model 3.](assets/model-3-stages.png){#fig:m3-stages width=90%}

![Forager changes predicted by Model 3.](assets/model-3-workforce.png){#fig:m3-workforce width=90%}

The average number of visits is 502,791 per hive per day during days 20 to 29, so 4 hives are needed for the field.

## Weather parameters

The daily survival probabilities are 0.97, 0.99, 0.999, 0.985 and 0.955, using one parameter set in [@model2015]. We use 1500 eggs per day. Rain is placed on days 20 to 29. During rain in Model 3, the egg input is multiplied by 0.85, the hive-to-forager probability by 0.7, forager survival becomes 0.94 and 45 percent of foragers go out. We did not find all the weather parameters, so we assumed these values. They are reasonable because bees are less active in rain.

Model 3 gives the largest hive requirement and therefore gives the best result. The figures of all three models have similar trends, which also verifies the models.
