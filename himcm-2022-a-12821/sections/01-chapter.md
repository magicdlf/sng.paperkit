# Introduction {#sec:s1}

## Background {#sec:s1-1}

Colony Collapse Disorder (CCD) was coined in 2007 to characterize the global collapse in honeybee colonies [@ref27]. These colonies play a crucial role in agricultural productivity and the maintenance of natural ecosystems [@ref21]. Bee pollination is vital for producing one-third of the food people consume. In the US, the value of honeybee pollination is from \$15 to \$20 billion each year [@ref10]. Beekeepers have lost between 30 and 45 percent of their colonies each year for the past ten years, with the most recent losses in 2019-2020 topping 40 percent [@ref7]. The beekeepers promptly replace the lost colonies, therefore even though there are progressively more lost colonies, the overall population has not diminished [@ref14]. Moreover, beekeepers may utilize cold storage to assist the colony in successfully surviving the winter [@ref9]. In the context of apiculture, these treatment procedures come with a hefty price. Therefore, the decline of the honeybee colony represents an issue for the world's economy, agriculture, and environment.

Honeybees are social insects that reside in colonies comprised of a single egg-laying queen, zero to several thousand reproductive males, tens of thousands of reproductively sterile female workers, and 10,000-30,000 eggs, larvae, and pupae [@ref3] [@ref15] [@ref26]. Thousands of worker bees work together to construct nests, gather food, and raise young. With respect to their level of adulthood, each member has a specific obligation to fulfill. But the entire colony must work together to survive and reproduce[@ref23]. A worker honeybee's life cycle typically includes the following stages: egg, larva, pupa, capped, adult, and foraging.

We aim to develop a model that can accurately and effectively predict the population of a honeybee colony over time by taking into account a variety of factors, including the population size, the lifespan of a honeybee, virus infection, and climate change with regards to the seasons. The survival rate of colonies can be enhanced by using this model, which sheds light on critical processes and probable contributing elements. This model assists in addressing the economic, environmental, and agricultural crisis brought on by the reduction of the honeybee colonies.

## Restatement of Questions {#sec:s1-2}

Our research focuses mostly on the Colony Collapse Disorder (CCD) concern, which causes honeybee populations to drop globally. Hence, building models to estimate honeybee populations is our primary objective.

- A continuous-time dynamic model should first be constructed to describe a honeybee colony's (a honeybee hive's) population over time. The variables that could affect the population of honeybees should be included in the model. For instance, the number of births during a certain time frame may be impacted by egg-laying rates.
- Second, we need to conduct a sensitivity analysis on the population model to see how much each factor affects the size of the honeybee colony. We will alter each factor while holding the others constant and then quantitatively examine how it impacts the colony population. The factors can then be ranked in order of impact.
- Third, we need to create a model to estimate how many honeybee hives are required to pollinate a 20-acre plot of land with crops in the best possible way.
- Last but not least, we would develop a one-page, non-technical blog for a website to present the data we have discovered during our research. This blog may address how a honeybee colony's population will evolve over time and aims to demonstrate our model's findings and their practical application to non-technical readers.

## Assumptions and Justifications {#sec:s1-3}

Several assumptions are listed to simplify the problem. The assumptions and their justifications are listed below.

- Assumption 1: There is an Allee effect within the honeybee population where the survival probability of the new brood increases in the total population. Justification: Colony Collapse Disorder needs to be considered, so the population isn't merely growing but has the possibility to collapse into extinction.
- Assumption 2: We consider the honeybee population from a macroscopic view, regardless of each age-stages. Justification: As we are interested in the overall population, various age-stages are abstracted from the model.
- Assumption 3: We assume that the honeybee population does not have natural enemies and can only die out of natural causes or infections. Justification: We consider honeybee colonies under a hospitable environment and ignore the factors of predators and natural disasters for simplification.
