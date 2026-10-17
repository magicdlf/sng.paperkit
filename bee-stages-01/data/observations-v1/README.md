# 蜂群实测数据补充包

状态：原始CSV尚未下载，不能据此拟合。请从下方公开页面下载 pop.csv，放入 raw/pop.csv，再运行 prepare.py。此包不修改原工地正文或模型。

来源：Chen et al. (2025), Negative effects of excessive heat on colony thermoregulation and population dynamics in honey bees. DOI 10.5061/dryad.5tb2rbpg5。
https://datadryad.org/dataset/doi:10.5061/dryad.5tb2rbpg5

研究说明：2022年亚利桑那州夏季，9个蜂群约每两周观测一次。数量来自照片计数与现场估计，非逐日精确清点。先按单蜂群画观测点，不跨蜂群拼时间序列，不把缺测填成0，不插值冒充实测。Adults没有细分巢内蜂与采集蜂。

| 原字段 | 含义 |
|---|---|
| Colony.ID | 蜂群编号 |
| demography | 测量日期，须查看原始字符串确认日期格式 |
| Eggs | 卵数量估计 |
| Larvae | 幼虫数量估计 |
| Pupae | 蛹数量估计 |
| Adults | 成蜂数量估计 |
| Total | 原表总量，检查是否等于四组之和 |

学生任务：先画一个蜂群的四组观测点，说明数据实际上测到了什么，再决定原模型哪些状态可直接对照、哪些参数需要文献约束。暂不要求加入食物或天气模型，也不预设能拟合全部参数。

校验与整理：python3 prepare.py。脚本先核对官方SHA256；若文件不是本版本就停止。原文件不改写，按蜂群拆分后的原字段CSV位于 prepared/，含行数、缺失值和总量检查的报告位于 quality.json。日期不自动猜测，不排序或补齐；先核对格式再分析。
