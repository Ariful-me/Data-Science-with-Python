import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('ultimate_student_productivity_dataset_5000 copy.csv')


agg_df = df.groupby(['academic_level', 'gender']).agg({
    'sleep_hours': 'mean',
    'exam_score': 'mean',
    'study_hours': 'mean'
}).reset_index()


agg_df['label'] = agg_df['academic_level'].str[:2].str.upper() + "-" + agg_df['gender'].str[:1].str.upper()


plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 7))
bg_color = '#0e1628' # Matches the deep navy in your image
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)


colors = ['#d65a31', '#c1272d', '#2ecc71', '#f1c40f', '#1abc9c', '#3498db', '#9b59b6', '#e67e22', '#ecf0f1']
scatter = ax.scatter(
    agg_df['sleep_hours'], 
    agg_df['exam_score'], 
    s=agg_df['study_hours'] * 800, 
    c=colors[:len(agg_df)], 
    alpha=0.85, 
    edgecolors='white', 
    linewidth=1.5,
    zorder=3
)


for i, row in agg_df.iterrows():
    ax.annotate(
        row['label'], 
        (row['sleep_hours'], row['exam_score']),
        color='white', 
        fontweight='bold', 
        ha='center', 
        va='center',
        fontsize=9,
        zorder=4
    )


ax.set_xlabel('Mean Sleep Hours →', color='#7f8c8d', fontsize=11)
ax.set_ylabel('Mean Exam Score →', color='#7f8c8d', fontsize=11)
ax.grid(True, linestyle='--', color='#2c3e50', alpha=0.5, zorder=0)


for spine in ax.spines.values():
    spine.set_edgecolor('#3a475a')

plt.title('Sleep Hours vs Exam Score (Grouped Data)', color='white', pad=20)
plt.tight_layout()
plt.show()