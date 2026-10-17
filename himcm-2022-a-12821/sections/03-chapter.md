# Sensitivity Analysis {#sec:s3}

We divide sensitivity analysis into two parts-the variables selected and the percentage change regarding the alteration of the value of the variables.

## Baseline {#sec:s3-1}

We conducted a sensitivity analysis regarding our baseline model. We selected natural death rate $\lambda$, the number of eggs laid daily R, and K as variables. We altered the variables $\pm10\%$, and the resulting percentage changes of the model are around $\pm10\%$, meaning our variables have a linear relationship with our baseline model, proving our model's stability and credibility.

![Original baseline sensitivity table: baseline sensitivity, critical and maximum population panels](assets/source-table-2a.png){#fig:source-table-2a width=98%}

![Original baseline sensitivity table continued: yearly population panels](assets/source-table-2b.png){#fig:source-table-2b width=98%}

## Virus {#sec:s3-2}

The demise of mite-infested colonies has come to be associated with the persistent infection known as Deformed Wing Virus (DMV) [@ref13]. When DWV is injected into the pupa during development, this shortens adult life expectancy by 50%-75%, which results in 2-4 times the initial death rate (0.015). So we estimate the death rate caused by the virus would be 0.04. On the 400th day in our model, the virus is introduced as the colony population has reached a relatively stable state. Applying the DMV-influenced death rate to our model and adjusting the transmission rate results in the conclusion that the system will eventually reach an equilibrium (survive or extinction).

We have created four scenarios where the death rate and transmission rate are individually high or low in order to assess the total impact of these rates on the population amount in a stable state. The conclusion suggests that, in comparison to the transmission rate, the death rate has a more significant impact on the steady-state population, which is consistent with the real-life situation.

![Comparison between different transmission rate and death rate of virus (panel 1 of 4)](assets/source-figure-12.png){#fig:source-figure-12 width=95%}

![Comparison between different transmission rate and death rate of virus (remaining panels)](assets/source-figure-13.png){#fig:source-figure-13 width=95%}

In order to determine how the death rate or the transmission rate separately has an effect on the colony population, we made each of these rates into controlled variables. While controlling the death rate of the virus, since it shortens 50%-75% lifespan of bees, the corresponding death rate is 0.03-0.06, and we decided the death rate of the virus to be 0.04 as a medium rate in the range. Results have shown that the population will decline in death or transmission rates. The percentage change of the population is decreasing yet when the transmission rate is large to a certain value, the percentage change will become relatively constant; this situation does not occur in the death rate. With the increase in the death rate, the percentage change decreases and then increases. This phenomenon suggests that whereas an increase in the death rate affects the population continuously, an increase in the transmission rate has a diminishing effect on the population after it reaches a certain point.

| Transmission rate | Death rate | Equilibrium population | Days needed | Percentage change |
| --- | --- | --- | --- | --- |
| 0.1 | 0.04 | 42,891 | 419 | -- |
| 0.15 | 0.04 | 34,300 | 285 | 20.03% |
| 0.2 | 0.04 | 30,893 | 270 | 9.93% |
| 0.25 | 0.04 | 29,070 | 257 | 5.90% |
| 0.3 | 0.04 | 27,932 | 249 | 3.91% |
| 0.35 | 0.04 | 27,156 | 244 | 2.78% |
| 0.4 | 0.04 | 26,588 | 240 | 2.09% |
| 0.45 | 0.04 | 26,157 | 233 | 1.62% |
| 0.5 | 0.04 | 25,820 | 235 | 1.29% |
| 0.55 | 0.04 | 25,545 | 232 | 1.06% |
| 0.6 | 0.04 | 25,320 | 229 | 0.88% |
| 0.65 | 0.04 | 25,131 | 227 | 0.75% |
| 0.7 | 0.04 | 24,970 | 223 | 0.64% |
| 0.75 | 0.04 | 24,832 | 223 | 0.55% |
| 0.8 | 0.04 | 24,711 | 221 | 0.49% |

Table: Sensitivity analysis of transition rate {#tbl:transition}

*Note that the first percentage change is considered invalid as the percentage change from 0.0 is different compared to other changes. Same applies to the next table.

| Transmission rate | Death rate | Equilibrium population | Days needed | Percentage change |
| --- | --- | --- | --- | --- |
| 0.4 | 0.02 | 42,816 | 285 | -- |
| 0.4 | 0.025 | 37,363 | 270 | 12.74% |
| 0.4 | 0.03 | 33,051 | 259 | 11.54% |
| 0.4 | 0.035 | 29,535 | 245 | 10.64% |
| 0.4 | 0.04 | 26,588 | 240 | 9.98% |
| 0.4 | 0.045 | 24,064 | 233 | 9.49% |
| 0.4 | 0.05 | 21,850 | 234 | 9.20% |
| 0.4 | 0.055 | 19,869 | 234 | 9.07% |
| 0.4 | 0.06 | 18,053 | 237 | 9.14% |
| 0.4 | 0.065 | 16,337 | 244 | 9.51% |
| 0.4 | 0.07 | 14,633 | 267 | 10.43% |
| 0.4 | 0.075 | 12,771 | 314 | 12.72% |
| 0.4 | 0.08 | 4 | 679 | 99.97% |
| 0.4 | 0.085 | 4 | 343 | 0.00% |
| 0.4 | 0.09 | 4 | 275 | 0.00% |

Table: Sensitivity analysis of death rate {#tbl:death}

We controlled the transmission rate to find the least death rate that can cause extinction. The findings showed that the death rate has a greater impact on colony population extinction, and the higher the transmission rate, the lower the death rate required to bring a colony to extinction. As time goes on, the death rate decreases and becomes slower. The time to reach an equilibrium state of the population has small oscillations, but overall it decreases as the transmission and death rate rise. The death rates we gained are around 0.06, which is similar to the death rate of DMV in real life, which proves our model to be effective.

| Transmission rate | Threshold death rate |
| --- | --- |
| 0.5 | 0.074 |
| 0.55 | 0.073 |
| 0.6 | 0.072 |
| 0.65 | 0.071 |
| 0.7 | 0.07 |
| 0.75 | 0.069 |
| 0.8 | 0.0684 |
| 0.85 | 0.068 |
| 0.9 | 0.0677 |
| 0.95 | 0.0675 |
| 1 | 0.0673 |

Table: Threshold death rates of extinction under different transmission rates {#tbl:threshold}

## Seasonality {#sec:s3-3}

To assess the sensitivity of the longest lifespan of the honeybee and the maximum fertility rate of the queen bee, we calculated the percentage change of the model after adjusting the values.

We selected mmax and Rmax as variables. We did not select am as the amplitude of the model is relatively the same when it is decreasing or increasing, and considering the change in am will result in the change of lifespan, making the fertility rate negative, we did not choose am and the percentage change of mmax or Rmax to shrink 10%.

According to the sensitivity analysis shown below, the oscillation of the model brought on by altering K is adequate when K changes by 10% and -10%, the change of maximum population and critical population changes around 0.1% and 10%, respectively, which suggests that our model is stable. A similar linear relationship between the model's output and the percentage change of the variables was produced when mmax and Rmax were changed. Although adjusting mmax caused the model's outcome to vary by a large factor, this is due to the initial dates being different, thus the percentage change is actually about smaller of the model's result.

| Parameter | Ratio to standard | Maximum population change | Critical population change |
| --- | --- | --- | --- |
| standard | 100% | 0.00% | 0.00% |
| $m_{max}$ | 110% | 31.39% | -23.56% |
| $m_{max}$ | 120% | 61.67% | -37.63% |
| $R_{max}$ | 110% | 24.58% | -19.03% |
| $R_{max}$ | 120% | 49.11% | -31.43% |
| $K$ | 90% | 0.13% | -10.07% |
| $K$ | 110% | -0.12% | 10.09% |

Table: Impact of transmission rate and death rate to extinction (original caption) {#tbl:seasonality}

To assess how well the seasonality functions, we compared it to the baseline model. As the curve is extremely close to the equilibrium curve in year 3, indicating that it has nearly attained the equilibrium state, we determined the average lifespan in year 3. The average lifespan of bees can be calculated by dividing the average daily population by the average birth rate since one population corresponds to a new day of lifespan. The average lifespan, $\lambda$1 , yields a value of 0.0137, which is close to the baseline model's value of 0.015. This demonstrates the accuracy and reliability of our model.

## Discussion {#sec:s3-4}

Overall, the longest life span mmax (the smallest $\lambda$) has the greatest impact on our model, while Rmax also has a substantial influence on our model. This is owing to the extended lifespan and rising fertility will allow the population to accumulate, having a dramatic effect and causing a disproportionately large response in the overall population growth.
