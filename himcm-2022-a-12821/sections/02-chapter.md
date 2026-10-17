# Population Model {#sec:s2}

## Variables {#sec:s2-1}

| Variable symbol | Meaning |
| --- | --- |
| $N(t)$ | Population size at time t |
| $N_C$ | Critical population |
| $N_{\max}$ | Maximum sustainable population |
| $\sqrt K$ | Colony size where brood survival is half maximum |
| $R$ | Average eggs laid by queen per day |
| $\lambda$ | Probability of natural death per day |
| $t$ | Time in days |
| $m$ | Average lifespan |
| $m_{\max}$ | Longest lifespan in one year |
| $m_{\min}$ | Shortest lifespan in one year |
| $t_0$ | Starting date |
| $\varphi_0$ | Interval from t0 to last 22 December |
| $a_m$ | Lifespan amplitude |
| $R_{\max}$ | Maximum daily eggs |
| $R_{\min}$ | Minimum daily eggs |
| $a_R$ | Fertility amplitude |
| $N_I(t)$ | Infected and infectious population |
| $N_S(t)$ | Susceptible population |
| $\alpha$ | Transmission rate |
| $\mu$ | Recovery probability |
| $d_I$ | Death probability due to infection |

Table: Variables in the population model {#tbl:population-vars}

## Baseline Model {#sec:s2-2}

### Model Setup {#sec:s2-2-1}

Prior to creating a model that incorporates all the factors that influence a honeybee colony's population over time(in days), a baseline model ought to be constructed. This model's assumption applies to all the models developed afterward.

The social organization of honey bees includes the reproductive division of work where each honey bee colony is comprised of a queen (reproductive female responsible for laying eggs), workers (nonreproductive females), and drones (males). Additionally, the number of deaths per unit of time is proportionate to the population. These two factors are the major components of the population change in the honeybee colony.

To begin with, consider the population size N(t) at time t where time is in the unit of days, and we have the population growth per unit time to be:

$$
\frac{dN}{dt}=\underbrace{\frac{N^2}{K+N^2}R}_{\text{Birth per day}}-\underbrace{\lambda N}_{\text{Death per day}}
$$ {#eq:baseline}

The birth of new honeybees is assumed to be the the average number of eggs laid by the queen per N2 day R, multiplied by the survival rate of the brood K+N 2 . The survival rate is determined by the population

size N(t) at time t, together with the carrying capacity of the population K. Thus the total new birth per N2 unit time can be written as K+N  2 R.

$\lambda$ can be treated as the probability of individual death per day or from the entire population's point of view the proportion or rate of death per day. So the death in unit time may be represented as a constant proportion of the total population, which is $\lambda$N.

### Allee Effect {#sec:s2-2-2}

The Allee effect, a phenomenon in biology marked by a link between population size or density and the mean individual fitness of a population or species [@ref4], is illustrated by this model. When the population N2 N grows to infinity, the survival probability of new brood K+N      2 reaches its approaches to 100% and the

number of newborns is consequently approaching the number of eggs laid R. Conversely, as N shrinks to N2 zero, the survival probability of new brood K+N  2 declines to 0, reducing the birthrate. Due to the constant N2 death rate $\lambda$N, the nonlinear term K+N 2 has an influence on the system that results in an Allee threshold, or critical population, below which the colony will collapse over time and above which it will be able to survive and grow over time.

This applies to the impacts of collaboration in honeybee colonies, where larger colonies result in stronger cooperative efforts between the hive and foraging bees to ensure the survival of young bees. The

N2 term K+N  2 represents the probability of an egg turning into an adult. It also denotes that for an egg to

develop into a worker bee, care must be provided by adult workers (N) inside the colony, as well as food brought in by foragers. Additionally, this term implies that having more adult workers in the colony can boost the survival of an egg and its development into an adult. Due to the constant death rate $\lambda$N, the N2 nonlinear term K+N   2 has an influence on the system that results in an Allee threshold, below which the

colony will collapse and above which it will be able to survive.

### Critical and Maximum Sustainable Population {#sec:s2-2-3}

There are two steady-states in our baseline model. Setting the right-hand side of [@eq:baseline] to be 0,

$$
\frac{N^2}{K+N^2}R-\lambda N=0
$$

This can be rearranged into a quadratic equation for N.

$$
\lambda N^2-RN+\lambda K=0
$$

$$
N_C=\frac{R-\sqrt{R^2-4\lambda^2K}}{2\lambda}
$$ {#eq:critical}

$$
N_{\max}=\frac{R+\sqrt{R^2-4\lambda^2K}}{2\lambda}
$$

### Parameter Calibration and Model Results {#sec:s2-2-4}

We set $\lambda$ to be 0.015, indicating an average lifespan of 1/$\lambda$ $\approx$ 67 days. R is set to be 1500 eggs per day. K is determined by the critical population given by [@eq:critical] (when dN  dt = 0). We take the critical population to be 1000, plug in the values of $\lambda$ and R into $\sqrt{}$  [@eq:critical], and we get that K = 9.9x107 .[@ref5] This means that when the population of a colony reaches K $\approx$ 9950, the survival probability of new brood becomes 50% [@ref11].

We analyzed the population growth with and without the Allee effect in order to validate the significance of the Allee effect on our model. The average number of eggs laid by the queen bee per day R, death rate $\lambda$, and K respectively are 1500, 0.015, and 9.9x107 . We used 6 characteristics of the model to conduct analysis: critical population, maximum population, time to reach 90% of the maximum sustainable population, and change in population in 1 st , 2nd , and 3rd year.

[@fig:source-figure-1] illustrates the short-term effect of the Allee effect in our model, introduced by the term of the N2 survival probability K+N   2 . When the initial population is comparatively small, a lower survival probability

results in a lower fertility rate than the ideological value, so the rate of population expansion is lower when the Allee effect is incorporated into the model than it would be without it.

![Population change in 1 year starting at 3000 with Allee effect](assets/source-figure-1.png){#fig:source-figure-1 width=82%}

[@fig:source-figure-1] illustrates population growth for a longer time. The Allee effect has a substantial impact by the first year with a percentage change compared to the initial population of 3176.19%, whereas the two lines are about parallel in the second and third year (3199.89% and 3200.00%, which is the percentage change compared to the initial population at day 1), showing a relatively minor impact. This is due to the N2 carrying capacity having been reached and K's importance decreases as N increases in K+N    2 . The time to

reach 90% maximum population is 187 days as shown below, indicating the growth of the population.

![Population change in 3 years starting at 3000 with Allee effect](assets/source-figure-2.png){#fig:source-figure-2 width=90%}

![Population change in 1 year with different initial population with Allee effect](assets/source-figure-3.png){#fig:source-figure-3 width=88%}

[@fig:source-figure-3] demonstrates the relationship between different initial population and its impact on population growth over time. The two red lines indicate the carrying capacity (99000) and the Allee threshold (1000 bees); these two population points are the points where the population will not grow or shrink. The critical point, or Allee threshold, is set at 1000 bees [@ref5], below which the colony will collapse and

above which it can flourish. As there were not enough adult workers in the colony to maintain the eggs' survival rate, the population below 1000 in this graph steadily shrank to zero, but the population above 1000 thrived and eventually reached a colony of 99000 bees. The carrying capacity of the population, or the most number of individuals the ecosystem can support, is 99000. Therefore, all initial population above the Allee threshold will eventually approach to the carrying capacity of 99000 bees.

## With Virus {#sec:s2-3}

### Model Setup {#sec:s2-3-1}

Deformed Wing Virus is a persistent pathogen that has become synonymous with the death of miteinfested colonies across the world. When DWV is injected into developing pupa, this causes a reduction in adult lifespan of 50-75%, which lead to 2 to 1.5 times the original death rate (0.02). We introduce the virus on the 400th day in our model. By applying the death rate influenced by DMV to our model and changing the transition rate, we find out that the system will finally reach an equilibrium (symbiosis or extinction).

In order to determine how the colony population is affected by the virus, this model "compartmentalizes" the population, each honeybee in the population is in exactly one of the three groups:

- NS : the population that is susceptible to the disease (namely, honeybees who have not had the infection or recovered from the infection).

- NI : the population infected with the virus and are themselves infectious.

![The flowchart of the virus model](assets/source-figure-4.png){#fig:source-figure-4 width=90%}

We assume that a disease is spreading through a population of growing size N, and NS , NI , the number of honeybees in the two groups respectively. Individuals can move from NS $\to$ NI (infection) and from NI $\to$ NS (recovery), so NI and NS can all change with time.

The dynamics of the colony population can be specified with three parameters:

- $\alpha$, the transmission rate, which is the number of contacts a honeybee has each probability of catching the disease from contact with an infected honeybee

- $\mu$: the probability of recovery when infected

- dI : the incremental probability of death when infected, in addition to the probability of natural 1 death. This means the average length of the infection is $\lambda$+$\mu$+d I , where death due to infection and natural causes and the recovery rate are considered.

With these parameters, the dynamics of the honeybee population with virus is summarized in [@fig:source-figure-4].

The population growth rate can be decomposed into:

$$
\frac{dN}{dt}=\frac{dN_I}{dt}+\frac{dN_S}{dt}
$$

According to the dynamics illustrated in [@fig:source-figure-4], the dynamics of thesusceptible population can be

$$
\frac{dN_S}{dt}=\frac{N^2}{K+N^2}R-\lambda N_S-\frac{\alpha N_IN_S}{N}+\mu N_I
$$

dt     K+N                       N

where $\mu$ is the probability of recovery when infected, $\mu$NI represents the population recovered from the infection per unit time. $\lambda$ is the probability of natural death, $\lambda$N represents the population that died N2 from natural causes. The fertility rate K+N  2 R and the recovery number $\mu$N I give rise to the susceptible

population, assuming all the newborns are uninfected. The natural deaths $\lambda$NS and infections $\alpha$·NNI ·NS reduces the susceptible population.

The infected population may be stated as:

$$
\frac{dN_I}{dt}=\frac{\alpha N_IN_S}{N}-d_IN_I-\mu N_I-\lambda N_I
$$

where $\alpha$ is the transmission rate, which is the number of contacts a honeybee has each day times the probability of catching the disease from contact with an infected person, we model the probability at which the susceptible adult honeybees are virus infected by the virus as $\alpha$·N N . Thus, the infections in total I

can be expressed as $\alpha$·NNI ·NS .

dt = dt + dt can be elaborated as: dNI  dNS

By combining the susceptible and infected population, dN

$$
\frac{dN}{dt}=\frac{N^2}{K+N^2}R-\lambda N-d_IN_I
$$

dt     K+N

Where dI is the probability of death caused by infection, dI NI represents the population that died due to the virus infection. The infected population $\alpha$·NNI ·NS grows when more bees are infected. The infected population drops when bees die of natural causes($\lambda$NI ), infections(dI NI ), or recover from the infection($\mu$NI ).

Further analysis of the how transition rate and death rate would influence the population would be elaborated in the sensitivity analysis.

### Parameter Calibration and Model Results {#sec:s2-3-2}

The death rate was set at 0.04 during parameter estimation, meaning that the infected bees live an average of 25 days. Since the DMV can reduce an infected bee's lifespan to 1733 days, it has been determined that a lifespan of 25 is the average. The transition rate is set at 0.4, indicating that 2.5 days are required for an infected bee to spread throughout a congested hive. We maintain the recovery rate at a constant 0.01, which is negligibly low when compared to the mortality rate.

![Honeybee population over time with virus](assets/source-figure-5.png){#fig:source-figure-5 width=95%}

## Seasonality {#sec:s2-4}

In the baseline model, the number of eggs laid by the queen and the lifespan of the honeybees are taken to be the average over the entire year. However, in reality both of those variables change over time.

### The Lifespan With Seasonal Change {#sec:s2-4-1}

The lifespan of the honeybee varies with seasonal change. Most honeybees labor themselves to death throughout the summer due to the heavy workload, which reduces their longevity. Honeybees may live longer in fall and winter (for a lifespan of four to six months). The probability of individual death $\lambda$ is inversely proportional to the expected lifespan m, which can be expressed by the equation:

$$
\lambda=\frac{1}{m}
$$

Since the lifespan of the honeybee is longer during autumn and winter, we assume the longest lifespan mmax occurs on 22 December, which is estimated to be the coldest temperature. Similarly, we assume that the shortest lifespan mmin occurs on 22June in the summertime. Thus, the function of lifespan m with

$$
m(t)=a_m\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(m_{\max}-a_m)
$$ {#eq:lifespan}

In this case, $\varphi_0$ is the horizontal translation of the function. $\varphi_0$ is defined as the time interval between t0 and the last 22 December, where t0 is the starting date of population change. Y represents a year, which

$$
a_m=\frac{m_{\max}-m_{\min}}{2}
$$

Here, the period of the function is 365 days. mmax is the longest lifespan of the honeybee and mmin is the shortest lifespan of the honeybee, so the amplitude is expressed.

The probability of individual death $\lambda$ is reciprocal of the lifespan m, which could be expressed by:

$$
\lambda=\frac{1}{a_m\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(m_{\max}-a_m)}
$$ {#eq:seasonal-death}

Substitute [@eq:seasonal-death] to the baseline model ([@eq:baseline]), we get:

$$
\frac{dN}{dt}=\frac{N^2}{K+N^2}R-\frac{N}{a_m\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(m_{\max}-a_m)}
$$

### The fertility with Seasonal change {#sec:s2-4-2}

The average number of eggs laid by the queen bee per day (R) varies with seasonal change. The number of eggs laid R increases in warmer seasons and decreases in colder seasons. Thus, we assume that R reaches its maximum on 22nd June and reaches its minimum on 22nd December. The function of the number of eggs laid R with respect to time t in days is a cosine function which is similar to what we

$$
R=-a_R\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(R_{\max}-a_R)
$$

In this case, $\varphi_0$ is the horizontal translation of the function. $\varphi_0$ is defined as the time interval between t0 and the last 22nd December, where t0 is the starting date of population change. Y represents a year, which is 365 days. Rmax is the highest fertility rate of the queen bee. aR is the amplitude of the function,

$$
a_R=\frac{R_{\max}-R_{\min}}{2}
$$

There is a negative sign before the amplitude because this is the reflection across the x-axis of the lifespan function. The lifespan is the longest in winter as the temperature is the lowest and the queen rarely lays eggs, so R has become Rmin .

Combining seasonality changes of both the lifespan and the fertility rate, we have that the final model

$$
\frac{dN}{dt}=\frac{N^2}{K+N^2}\left[-a_R\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(R_{\max}-a_R)\right]-\frac{N}{a_m\cos\left(\frac{t+\varphi_0}{Y}\,2\pi\right)+(m_{\max}-a_m)}
$$

### Parameter Calibration and Model Results {#sec:s2-4-3}

Our seasonality model features a critical threshold and a carrying capacity, similar to the baseline model. The population above the critical threshold thrives, whereas the population below it collapses. The second graph demonstrates how the population will gradually reach a carrying capacity (the maximum population that the environment is able to support) with different initial populations. In addition, our model's seasonality is demonstrated by the identical growth patterns in years 2 and 3.

![Population change in 1 year with different initial population starting on 1 January](assets/source-figure-6.png){#fig:source-figure-6 width=85%}

![Population change in 3 years with different initial population starting on 1 January](assets/source-figure-7.png){#fig:source-figure-7 width=95%}

We display the graphs below to show how the starting date (t0 ) affected the initial population. Varied t0 results in different initial population values. Despite the population's diverse starting positions, every graph has revealed a consistent, recognizable pattern. The curves with various starting dates are identical when translated horizontally. The curves are the same regardless of starting dates or initial populations and have a periodicity of 365 days (or one year). This illustrates the stability and validity of our seasonality model.

![Population change in 1 year with different initial population starting on different dates](assets/source-figure-8.png){#fig:source-figure-8 width=98%}

From the two graphs below, it can be implied that the population has a periodicity of one year: there is no difference between the three years regarding the pattern of the population change. Moreover, with

[@fig:source-figure-9] and [@fig:source-figure-10] with different initial dates of January and July, the difference is a horizontal translation, which indicates that the two graphs have the same pattern. This demonstrates the seasonality of our model.

![Critical curve starting on 1 January](assets/source-figure-9.png){#fig:source-figure-9 width=86%}

![Critical curve starting on 1 July](assets/source-figure-10.png){#fig:source-figure-10 width=86%}

This graph above illustrates the crucial point at 923 bees, below which the colony will collapse. The oscillations are larger than those of the previous initial graph because the initial population is relatively near the critical point. The curve pattern in three years is identical, implying the seasonality of our model is valid. In our seasonality model, the allee threshold (critical point) is 923 bees, while the carrying capacity is 96203 bees. These two numbers show that our model is robust and reliable because they are comparable to the baseline model's carrying capacity of 99000 bees and an allee threshold of 1000 bees.

As shown in the graph below, the seasonality function also has a maximum population. The graph's cycle is one year long, demonstrating the seasonality of our model.

![Maximum population curve starting on 1 January](assets/source-figure-11.png){#fig:source-figure-11 width=86%}

The new average lifespan of the model with seasonality can be calculated using the method of dividing the sum of the population each day by the total birth in a one-year period when the population is relatively

stable. This method can be interpreted as adding up all the lifespan of each individual, and divided by the total number of individual bees. We selected the third year from the start as the one-year time period with stable population, which can be justified by [@fig:source-figure-7].

In our model with seasonality, the average lifespan calculated this way is roughly 73 days, which is very close and comparable to the 67 days of average lifespan in the baseline model.
