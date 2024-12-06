library(jsonlite)
library(ggplot2)
library(gridExtra)

# 读取 JSON 文件
data <- fromJSON("/Users/jolie/Desktop/school/98-SCSU/3-course-563/project assignment 1/benchmark_data.json")

# 查看数据
print(data)


# 绘制 Giga FLOPS 平均值和标准差
plot_flops <- ggplot(data, aes(x = factor(num_threads), y = flops_mean)) +
  geom_bar(stat = "identity", position = "dodge", fill = "skyblue") +
  geom_errorbar(aes(ymin = flops_mean - flops_std, ymax = flops_mean + flops_std), width = 0.2) +
  labs(title = "Average Giga FLOPS by Number of Threads", x = "Number of Threads", y = "Average Giga FLOPS") +
  theme_minimal()

# 绘制 Giga IOPS 平均值和标准差
plot_iops <- ggplot(data, aes(x = factor(num_threads), y = iops_mean)) +
  geom_bar(stat = "identity", position = "dodge", fill = "orange") +
  geom_errorbar(aes(ymin = iops_mean - iops_std, ymax = iops_mean + iops_std), width = 0.2) +
  labs(title = "Average Giga IOPS by Number of Threads", x = "Number of Threads", y = "Average Giga IOPS") +
  theme_minimal()

# 使用 grid.arrange 将两个图放在一起展示
grid.arrange(plot_flops, plot_iops, ncol = 2)
