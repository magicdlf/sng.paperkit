# Model 3 结构检查与拟合方向（新）

## 比换一组参数更重要的发现

用了哪个文件：`pop.csv`，选择6号蜂群说明四阶段不同步的问题。这个例子不是整体蜂群平均规律，其他蜂群仍见Model 1的九宫格。

![6号蜂群四阶段记录。前三个面板与成蜂面板的纵轴范围不同。](assets/observed-colony6-four-stages.png){#fig:model3-stages width=100%}

卵数量在6月13日约69、6月27日约2809、7月11日约1082。原模型若固定产卵b、卵存活率和卵转移率，卵方程可写作 $E_{t+1}=kE_t+b$，其中 $0\leq k<1$。这条确定性递推会单调趋近固定值，不能精确生成先大幅上升再下降的观测序列。若允许测量误差可以近似拟合，但必须评估误差，而不是不断调参数就声称复现了波动。

因此第一步可以问：恒定产卵假设是否需要放宽？时间变化的产卵输入、管理事件或观测误差都可能有关；这份数量表本身不能决定哪一个是原因。

10月31日记录里，卵、幼虫、蛹均为0，但成蜂还有10894。12月12日成蜂记录骤降到2293，随后又恢复；不能只看最后恢复了就宣布前面没有问题，也不能把未成熟阶段的0解释成全群灭绝。应先核查零值、测量、蜂群管理和记录过程。

## 数据自己也要审稿

2022年11月14日，8个蜂群的卵、幼虫、蛹和成蜂数都与10月31日、11月28日两次记录的算术中点一致（浮点误差内）。这强烈提示可能有插值行，但还未获得原始处理说明确认。拟合前先标记，不能把这些点当成额外独立测量。可比较包含与暂不包含这些行的拟合结果。

9个蜂群里只有5个记录到次年5月。序列提前结束不等于已经确认蜂群死亡。跨日期平均应说明每次用了哪些蜂群，避免把样本退出当成季节效应。

## 成品段落候选

The observations reveal a structural limitation of the constant-input egg equation. With fixed survival and transition probabilities, the deterministic egg population approaches a steady value monotonically. The observed increase followed by a decrease therefore cannot be reproduced exactly by that equation. We will first assess observation uncertainty and the assumption of constant egg input before adding further weather coefficients.

## 下一步拟合 还没有做

先从一个蜂群的四状态模型开始；明确观测映射；固定阶段时长；只拟合少量参数。按时间留出一段记录检验，标记疑似插值点。画观测点和模型曲线的叠图，同时报告各阶段误差。食物变量暂不加入，因为当前数量与温度文件没有提供食物储量观测。
