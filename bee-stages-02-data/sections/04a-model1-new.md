# Model 1 分组与参数（新）

## 先拿现实初始状态替换拍脑袋的初始状态

用了哪个文件：`data/observations-v1/raw/pop.csv`，保留原文件；只把 `Pupae ` 列名末尾空格去掉，将月/日/年转为日期，按蜂群分组和日期排序。没有补零、插值或四舍五入后再计算。185条记录、9个蜂群，没有重复的蜂群与日期组合，四阶段之和与Total相差不超过1。

2022年5月30日的初始记录如下。小数是面积换算等得到的数量估计，不代表半只蜂。

| 蜂群 | Eggs | Larvae | Pupae | Adults |
| --- | --- | --- | --- | --- |
| 1 | 506.6 | 1,473.7 | 2,486.9 | 2,954.0 |
| 2 | 92.1 | 1,312.5 | 4,674.4 | 5,572.0 |
| 4 | 391.5 | 3,131.6 | 11,766.5 | 14,738.0 |
| 5 | 92.1 | 1,128.3 | 5,641.5 | 5,156.0 |
| 6 | 322.4 | 1,957.3 | 2,348.7 | 11,306.0 |
| 7 | 230.3 | 46.1 | 2,901.3 | 3,876.0 |
| 8 | 1,312.5 | 990.1 | 3,776.3 | 5,929.0 |
| 9 | 0.0 | 0.0 | 115.1 | 12,932.0 |
| 10 | 184.2 | 2,072.4 | 3,753.3 | 11,885.0 |

Table: 原表同一天的各阶段初始数量估计。 {#tbl:observed-initial}

对模型直接有用：初始条件应按蜂群填写，不再让所有蜂群统一使用3000、4500、10000、15000、6000。数据只有成蜂A，原模型有巢内蜂H和采集蜂F，所以观测对应关系是 $A=H+F$，并不能从这张表读出H和F各占多少。

![九个蜂群的成蜂数量，统一日期轴和数量轴。](assets/observed-adults-nine-colonies.png){#fig:model1-observed width=100%}

## 成品段落候选

We initialized the observed stages using the first record of each colony rather than a common assumed population. The data distinguish eggs, larvae, pupae and adults, whereas our model separates adults into hive bees and foragers. Consequently, adult observations constrain the sum of these two model states, not either state individually. Their initial split requires additional evidence or an explicitly stated assumption.

## 还没完成

- 先拟合四组，还是保留五组并承认成蜂拆分不可直接观测？待决定。
- 表内记录大多约两周一次，不是每日出生死亡或转移记录。不能用相邻数量差直接当死亡数。
- 先固定有文献依据的阶段时长，再选少量未知参数；不要把所有初始状态和所有转移率同时自由拟合。
