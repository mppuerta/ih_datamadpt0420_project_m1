

# Function to group by the columns below defined and count by all the unique id's (Quantity column defined in the
# acquisition module). The function also calculates the Percentage column.

def func_analysis(rural):
    group_rural = rural.groupby(['Country', 'Job_name', 'Rural'], as_index=False).count()
    group_rural['Percentage'] = group_rural['Quantity'].apply(
        lambda qtty: str((qtty * 100 / group_rural['Quantity'].sum()).round(2)) + '%')
    return group_rural

def filtering(rural,country):
    grouped_analysis = func_analysis(rural)
    filter_analysis = grouped_analysis[grouped_analysis['Country'].isin(country)]
    return filter_analysis


def analyze(rural, country):
    main_analysis = func_analysis(rural)
    if country is not None:
        filtered_analysis = filtering(main_analysis, country)
        print(f'Filtered by {country} and exported to csv')
        filtered_analysis.to_csv(f'data/results/{country}country_analysed_rural_info.csv', index=False)
        return filtered_analysis

    else:
        print('No country filter. Exported results to csv')
        main_analysis.to_csv('data/results/analysed_rural_info.csv', index=False)
        return main_analysis


