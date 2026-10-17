# What the downloaded observations show

Source: Chen et al., Dryad DOI 10.5061/dryad.5tb2rbpg5. The original pop.csv contains 185 dated records from nine colonies, from 30 May 2022 to 15 May 2023. Fractional counts are retained because the stage quantities are estimates. These figures use that CSV, not a published model figure.

![Adult counts for all nine colonies, with the same date and count scales.](assets/observed-adults-nine-colonies.png){#fig:observed-adults width=100%}

Colony trajectories differ. Colony 9 rises from 12,932 to 25,171 adults across its full record, while Colony 5 falls from 5,156 to 3,647. Four series end earlier than the others; their disappearance from the table does not establish why recording stopped. Do not replace these missing tails by zero or treat changing-membership averages as a seasonal trajectory.

![Egg, larval, pupal and adult counts for Colony 6. Scales differ across panels.](assets/observed-colony6-four-stages.png){#fig:observed-stages width=100%}

Colony 6 illustrates a difference between adult abundance and recruitment-stage abundance. On 31 October 2022, all three immature stages are recorded as zero, while 10,894 adults remain. On 15 May 2023 the table records immature stages again and 11,807 adults. A zero stage count therefore does not by itself establish irreversible colony loss; measurement and management context must be checked.

Using the same five colonies throughout (5, 6, 7, 8, 9), mean larvae rise from 921 on 16 January to 2,911 on 27 February 2023; mean adults rise from 6,037 to 8,873. This describes a shared-subset change, not evidence that food or weather caused it. The subset excludes incomplete records and is not necessarily representative of all nine colonies.

The sampling is mostly about two weeks apart and does not directly measure daily deaths, births or transition probabilities. Some adjacent values also match linear interpolation unusually closely; consult the original processing and field records before treating every row as an independent measurement. Keep these limitations visible when fitting a stage model.
