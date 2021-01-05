def process_dataframe(main_df):
    import pandas as pd
    # from sklearn.preprocessing import StandardScaler

    main_df.fillna(main_df.mean(), inplace=True)
    main_df.drop(columns='employee_id', inplace=True)
    main_df = pd.get_dummies(main_df, columns=['department', 'salary'], drop_first=True)

    # main_df = StandardScaler().fit_transform(main_df)
    
    return main_df
