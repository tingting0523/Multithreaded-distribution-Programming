library(jsonlite)
library(ggplot2)
library(gridExtra)

# Read the JSON file
data <- fromJSON("/Users/jolie/Desktop/school/98-SCSU/3-course-563/project1/benchmark_data.json")

print(data)


# Plot the Giga FLOPS mean and standard deviation
plot_flops <- ggplot(data, aes(x = factor(num_threads), y = flops_mean)) +
  geom_bar(stat = "identity", position = "dodge", fill = "skyblue") +
  geom_errorbar(aes(ymin = flops_mean - flops_std, ymax = flops_mean + flops_std), width = 0.2) +
  labs(title = "Average Giga FLOPS by Number of Threads", x = "Number of Threads", y = "Average Giga FLOPS") +
  theme_minimal()

# Plot the Giga IOPS mean and standard deviation 
plot_iops <- ggplot(data, aes(x = factor(num_threads), y = iops_mean)) +
  geom_bar(stat = "identity", position = "dodge", fill = "orange") +
  geom_errorbar(aes(ymin = iops_mean - iops_std, ymax = iops_mean + iops_std), width = 0.2) +
  labs(title = "Average Giga IOPS by Number of Threads", x = "Number of Threads", y = "Average Giga IOPS") +
  theme_minimal()

grid.arrange(plot_flops, plot_iops, ncol = 2)
