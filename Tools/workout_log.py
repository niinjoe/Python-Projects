import pandas as pd

# Create a dictionary with exercise names as keys and an empty list as values
exercises = {
    'Bench Press': [''] * 5,
    'Squats': [''] * 5,
    'Deadlifts': [''] * 5,
    'Pull-Ups': [''] * 5,
    'Push-Ups': [''] * 5,
    'Barbell Rows': [''] * 5,
    'Lunges': [''] * 5,
    'Shoulder Press': [''] * 5,
    'Bicep Curls': [''] * 5,
    'Tricep Dips': [''] * 5,
    'Planks': [''] * 5,
    'Crunches': [''] * 5,
    'Leg Press': [''] * 5,
    # Add more exercises if needed
}

# Create DataFrames for Overview and Exercise Log
overview_df = pd.DataFrame(exercises)
exercise_log_df = pd.DataFrame(columns=['Exercise', 'Set Number', 'Weight', 'Reps', 'Date'])

# Create an Excel writer using pandas
with pd.ExcelWriter('workout_log_template.xlsx') as writer:
    overview_df.to_excel(writer, sheet_name='Overview', index=False)
    exercise_log_df.to_excel(writer, sheet_name='Exercise Log', index=False)
