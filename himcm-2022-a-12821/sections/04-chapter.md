# Pollination Prediction {#sec:s4}

## Variables {#sec:s4-1}

| Variable symbol | Meaning |
| --- | --- |
| $H_{resource}$ | Honey needed by the area |
| $C_{nectar}$ | Nectar from one flower in one day |
| $C_{flower}$ | Density of flowers per unit area |
| $A$ | Orchard area |
| $h$ | Nectar to honey production rate |
| $p$ | Honeybee-produced fraction of honey |
| $\rho_{flower}$ | Flowers per tree |
| $a$ | Trees per unit area |
| $H_{hive}$ | Honey collected by one hive |
| $F$ | Forager population |
| $t_{flight}$ | Average foraging flight time |
| $k$ | Foraging efficiency coefficient |
| $N$ | Hive population |
| $n_{hive}$ | Hives required |
| $T$ | Temperature in degrees Fahrenheit |
| $\eta$ | Probability of foragers going out |
| $\delta$ | Polluted-to-standard foraging time ratio |
| $a_c$ | Transition rate |
| $N_U$ | Uncontaminated bees |
| $N_C$ | Contaminated bees |
| $\lambda_C$ | Extra death rate due to pesticide |

Table: Variables in the pollination prediction model {#tbl:pollination-vars}

## Model {#sec:s4-2}

To predict the amount of honeybee hives are required to support the pollination of a 20-acre parcel of land containing crops that benefit from pollination, we assumed the amount of honey is proportional to the number of pollination, we chose the amount of honey production to quantify the process of pollination. The mass of a hive's honey can be evaluated more with ease compared to using pollination.

The amount of honey that an area is able to produce can be represented can be described as:

$$
H_{\mathrm{resource}}=C_{\mathrm{nectar}}C_{\mathrm{flower}}Ahp
$$

Where the amount of honey that an area is able to collect can be represented as Hresource , with the area

of the orchard presented as A, Cnectar as the amount of nectar one flower has, and C f lower as the density of flower in unit area, h as the production rate from nectar to honey, and p as the percentage of nectar collected by honeybees with all the nectar secreted.

The amount of flowers in a unit area can be expressed as:

$$
C_{\mathrm{flower}}=\rho_{\mathrm{flower}}a
$$

With $\rho$ f lower as the number of flowers on one tree and a as the number of trees planted in a unit area.

The total amount of honey a hive can collect can be described as Hhive . We assume it is proportional with the number of foragers and inversely proportional to the time consumed for one foraging flight. The

$$
H_{\mathrm{hive}}\propto F\frac{1}{t_{\mathrm{flight}}}
$$

Where F is the population of foragers, t f light is the time of each foraging flight (in days). Then, k can be set as a proportionality coefficient and the relationship between F and Hhive can be expressed as

$$
H_{\mathrm{hive}}=kF\frac{1}{t_{\mathrm{flight}}}
$$

Moreover, the population of foragers F can be expressed as F = f · N, by assuming the number of foragers is proportional to the total population of honeybees in a hive. f is the fraction of foragers in the total population and N is the total population.

So, when the number of hives needed by a certain area of crops, nhive , can be stated as:

$$
n_{\mathrm{hive}}=\frac{H_{\mathrm{resource}}}{H_{\mathrm{hive}}}
$$

which the elaborated function of nhive can be:

$$
n_{\mathrm{hive}}=\frac{C_{\mathrm{nectar}}\rho_{\mathrm{flower}}aAhp}{kfN/t_{\mathrm{flight}}}
$$

## Values of parameters {#sec:s4-3}

Each bee forage for food with 10 flights per day [@ref17], so the average time of each flight is 0.1 days, h=0.4,p=0.35 [@ref12], and f is 20% [@ref24]. The bee population N of a typical hive we selected is 60,000 since most of the blossoms occur in spring.

We calculate the value of k by implementing the Hresource and number of hives which is 51, into our model [@ref12]. The value of k we obtained is 4.17 $\times$ 10-5 . Then, we utilize these parameters to calculate the number of hives needed for various types of crops in 81000 square meters.

## Number of hives for different crops {#sec:s4-4}

The first crop we selected is apple trees. For apple orchards, the amount of nectar produced by each apple flower per day is 2 $\times$ 10-6 kg [@ref19]. The number of flowers on one apple tree is 410 [@ref28]. For dwarf apple trees, normally, 485 apple trees are planted per acre [@ref2]. The number of hives required by 81000m2 of apple trees is 0.22 consequently, which is approximated as 1 hive.

We also select pear and watermelon as crops. For pear orchards, Cnectar is 8 $\times$ 10-6 kg [@ref6], $\rho$ f lower is 500 [@ref20][@ref1], a is 2000 per hectare [@ref16]. For watermelons, Cnectar is 1.4 $\times$ 10-5 kg [@ref22], $\rho$ f lower is 250 [@ref29], a is 4000 per acre [@ref25]. Noteworthily, the population of a hive in watermelon orchards is selected as 40,000 since the flowering season of watermelon is in summer, when the population is low. Thus, the number of hives required for an area of 81000m2 in each case is 1.43, approximated to 2 hives for pears, and 7.85, approximated to 8 hives for watermelons.

For the three crops listed above, with the same area of cropland, the number of hives needed by watermelons is higher than that of pears, and both higher than that of apples, mainly due to the different spacing of plants and the amount of nectar secretion.

Since the bees can normally travel up to 6km, the area of the 20-acre parcel of land can be all covered up by the range of bees' activity, which has a radius of 6 kilometers. Thus, the land only requires a single point of hives without arranging hives in a 2 dimensional plane, in order to meet the pollination requirement. The results we obtained can be justified by other results that 51 hives are needed by an area of radius 3km [@ref12], and placement of 2-3 hives/ha is recommended as a high rate to be adequate for pollinating apples [@ref18].

## Factors influencing foraging ability {#sec:s4-5}

### Temperature {#sec:s4-5-1}

| Temperature | Foraging |
| --- | --- |
| 65 F | 100% |
| 63 F | 62% |
| 54 F | 21% |
| 51 F | 6% |

Table: Relative percentage of honey bees foraging at different temperatures (source reference 24) {#tbl:temperature}

The foraging bee's activities would be affected by the temperature shift, slowing pollination down as a result. The percentage of foraging bees who would actually go out and forage decreases as a result of the drop in temperature [@ref24].

The temperature has an influence on that the percentage of foraging bees that go out. The formula for

$$
H_{\mathrm{hive}}=\frac{kF}{t_{\mathrm{flight}}}\eta(T)
$$

Where T is the temperature in  degrees  F, and $\eta$ represents the probability of foraging bees that go out.

$$
\eta(T)=\begin{cases}\frac{1.16\times10^{-17}T^{10.43}}{100},&T\le65^\circ\mathrm{F},\\1,&T>65^\circ\mathrm{F}.\end{cases}
$$

$\eta$(T ) = 1(T > 65 F)

However, the $\eta$ is a probability, meaning when it exceeds 100%, it should only be counted as 100%. When T is larger than 65  degrees  F the $\eta$(T ) equals to 100 percent. The derivative of nhive with respect to

$$
\frac{dn_{\mathrm{hive}}}{dT}=\frac{C_{\mathrm{nectar}}\rho_{\mathrm{flower}}aAhp}{kfN/t_{\mathrm{flight}}}\,8.62\times10^{18}(-10.43)T^{-11.43}=-\mathrm{constant}\,T^{-11.43}\quad(T\le65^\circ\mathrm F)
$$

By differentiating the original equation, we observe that dndThive is negative, thus when temperature increases, the number of hives required decreases and vice versa. dndThive is inversely proportional to T to the power of -11.43.

### Air pollution {#sec:s4-5-2}

We find the PM mass concentration as a vital factor that would influence "honeybee vision", and reduce its efficiency of pollinating [@ref8]. Foraging duration would increase as PM mass concentration and have an exponential relationship. The formula of the number of hives can be rewritten as:

$$
n_{\mathrm{hive}}=\frac{C_{\mathrm{nectar}}\rho_{\mathrm{flower}}aAhp}{kfN\eta(T)/(\delta t_{\mathrm{flight}})}
$$

Here, $\delta$ is the ratio between the foraging time that has air pollution and the standard foraging time.Using the data provided in the article, we can calculate $\delta$ as follows:

$$
\delta=e^{0.004C_{\mathrm{PM}}}
$$

The derivative of nhive with respect to temperature represents how nhive changes when the PM mass concentration is changed.

$$
\frac{dn_{\mathrm{hive}}}{dC_{\mathrm{PM}}}=\frac{C_{\mathrm{nectar}}\rho_{\mathrm{flower}}aAhp}{kfN\eta(T)/t_{\mathrm{flight}}}\,0.004e^{0.004C_{\mathrm{PM}}}=\mathrm{constant}\,e^{0.004C_{\mathrm{PM}}}
$$

dnhive dC PM is positive, thus when the PM mass concentration increases, we would require more hives to complete the pollination, and vice versa.

### Use of pesticide {#sec:s4-5-3}

When a pesticide is introduced to the habitat of bees, we separate bees into 2 categories: uncontaminated and contaminated. The uncontaminated bees are not exposed to pesticides yet the contaminated

$$
\begin{aligned}\frac{dN_U}{dt}&=R\frac{N^2}{K+N^2}-\lambda N_U-\alpha_CN_U,\\\frac{dN_C}{dt}&=(1-\lambda_C)\alpha_CN_U-\lambda N_C,\\\frac{dN}{dt}&=R\frac{N^2}{K+N^2}-\lambda N-\lambda_C\alpha_CN_U.\end{aligned}
$$

dt       K+N

Here, ac is the transition rate from uncontaminated bees NU to contaminated bees NC . It is associated with the concentration of the pesticide in the habitat, but in order to simplify the model, we set it as a constant. $\lambda$C is the extra death rate caused by pesticides. Adding the equation between time and uncontaminated and contaminated bees, we can obtain an equation that indicates the relationship of the total population that may be exposed to pesticides. The introduction of pesticides actually decreases the total population and indirectly influences the number of hives required. We find the derivative of nhive with respect to N represents how nhive changes when the population is changed.

$$
\frac{dn_{\mathrm{hive}}}{dN}=\frac{C_{\mathrm{nectar}}\rho_{\mathrm{flower}}aAhp}{kf\eta(T)/(\delta t_{\mathrm{flight}})}(-N^{-2})=-\frac{\mathrm{constant}}{N^2}
$$

dnhive dN is negative, thus the number of hives decreases with the growth in population, and the pesticides would inhibit the speed of population growth.
