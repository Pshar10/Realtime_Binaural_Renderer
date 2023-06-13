import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Data: scores for each question by the test subjects (5 in total)
scores = {
    'Stage 1': {
        'Quality': np.array([4, 3, 5, 5, 4]),
        'Localization': np.array([5, 4, 5, 5, 4]),
    },
    'Stage 2 (Head Motion)': {
        'Stability': np.array([5, 5, 5, 4, 3]),
        'Latency': np.array([4, 4, 4, 5, 4]),
        'Localization': np.array([5, 5, 5, 4, 4]),
    },
    'Stage 3 (Head and Body motion)': {
        'Stability': np.array([5, 4, 4, 5, 4]),
        'Latency': np.array([4, 4, 4, 4, 3]),
        'System move with you': np.array([4, 5, 4, 3, 5]),
        'Localization': np.array([4, 4, 5, 5, 4]),
    },
    'Final Stage': {
        'Overall Experience': np.array([4, 5, 5, 5, 4])
    }
}

# Calculate means and 95% confidence intervals
means = {stage: {q: np.mean(vals) for q, vals in questions.items()} for stage, questions in scores.items()}
conf_intervals = {stage: {q: stats.sem(vals) * stats.t.ppf((1 + 0.95) / 2., len(vals)-1) for q, vals in questions.items()} for stage, questions in scores.items()}

for stage, questions in scores.items():
    plt.figure(figsize=(8, 4))
    
    names = list(questions.keys())
    stage_means = [means[stage][q] for q in names]
    stage_conf_intervals = [conf_intervals[stage][q] for q in names]
    bar_positions = np.arange(len(names))

    bars = plt.bar(bar_positions, stage_means, yerr=stage_conf_intervals, alpha=0.8, color='skyblue', capsize=10, width=0.5)
    plt.title(stage)
    plt.ylabel('Average Scores')
    plt.xticks(bar_positions, names)
    plt.ylim(0, 6)  # to accommodate error bars

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() -0.2, yval+0.1, round(yval,2), ha='left', va='center')

    plt.xlim(-0.8, len(names))  # added this line to adjust x-axis limits

    # Reduce spacing between bars
    # plt.subplots_adjust(wspace=0.21)

# Show all the figures at once
plt.show()
