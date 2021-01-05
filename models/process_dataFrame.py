def process_dataframe(main_df):
    import pandas as pd

    main_df.fillna(main_df.mean(), inplace=True)
    main_df.drop(columns='employee_id', inplace=True)
    main_df = pd.get_dummies(main_df, columns=['department', 'salary'], drop_first=True)
    
    return main_df.to_numpy()
