# Model 2 天气与数据对齐（新）

## 真正下载到的天气是什么

用了哪个文件：`data/observations-v1/raw/airport_summer.csv`。按date聚合观测温度，先算每个日历日的记录最高温，再统计天数。覆盖2022年5月18日至8月22日，共97天，最高记录45°C，其中27天的日内记录最高温超过40°C。每天只有17至38条记录，因此这里是采样记录的日最高值，不保证捕捉到真实连续时间最高温。

对模型直接有用：这份文件是温度资料，不能拿来验证“雨天45%的采集蜂出门”。它没有给本分析所需的降雨、出勤或花朵访问次数。`pop.csv`虽然延伸到2023年5月，但这份天气文件只到2022年8月，不能直接覆盖全年。

## 对齐提纲

1. 选同一蜂群相邻两个实测日期，使用实际间隔天数。
2. 从天气文件中取这段间隔内有记录的日期，而不是只取末日天气。
3. 先画温度暴露与各阶段数量变化的对照。标记天气覆盖不全的间隔，先不填补。
4. 同一天多个蜂群共用机场天气，不等于得到了多个独立天气实验。

## 成品段落候选

The available weather file contains sampled air temperatures rather than rainfall or foraging activity. We therefore cannot estimate the proposed rainy-day activity coefficient from this file. Weather observations cover only the summer portion of the population series. Comparisons must use matching calendar intervals and distinguish an association with temperature from an identified causal effect.

## 原模型里先别动的数

$a=0.45$、产卵乘0.85、转移乘0.7、生存率0.94仍是原工地假设，不因找到了温度文件就变成实测参数。还缺出勤记录、降雨记录，或能把具体气象变量连接到具体转移机制的文献。这里暂不硬凑一张“温度导致衰退”的图。
